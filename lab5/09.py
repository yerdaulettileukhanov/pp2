import re

txt = input()

pattern = r"([a-z]+)([A-Z])"

x = re.sub(pattern, r"\1 \2", txt)

print(x)