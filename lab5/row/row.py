import re
import csv

file = open("row.txt", "r", encoding="UTF-8")

data = file.read()

pattern = r"\n(?P<no>\d+)\.\n(?P<name>.+)\n(?P<quantity>.+),0+\s+x(?P<price>.+),0+\w\n(?P<total>.+),0+\s+"

results = re.finditer(pattern, data)

with open('data.csv', 'w', newline='',encoding="utf8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['№', 'Name', 'Quantity', 'Price', 'Total'])
    for x in results:
        writer.writerow([
            x.group('no'),
            x.group('name'),
            x.group('quantity'),
            x.group('price'),
            x.group('total')
        ])