# Gabriel Colon, problem 11
#make a function called MaxNum to compute and return max val 
def maxNum(list):
        maxValue = list[0]
        for x in range(len(list)):
                if maxValue < list[x]:
                        maxValue = list[x]
        return maxValue
# accumulate numbers into a list
List = [] #initialize empty list
user = (input('enter a number '))
while user != "":
	nums = float(user)
	List.append(nums)
	user = (input('enter another number '))
print('Maximum Value: '+str(maxNum(List)))
# Delay closing the prompt
input()