# Gabriel Colon, problem 6

#using a loop to keep the solution from problem 1 running

#	declare variables
choice =  3 #dummy value
def ctof(temp):
    far = (temp * 1.8) + 32
    return far

def ftoc(temp):
      cel = (temp-32) * 0.555
      return cel
#		start loop and stop only on a 0 value
while choice != 0:
      print('============ CONVERT TEMPERATURE TO:_ ============')
      choice =  int(input('1. Farenheight OR 2. Celcius?  0. To End Script '))
      if choice == 0:
            print('Thank you')
      elif choice == 1:
            fltTemp = float(input('Enter temperature '))
            ans = ctof(fltTemp)
            print('...is equal to ' + str(ans) + ' degrees Farenheight\n')
      elif choice == 2:
            fltTemp = float(input('Enter temperature '))
            ans = ftoc(fltTemp)
            print('...is equal to ' + str(ans) + ' degrees Celcius\n')
      else:
            print('\nINVALID -- valid input: 0,1,2')
