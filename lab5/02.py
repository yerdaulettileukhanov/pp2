import re

txt = input("Enter text here: ")

pattern = r"ab{2,3}"

x = re.findall(pattern, txt)

print(x)