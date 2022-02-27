colors = {'clear':'\033[m',
          'green':'\033[32m',
          'purple':'\033[35m',
          'blue':'\033[34m'}
number = int(input('{}Please type an number: {}'.format(colors['green'],colors['clear'])))
print('''{}Choose one of the following bases to conversion:
 [1] Convert to BINARY
 [2] Convert to OCTAL
 [3] Convert to EXADECIMAL{}'''.format(colors['blue'],colors['clear']))
option = int(input('{}Your option: {}'.format(colors['blue'],colors['clear'])))
if option == 1:
    print('{} converted to BINARY is {}'.format(number,bin(number)))
elif option == 2:
    print('{} converted to OCTAL is {}'.format(number, oct(number)))
elif option == 3:
    print('{} converted to EXADEMAL is {}'.format(number,hex(number)))
else:
    print('Invalid option.')