import re

txt = input("Enter text here: ")

pattern = r"\s|\.|\,"

x = re.sub(pattern, ":", txt)

print(x)