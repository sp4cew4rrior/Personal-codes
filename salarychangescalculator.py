#This program calculates increase or decrease in salary's. You just need to inform the base salary, and it changes in %.
#The lines 3 to 6 get the information about the salary, and it changes.
bes = float(input('Please inform the employee base salary in USD: '))
readjustment = int(input('Now, please insert the employee salary adjustment in %:'))
readjustmenti = bes + (bes * readjustment / 100)
readjustmentd = bes - (bes * readjustment / 100)
#Lines 8 to 13 asks if you want to increase or decrease the salary, that shows you de % of the changes and the new salary.
print ('Do you wanna increase or decrease the employee salary? '  )
answer = input('If is increase type i, if is decrease type d. ')
if answer == 'i':
    print ('The employee have received an increase of {}% on it salary. Now his salary is ${:.2f}.'.format(readjustment, readjustmenti))
else:
    print ('The employee have received an decrease of {}% on it salary. Now his salary is ${:.2f}.'.format(readjustment, readjustmentd))