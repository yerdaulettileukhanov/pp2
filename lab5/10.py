import re

def repl(matchObject):
    return matchObject.group("a") + "_" + matchObject.group("b").lower()

txt = input()

pattern = r"(?P<a>[a-z0-9])(?P<b>[A-Z]+)"

x = re.sub(pattern, repl, txt)

print(x)