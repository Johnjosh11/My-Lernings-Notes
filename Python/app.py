# Comparing strin, list, dictionaries, tuples
#text = 'hello there'
#print(text)
#print(len(text))
#text = ['hello', 'there']
#print(text)
#print(len(text))
#text = {'key1': 'hello', 'key2': 'there'}
#print(text)
#print(len(text))
#text = ('hello', 'there')
#print(text)
#print(len(text))
#text = ([12,13,14])
#print(text)

#text = [12,13,14]
#print(text[0])



#print('Hello') ## This is just a print statement

#print('  ----0')
#print('  ||||')
#print('*' * 10) #This a math expression

#price = 10 #Assigning a variable
#print(price) 

#name = input('what is your name ') # Taking the input from the user and printing the value
#favc = input('What clour do you like ')
#print(name + ' likes ' + favc)

#DOB = input('what is your DOB ')
#age = 2019 - int(DOB) # value passed through the input is treated as string
#rint('Your age is ' + str(age)) # when you concatinate then the out put should be a string

#name = 'jennifer'  [start:stop:step]
# index 01234567
#print(name[1]) #Output is 'e'
#print(name[0:3]) #Ouput is 'jen' this will print from 0 to 2 index but not 3rd value
#print(name[0:7:2]) #Ouput is 'jnie' The last digit indicates the step size (meaning jump two times)
#print (name[0:-1]) #Ouput is 'jennife' reverse indexing

######### f formating ###########
#first = 'John'
#last = 'Wesley'
#mess = f'{first} [[{last}]] is a player' # f formated string
#message = f'{first.upper()}' # use case of f formated string
#print(mess)
#print(message)

######### Boolian (True or False) ###########
#context = 'His name is wesley'
#print(len(context)) # This is for knowing how many carectors -note:spaces are counted
#print(context.replace('His','Her')) # For replacing
#print(context.find('w')) # This will find the index value -note first occurence
#print('name ' in context) # Returns Boolian value as 'true' as we can find that string in the passed variable. 

######### Arithmatic operators ###########
#print(10 + 5)  # Addition
#print(10 - 5)  # Sup
#print(10 * 5)  # Mul
#print(10 / 5)  # Div may result in floating value
#print(10 // 5) # Div will make the nearest round off
#print(10 % 5)  # Mod which returns the result
#print(10 ** 5) # Power or times of 

#x = 10
#x += 15 # simmiler to (x = x + 10) # adding the value to its own and stores the value
#x -= 5  # simmiler to (x = x - 5)
#print (x)


#priority
#  ()
#  **
#  multiplication or division
#  addition or supraction
#
## Guess the output
#x = (10 + 5) * 8 -3 
#print (x)
             ######### import ########### 

#import math # This math is called modules and we can tons of modules to import and work with. 
#print(math.ceil(2.9))
#print(math.floor(2.9))

# To explore (https://docs.python.org/3/library/math.html)

######### If Statement ########### 

#is_hot = True # Boolian varialbes are preset
#is_cold = False
#
#if is_cold:  # Checks for this condition
#    print('Its winter please were your jacket')
#elif is_hot: # If the above condition is Flase then checks for this condition
#    print('Its summer, drink pleanty of water')
#else: # If the both above values are Flase then executes this print 
#    print('Its a lovely day')
#print('Enjoy your day')  # This print is executed for all the conditons as it is in line with the conditions.

#price = 10000
#has_good_credit = False
#
#if has_good_credit:
#    down_payment = 0.1 * price
#else:
#    down_payment = 0.2 * price
#print(f"Down Payment: Rs = {down_payment}")

######### Logical Operators ########### 
#and 
#or
#not

######### comparision Operators ########### 
#>
#>=
#<
#<=
#==
#!=

#weight = int(input('Weight: '))
#unit = input('(L)bs or (K)g: ')
#if unit.upper() == "L":
#    converted = weight * 0.45
#    print(f"Your are {converted} kilos")
#else:
#    converted = weight / 0.45
#    print(f"Your are {converted} Pounds")

######### while loop  ###########

# While loop is used to itterate through a block of code#

#i = 1 # This is the initial value
#while i <= 5: # This is the while if condition
#    print('*' * i) # if it is less that 5 then print
#    i += 1 # i value is incresed when the while condition is true
#print("Done") # This is executed when the intepritor exits out of the while loop

                   ######### while loop  guess game ###########
#secret_number = 9
#number_guess = 0
#while number_guess < 3:
#    Guess = int(input('What is your guess: '))
#    number_guess += 1 
#    if Guess == secret_number:
#        print('You won')
#        break
#    else:
#        print ('Try again')
#else:
#    print('You have failed')

                    ######### while loop  Car game ###########
#help = '''Stop  -> Stop the car
#start -> Start the Car
#Quit  -> Quit the Game '''
#user_input = ""
#started = False
#while True:
#    user_input = input('Hey Jack > ').upper()
#    if user_input == 'HELP':
#        print(help)
#    elif user_input == 'START':
#        if started:
#            print ('Its already started')
#        else:
#            started = True
#            print ('Car has Started')            
#    elif user_input == 'STOP':
#        if not started:
#            print('Its already stopped')
#        else:
#            started = False
#            print('Car has Stopped')            
#    elif user_input == 'QUIT':
#        print('Thanks for playing the game')
#        break
#    else: 
#        print ('I dont understand you')

######### for loop  ###########

# This is used to itterate through a charecter in a string or item in a list

#exp:1 
#for item in 'Python':
#    print(item)
#
#for item in ['john', 'wesley']:
#    print(item)
#
#for item in ['john', 'wesley']:
#    print(item[0])
#
#for item in [1,2,3,4,5]:
#    print(item)
#
#for item in range(5,10,2):
#    print(item)

# exp:
#price = [10, 20, 30]
#total = 0
#for prices in price:
#    total += prices
#print (f"Total price in rs is: {total}")

######### Lists  ###########

#item = ['john', 'wesley']
#print (item[0])
#
#item = ['john', 'wesley']
#print (item[1][0])

# exp: Find the largest number in the list
#List = [11,2,3,4,5,6,10]
#largest = List[0]
#for item in List:
#    if item > largest:
#        largest = item
#print (largest)

#exp: Remove duplicates in a list
#List = [1,2,2,3,4,5,5,6]
#final_list = []
#for item in List:
#    if item not in final_list:
#        final_list.append(item)
#print(final_list) 

######### Tuples  ###########
# This is used when you dont want to modify the list
# Below example will get error as we are trying to re-assign inex '0' value 
#number = (1,2,3,4,5)
#number[0] = 10
#print(number[0])


######### unpacking  ###########
#number = [1,2,3]
#x, y, z = number
#print(z)

######### Dictionaries  ###########
# value assosiated with key pair
#customer = {'Name': 'John', 'age': 30, 'is_alive': True}
#print(customer['Name'])
#print(customer.get('Name'))
#print(customer.get('pame'))
#print(customer.get('pame', 'emap'))
#print(customer)
#customer['new_val'] = 'test_value'
#print(customer)

#exp: user input is number and the output is word
#user_input = input('enter phone no: ')
#key_value = {
#    '1' : 'one',
#    '2' : 'two',
#    '3' : 'three'
#}
#output_map = ""
#for num in user_input:
#    output_map += key_value.get(num, "!" ) + " "
#print (output_map)

                         ######### split ###########
#message = input(">")
#words = message.split(' ')
#vale = {
#    "1":":)",
#    "2":":(",
#}
#output = ""
#for ch in words:
#    output += vale.get(ch, ch) + " "
#print(output)

######### Functions  ###########
# This is used to call or reuse the block of code in our program, any where or anytime within the program 
#exp:
#def func(name):
#    print(f'Hi {name}')
#    print('welcome on board')
#
#func('sita')
#func('siri')

#exp:
#def func(first_name, last_name):
#    print(f'Hi {first_name} {last_name}')
#    print('welcome on board')
#
#func('sita', 'mukun')
#func('siri', 'tela')

#exp:
#def func(message):
#
#    words = message.split(' ')
#    vale = {
#        "1":":)",
#        "2":":(",
#    }
#    output = ""
#    for ch in words:
#        output += vale.get(ch, ch) + " "
#    return output
#
#
#message = input(">")
#print(func(message))

######### Exceptions  ###########
# This is to avoid user input errors

#exp:
#try:
#    age = int(input('>'))
#    loan = 2000
#    risk = loan / age
#    print (age)
#except ZeroDivisionError:
#    print('Age canot be zero')
#except ValueError:
#    print('Should enter Numerical Value')


######### Classes  ###########
#

#class Point():
#    def funcname1(self):
#        print('function1')
#
#    def funcname2(self):
#        print('function2')
#
#point = Point()
#point.funcname1()

#class Point():
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#
#    def funcname1(self):
#        print('function1')
#
#    def funcname2(self):
#        print('function2')
#
#point = Point(10,20)
#print(point.x)
                    ######### class Constructors  ###########
#exp: This is used when we want to pass arguments
#class Person:
#    def __init__(self, name):
#        self.name = name
#
#    def talk(self):
#        print(f"Hi, welcome {self.name} ")
#
#
#john = Person("John Smith")
#john.talk()
#
#bob = Person("prisly")
#bob.talk()
                     ######### class inheritance  ###########

#exp: This is used when we want to call some other class method in new class method
#class Person:
#    def __init__(self, name):
#        self.name = name
#
#    def talk(self):
#        print(f"Hi, welcome {self.name} ")
#
#class Cat(Person):
#    def behaviour(self):
#        print("This is your First Day")
#
#john = Cat('Jessy')
#john.talk()
#john.behaviour()

#########  Modules  ###########

#exp: import from predifined modules
#import converters
#print(converters.kgs_2_lbs(70))

#exp: import module with specific methods
 
#from converters import kgs_2_lbs
#print(kgs_2_lbs(50))

#exp:   
#from utils import max_Num
#
#number = [11,2,3,4,5,6,10]
#max = max_Num(number)
#print(max)

##########  Packages  ###########
# Here we have to create a folder for the package and create a file '__init__.py'
#import ecommerce.calc
#ecommerce.calc.calc_shippig()
#       or
#from ecommerce.calc import calc_shippig
#calc_shippig()

 
#exp:               ##########  Packages random  ###########
#import random
#
#for i in range(3):
#    print(random.randint(10, 20))
#
#exp:
#members = ['qw', 'er', 'ty']
#leader = random.choice(members)
#print(leader)