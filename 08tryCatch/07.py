d = {'name': 'jason', 'age': 20}

# try: 
#     value = d['dob']

# except KeyError as err:
#     print('KeyError: {}'.format(err))


if 'dob' in d:
    print(d['dob'])