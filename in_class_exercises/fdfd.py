import json 
data = {"name": "Rio", "courses": 3, "enrolled": True}
Jenna = {"name": "Jenna", "courses": 5, "enrolled": True}

# 1. dump(): Python dictionary → JSON file
with open("saved_data.json", "w") as f:
   json.dump(Jenna, f, indent=10, sort_keys=True)

# 2. load(): JSON file → Python dictionary
with open("saved_data.json", "r") as f:
    loaded_data = json.load(f)
print(loaded_data)

# 3. dumps(): Python dictionary → JSON string
json_string = json.dumps(data, indent=0, sort_keys=True)
print(json_string)

# 4. loads(): JSON string → Python dictionary
parsed_data = json.loads(json_string)

print("loads() result:", parsed_data)




