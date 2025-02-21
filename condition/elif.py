l = [1, 2, 3, 4]
for item in l:
    print(item)


d = {
    'name': 'jason',
    'dob': '2000-01-01',
    'gender': 'male'
}

for key in d:
    print(key)


for v in d.values():
    print(v)


for k, v in d.items():
    print('key: {}, value: {}'.format(k, v))


l = [1, 2, 3, 4, 5, 6]
for index in range(0, len(l)):
    if index < 4:
        print(l[index])


l = [1, 2, 3, 4, 5, 6, 7]
for index, item in enumerate(l):
    if index < 4:
        print(item)

name_price = {}
name_color = {}

for name, price in name_price.items():
    if price < 1000:
        if name in name_color:
            for color in name_color[name]:
                if color != 'red':
                    print('name: {}, color: {}'.format(name, color))

        else:
            print('name: {}, color: {}'.format(name, 'None'))