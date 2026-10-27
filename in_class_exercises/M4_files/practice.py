import json

data = {"1901": ["Chemistry", "Physics"], "1902": ["Peace"]}
print(type(data))   # <class 'dict'>
print(data)
print("_______________________________________________________________________________")

text = json.dumps(data, indent=2)
print(type(text))   # <class 'str'>
print(text)

print("_______________________________________________________________________________")

back = json.loads(text)

print(type(back))      # <class 'dict'>
print(back)    # ['Chemistry', 'Physics']  ← you can use it like a dict again
print(back == data)    # True
print("_______________________________________________________________________________")

with open("demo.json", "w") as f:
    result = json.dump(data, f, indent=2)

print(result)   # None  ← dump returns nothing; the JSON went into the file

with open("demo.json") as f:
    loaded = json.load(f)

print(type(loaded))     # <class 'dict'>
print(loaded == data)   # True