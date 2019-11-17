#!/usr/bin/env python
# hobbes3

import logging
import json
import splunk_rest.splunk_rest as sr
from splunk_rest.splunk_rest import rest_wrapped
from requests.auth import HTTPBasicAuth

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
            employee["__session_id"] = sr.session_id

            event = {
                "index": sr.config["workday_api"]["index"],
                "sourcetype": "workday_employee_json",
                "source": __file__,
                "event": employee,
            }

            data += json.dumps(event)

        logger.info("Sending data to Splunk...")
        s.post(sr.config["hec"]["url"], headers=sr.config["hec"]["headers"], data=data)

if __name__ == "__main__":
    logger = logging.getLogger("splunk_rest.splunk_rest")
    s = sr.retry_session()

    workday_auth = HTTPBasicAuth(
        sr.config["workday_api"]["user"],
        sr.config["workday_api"]["password"],
    )
    workday_url = sr.config["workday_api"]["url"]
    workday_params = sr.config["workday_api"]["params"]

    workday_rest_api()
