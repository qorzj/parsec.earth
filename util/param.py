import re
import web


def isEmail(text):
    if re.match("^(\\w)+(\\.\\w+)*@(\\w)+((\\.\\w+)+)$", text):
        return True
    return False

inputParam = {
        'password': (
            "is too short", lambda x: len(x)>=8,
            "is too long", lambda x: len(x)<=64,),
        'email': (
            "format error", isEmail,
            ),
        's': (
            "is empty", lambda x: x,
            ),
        'n': (
            "value error", lambda x: x>=0,
            ),
        'restMethod': (
            "value error", (lambda x: x in ['GET', 'POST', 'DELETE']),
            ),
        }

mapping = {
    'n': (lambda x: web.intget(x, None)),
}


def mapInput(value, tipe):
    if not value or tipe not in mapping:
        return value
    return mapping[tipe](value)


def checkInput(value, tipe, isMust):
    if value is None or value == '':
        if isMust:
            return 'is empty'
        return None
    for msg, checkFunc in web.utils.group(inputParam[tipe], 2):
        if not checkFunc(value):
            return msg
    return None
