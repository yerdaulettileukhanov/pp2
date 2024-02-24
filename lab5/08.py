import re

txt = input("Enter text here: ")

pattern = r"[A-Z]"

x = re.split(pattern, txt)

print(x)