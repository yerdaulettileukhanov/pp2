import re

txt = input("Enter text here: ")

pattern = r"[A-Z][a-z]+"

x = re.findall(pattern, txt)

print(x)