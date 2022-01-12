#This program calculates increase or decrease in salaryes. You just need to inform the base salarye and it change in %.
#The lines 3 to 6 recibe the informations about the salary and it changes.
bes = float(input('Please inform the imployee base salary in USD: '))
r = int(input('Now, please insert the employee salary adjustment in %:'))
ri = bes + (bes * r / 100)
rd = bes - (bes * r / 100)
#Lines 8 to 13 asks if you wanna increase or decrease the salary, that shows you de % of the changes and the new salary.
print ('Do you wanna increase or decrease the employee salary? '  )
answer = input('If is increase type i, if is decrease type d. ')
if answer == 'i':
    print ('The employee have recived an increase of {}% on it salarye. Now his salarye is ${:.2f}.'.format(r, ri))
else:
    print ('The employee have recived an decrease of {}% on it salarye. Now his salarye is ${:.2f}.'.format(r, rd))