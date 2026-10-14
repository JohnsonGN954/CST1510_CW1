"""
RECORD CHECK  -  my version
===========================

Name  : Goodluck Johnson 
Lane  :  Cyber
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
WARNING_PERCENT = 25           # failure rate at or above this = WARNING
OVER_LIMIT_PERCENT = 50        # failure rate above this = OVER LIMIT
 
 
def check_record(value, limit):
    """Return the successful logins, failure rate (%) and status for one source IP."""
    difference = limit - value            # attempts that succeeded
    if limit == 0:
        percent = 0.0                     # no attempts, so nothing to flag
    else:
        percent = value / limit * 100
    if percent > OVER_LIMIT_PERCENT:
        status = "OVER LIMIT"
    elif percent >= WARNING_PERCENT:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status
 
 
def print_report(label, value, limit, difference, percent, status):
    """Print one line of the report for a single source IP."""
    print(f"{label}: {value:.0f} failed of {limit:.0f} attempts | "
          f"{percent:.1f}% failed | {difference:.0f} succeeded | {status}")
# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.
records = [
    {"label": "10.0.0.5",     "value": 12,  "limit": 400},   # 3.0%  -> OK
    {"label": "192.168.1.20", "value": 120, "limit": 400},   # 30.0% -> WARNING
    {"label": "172.16.0.9",   "value": 310, "limit": 400},   # 77.5% -> OVER LIMIT
    {"label": "10.0.0.77",    "value": 50,  "limit": 100},   # 50.0% -> WARNING (not over 50)
]
# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"],
                 difference, percent, status)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
