#This program will calculate the amount of discound of a product.
#The lines 3 to 5 Recive the base value of the product (bv) and it discount (d).
#After this, it subtract the value of the discount on the base value and generates a new product price. (nv).
bv = float(input('Please insert the product value in R$: '))
d = int(input('Please insert the discont amouth listed on the product tag: '))
nv = bv - (bv * d / 100)
#Than it show the new product value.
print('The product value with {}% off is R${:.2f}.'.format(d, nv))
