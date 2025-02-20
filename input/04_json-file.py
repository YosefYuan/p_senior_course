import json

params = {
    "symbol": "123456",
    "price": 123.45,
    "quantity": 1000,
    "source": "file"
}

with open('params.json', 'w') as fout:
    params_str = json.dump(params, fout)

with open('params.json', 'r') as fin:
    original_params = json.load(fin)

print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))