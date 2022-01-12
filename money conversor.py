#Everything is based on the conversion from BRL to USD. Value of the dollar on that operation is 5.57 BRL. (day 11 of january 2022)
#Lines 3 and 4 calculate the amount of money and show to the user.
w = float(input('How much BRL do you wanna convert to USD?  '))
d = w / 5.57
print('With {} BRL you can buy {:.2f} USD.'.format(w, d))

#Askes if the user want to complete the transaction or end without completing it.
print('Want to continue with this transaction?')
answer = input('Type yes or no: ')
if answer == 'yes':
    print('The money was converted and the transaction ended successfully.')
else:
    print('Transaction ended.')