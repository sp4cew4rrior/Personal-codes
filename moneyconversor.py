#Everything is based on the conversion from BRL to USD. On that program you NEED to inform the exchange rate of the money.
#Lines 3 and 4 calculate the amount of money and show to the user.
w = float(input('How much BRL do you wanna convert to USD?  '))
er = float(input('Now, inform the current exchange rate of BRL-USD: '))
d = w / er
print('With {} BRL you can buy {:.2f} USD, with the exchange rate between BRL and USD at {}.'.format(w, d, er))

#Askes if the user want to complete the transaction or end without completing it.
print('Want to continue with this transaction?')
answer = input('Type yes or no: ')
if answer == 'yes':
    print('The money was converted and the transaction ended successfully.')
else:
    print('Transaction ended.')