d1 = {
    'name': 'jason',
    'age': 20,
    'gender': 'male'
}

d2 = dict({
    'name': 'jason',
    'age': 20,
    'gender': 'male'
})

d3 = dict([
    ('name','jason'),
    ('age', 20),
    ('gender', 'male')
])

d4 = dict(
    name='jason',
    age=20,
    gender='male'
)

d1 == d2 == d3 == d4 #True


s1 = {1,2,3}
s2 = set([1,2,3])
s1 == s2 #True


s = {1, 'hello', 5.0}

d = {'name': 'jason', 'age': 20}
d['name'] # 'jason'

d['location'] # Error

d.get('name') # 'jason'
d.get('location', 'null') # 'null'


s = {1,2,3}
s[0] # Error


# check if a value exist in a dict or set, you should use the the syntax like : value in dict / set

s = {1,2,3}
1 in s  #True
10 in s # False

d = {'name': 'jason', 'age': 20}
'name' in d # True
'location' in d # False


# operation: add, delete, update
d = {'name': 'jason', 'age': 20}
d['gender'] = 'male'
d['dob'] = '1999-02-01'

d['dob'] = '1989-01-01'
d.pop('dob')

d # {'name': 'jason', 'age': 20, 'gender': 'male'}

s = {1,2,3}
s.add(4)
s # {1,2,3,4}
s.remove(4)
s # {1,2,3}

# sort by asc / desc
d = {'b': 1, 'a': 2, 'c': 10}
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0])
d_sorted_by_key # [('a', 2), ('b', 1), ('c', 10)]

d_sorted_by_value = sorted(d.items(), key=lambda x: x[1])
d_sorted_by_value # [('b', 1), ('a', 2), ('c', 10

# sort set
s = {3, 4, 2, 1}
sorted(s) # [1, 2, 3, 4]




