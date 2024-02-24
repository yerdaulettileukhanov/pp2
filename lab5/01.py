import re

txt = input("Enter text here: ")

pattern = r"ab*"

x = re.findall(pattern, txt)

print(x)