attributes = ['name', 'dob', 'gender']
values = [
    ['jason', '2000-01-01', 'male'],
    ['mike', '1999-01-01', 'male'],
    ['nancy', '2001-02-01', 'female']
]

print(dict(zip(attributes, values[0])))

[dict(zip(attributes, value)) for value in values]

result = []
for value in values:
    item = dict(zip(attributes, value))
    result.append(item)
print(result)