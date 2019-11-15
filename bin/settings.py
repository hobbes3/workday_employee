# Optional variable for your convienence.
DEBUG = True

# Number of threads to create for multiprocessing.
THREADS = 1
# Sleep for a random seconds between SPLUNK_MIN and SLEEP_MAX (floating number) before a request call.
# Set both SLEEP_ to 0 to disable sleeping.
SLEEP_MIN = 0
SLEEP_MAX = 0
# Set TEXT_TRUNCATE to 0 to log entire data on sending and receiving (not recommended).
TEXT_TRUNCATE = 300

# Log will be saved at $SPLUNK_HOME/var/log/splunk/ and can be searched via `index=internal`.
# Size of each log file.
# 1 MB = 1 * 1024 * 1024
LOG_ROTATION_BYTES = 25 * 1024 * 1024
# Maximum number of log files.
LOG_ROTATION_LIMIT = 5

# No trailing slash.
SPLUNK_HOME = "/opt/splunk"

# Splunk or Cribl HEC info.
HTTP_URL = "https://localhost:8088/services/collector"
HTTP_HEADERS = {
    "Authorization": "Splunk 89e07dcb-1425-4175-843e-b12d41b9f50a"
}

# Set REST API specific variable like API keys and Splunk index below.

# Workday REST API info.
WORKDAY_USER = "ISU_WD-Drive To Splunk_L&D"
WORKDAY_PASS = "Welcome123()"
WORKDAY_INDEX = "workday"
