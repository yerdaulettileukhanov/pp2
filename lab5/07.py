import re

def rplc(matchObject):
    return matchObject.group("b").upper()

txt = input()

pattern = r"(?P<a>_+)(?P<b>\w)"

x = re.sub(pattern, rplc, txt)

if x[0].upper():
    print(x[0].lower() + x[1:])
else:
    print(x)