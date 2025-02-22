try:
    s = input('please enter two numnbers separeted by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())

except (ValueError, IndexError) as err:
    print('Error: {}'.format(err))

print('continue')


