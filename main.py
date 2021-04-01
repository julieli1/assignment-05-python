d = input("what is the diameter of your circle?  ")
area = 0
circumference = 0
pi = 3.141592


def is_digit(d):
   try:
    int(d)
    return True
   except ValueError:
    return False


def validate_input(d):
  while (True):
     if is_digit(d) == False:
       d = input("please enter a numerical value")
    elif (int(d) < 0):
       d = input("please enter a value greater than 0")
    else:
       return int(d)


d = validate_input(d)

area = pi * ((d / 2) * (d / 2))
circumference = pi * d
print('the area of your circle is ', area)
print('the circumference of your cirlce is', circumference)
print('thank you for using this program')
