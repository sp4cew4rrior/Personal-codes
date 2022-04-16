productbasevalue = float(input('Please insert the product value: $'))
print('''
PAYMENT METHODS AVALIABLE:
1 :Cash or Check (10% OFF!)
2 :Debit (5% OFF!)
3 :Two installments on Credit card
4 :Three or more installments on credit card (20% interest)
''')
##value changes
percentage = productbasevalue / 100
discount10 = 10 * percentage
discount5 = 5 * percentage
interest20 = 20 * percentage
payment = input('Please chose one of the avaliable payment methods using the numbers on the list: ')
if payment == '1':
    productvalue10 = productbasevalue - discount10
    print('The product value went from {:.2f} to {:.2f}.'.format(productbasevalue, productvalue10))
    print('Total to be paid: ${:.2f}'.format(productvalue10))
elif payment == '2':
    productvalue5 = productbasevalue - discount5
    print('The product value went from {:.2f} to {:.2f}'.format(productbasevalue, productvalue5 ))
    print('Total to be paid: ${:.2f}'.format(productvalue5))
elif payment == '3':
    print('Total to be paid: ${:.2f}'.format(productbasevalue))
elif payment == '4':
    productvalueinterest = productbasevalue + interest20 * 3
    print('Due to intersts of 20%, the price went from ${:.2f} to ${:.2f}.'.format(productbasevalue, productvalueinterest))
    print('Total to be paid: ${:.2f}'.format(productvalueinterest))
else:
    print('Invalid payment option, ending operation.')