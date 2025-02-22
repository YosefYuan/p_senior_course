try:
    s = input('please enter two numnbers separeted by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())

except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
# except Exception as err:
#     print('Other Error: {}'.format(err))
except:
    print('Other Error')

print('continue')
