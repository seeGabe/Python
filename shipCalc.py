#Gabriel Colon. problem 10
def shipCost(Weight):
	sngServ = 15.0
	sngSurc1 = 5.0
	sngSurc2 = 10
	if Weight <= 100:
		if Weight > 70:
			canShip = (sngServ + sngSurc2 + ((Weight - 2)* sngSurc1))
		elif Weight > 2:
			canShip = (sngServ + ((Weight - 2)* sngSurc1))
		else:
			canShip = (sngServ)
	else:
		canShip = -1	
	return canShip

# main program	
sngWeight = float(input('please enter weight of package in lbs '))
thisPackage = shipCost(sngWeight)
if thisPackage > 0:
        print('Shipping Costs will be: $'+str(thisPackage))
else:
        print('Sorry, not able to ship this package.')
input('press enter to continue')
