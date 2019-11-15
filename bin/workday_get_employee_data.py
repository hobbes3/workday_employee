#!/usr/bin/env python
# hobbes3

import logging
from requests.auth import HTTPBasicAuth
from splunk_rest.splunk_rest import session_id, config, script_args, retry_session, rest_wrapped

@rest_wrapped
def workday_rest_api():
# WORKDAY EMPLOYEES
    logger.info("Getting employee list...")
    r = s.get(workday_url, params=workday_params, auth=workday_auth)

    if r and r.text:
        r_json = r.json()
        employees = r_json["Report_Entry"]
        employee_count = len(employees)

        logger.info("Found employees.", extra={"employee_count": employee_count})

        data = ""
        for employee in employees:
            employee["__session_id"] = session_id

            event = {
                "index": WORKDAY_INDEX,
                "sourcetype": "workday_employee_json",
                "source": __file__,
                "event": employee,
            }

            data += json.dumps(event)

        logger.info("Sending data to Splunk...")
        s.post(HTTP_URL, headers=HTTP_HEADERS, data=data)

if __name__ == "__main__":
    logger = logging.getLogger("splunk_rest.splunk_rest")
    s = retry_session()

    workday_auth = HTTPBasicAuth(
        config["workday_api"]["user"],
        config["workday_api"]["password"],
    )
    workday_url = config["workday_api"]["url"]
    workday_params = config["workday_api"]["params"]

    workday_rest_api()
