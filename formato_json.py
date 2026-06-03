import json

# some JSON
x = '{"name":"jhon", "age":30 "city":"New York"}'

# Parse x
y = json.loads(x)

# the result is a python dictionary 
print(y)


# a python object (dict):

x = {
    "name": "jhon",
    "age": 30,
    "ciry": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
