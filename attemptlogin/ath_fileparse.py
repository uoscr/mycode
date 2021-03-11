#!/usr/bin/python3

# parse keystone.common.wsgi and return number of successful login attempts
login = 0 # counter for Ath

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Loaded 2" in line:
            login += 1 # this is the same as loginfail = loginfail + 1

print("The number of successful in the logs", login)