import re


def validate_feild(data):
    if re.match(r'[^@]+@[^@]+\.[^@]+', data):
        return 'email'
    elif re.match(r'(^(\+?7)|^[8])(\s?)[0-9]{3}(\s?)[0-9]{3}(\s?)[0-9]{2}(\s?)[0-9]{2}', data):
        return 'phone'
    elif re.match(r'(^[0-3]?[0-9]\.[0-1]?[0-9]\.[0-9]{4}$)|(^[0-9]{4}\-[0-1]?[0-9]\-[0-3]?[0-9]$)', data):
        return 'date'
    else:
        return 'text'
