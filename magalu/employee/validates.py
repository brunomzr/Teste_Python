import re

def isValidEmail(email):
    if len(email) > 7:
        if re.match('^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$)', email) is not None:
            return True
        return False
    else:
        return False