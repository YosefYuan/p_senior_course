# String
name = 'jason'
city = 'Beijing'
text = f'hello, {name}! you are in {city} right?'
print(text)

s1 = 'hello'
s2 = "hello"
s3 = '''hello'''
s1 == s2 == s3


def calculate_similarity(item1, item2):
    """
    Calculate similarity between two items
    Args:
        item1: 1st item
        item2: 2nd item
    Returns:
        similarity: similarity between two items    
    """

s = 'a\nb\tc'
print(s)
len(s)


name = 'jason'
name[0]
name[1:3]

for char in name:
    print(char)


s = 'hello'
s[0] = 'H' # Error

s = 'H' + s[1:]
s = s.replace('h', 'H')