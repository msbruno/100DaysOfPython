import json

data =  '{ "name":"Bruno", "age":36, "city":"Porto Alegre"}'
json_object = json.loads(data)
assert json_object["age"] == 36
assert json_object["name"] == "Bruno"
assert json_object["city"] == "Porto Alegre"
