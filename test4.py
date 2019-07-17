import json

with open("config.json")as f:
    param = json.load(f)

print(param["tableName"])
print(param["credentials"]["host"])
print(param["credentials"]["user"])
print(param["credentials"]["password"])
