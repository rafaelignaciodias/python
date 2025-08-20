# core 076

# defining a dictionary
person = {
    "first_name": "Coder",
    "last_name": "Smith",
    "age": 45,
    "height": 1.87,
    "address": [{"city": "São Paulo"}, {"city": "Ottawa"}],
}
print(person["first_name"])
print(person["age"])

for data in person:
    print(data, person[data])
