import re

txt = input("Enter text here: ")

pattern = r"a.*b"

x = re.findall(pattern, txt)

print(x)