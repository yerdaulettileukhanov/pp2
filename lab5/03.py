import re

txt = input("Enter text here: ")

pattern = r"([a-z]+_[a-z]+)+"

x = re.findall(pattern, txt)

print(x)