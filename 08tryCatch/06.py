import json

raw_data = queryDB(uid)
try:
    data = json.loads(raw_data)

except json.JSONDecodeError as err:
    print('JSON Error: {}'.format(err))
except Exception as err:
    print('Other Error: {}'.format(err))