#!/usr/bin/env python
# hobbes3

from splunk_rest.splunk_rest import *
from requests.auth import HTTPBasicAuth

@rest_wrapped
def workday_rest_api():
# WORKDAY EMPLOYEES
    log("Getting employee list...")
    r = s.get(workday_url, params=workday_params, auth=workday_auth)

    if r and r.text:
        r_json = r.json()
        employees = r_json["Report_Entry"]
        employee_count = len(employees)

        log("Found employees.", extra={"employee_count": employee_count})

        data = ""
        for employee in employees:
            event = {
                "index": WORKDAY_INDEX,
                "sourcetype": "workday_employee_json",
                "source": script_file,
                "event": employee,
            }

            data += json.dumps(event)

        logger.info("Sending data to Splunk...")
        s.post(HTTP_URL, headers=HTTP_HEADERS, data=data)

if __name__ == "__main__":
    s = retry_session()

    workday_auth = HTTPBasicAuth(
        WORKDAY_USER,
        WORKDAY_PASS
    )
    workday_url = "https://services1.myworkday.com/ccx/service/customreport2/splunk/tetang/SPLK_L_D_Headcount"
    workday_params = {
        "format": "json"
    }

    workday_rest_api()
