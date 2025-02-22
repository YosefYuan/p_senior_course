import sys

try:
    f = open('file.txt', 'r')

except OSError as err:
    print('OS error: {}'.format(err))
except:
    print('Unexpected error:', sys.exc_info()[0])
finally:
    f.close()