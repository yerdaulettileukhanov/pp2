# Don't name file as json when working with json. Because Python will understand it as a json.py module! Notes for future
import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("\nInterface Status\n================================================================================")
print("DN                                                 Description           Speed    MTU\n-------------------------------------------------- --------------------  ------  ------")
print(f"{data["imdata"][0]["l1PhysIf"]["attributes"]["dn"]}                              {data["imdata"][0]["l1PhysIf"]["attributes"]["fecMode"]}   {data["imdata"][0]["l1PhysIf"]["attributes"]["mtu"]}")
print(f"{data["imdata"][1]["l1PhysIf"]["attributes"]["dn"]}                              {data["imdata"][1]["l1PhysIf"]["attributes"]["fecMode"]}   {data["imdata"][1]["l1PhysIf"]["attributes"]["mtu"]}")
print(f"{data["imdata"][2]["l1PhysIf"]["attributes"]["dn"]}                              {data["imdata"][2]["l1PhysIf"]["attributes"]["fecMode"]}   {data["imdata"][2]["l1PhysIf"]["attributes"]["mtu"]}\n")