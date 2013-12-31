# Gabriel Colon, problem 7

# prompt for a number x
# prompt x times for more numbers
#     calculate and print :
#        add the Sum / find max Value / then Average


#     declare variables
iterations = int(input('How many numbers to process? '))
maxValue = 0
addSum = 0
# 			loop start
for i in range(iterations):
    currentValue = int(input('Enter number: '))
    addSum = currentValue + addSum
	# set high value, too
    if maxValue < currentValue:
       maxValue = currentValue
#			display the:
print('____RESULTS\t___')
print('The sum is:\t'+str(addSum))
print('The Average is:\t'+str(addSum / iterations))
print('Highest value:\t'+str(maxValue))
input('')