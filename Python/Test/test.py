#Questions 1:
    #Write a function that capitalizes the first and fourth letters of a name
    # exp word = oldmecdonald
#def old_macdonald(name):
#    if len(name) > 3:
#        return name[:3].capitalize() + name[3:].capitalize()
#    else:
#        return 'Name is too short!'

#Question 2:
    #Given a sentence, return a sentence with the words reversed
#def rev(name):
#    letter = name.split()
#    word_list = letter[::-1]
#    print (word_list)
#    return ' '.join(word_list)

# Question 3:
    # Given an integer n, return True if n is within 10 of either 100 or 200¶

###almost_there(90) --> True
###almost_there(104) --> True
###almost_there(150) --> False
###almost_there(209) --> True

#def with_in(number):
#    return (abs(100 - number) <=10) or (abs(200 - number) <= 10)

#Question 4:
###Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
###
###has_33([1, 3, 3]) → True
###has_33([1, 3, 1, 3]) → False
###has_33([3, 1, 3]) → False

#comprehension
op=[1,2,3,4,5]
square_op=[]
for i in op:
    square_op.append(i*i)
square_op_even=[_*_ for _ in op if i%2==0]
op={"name": "x", id: 755}
{k:str(v) for k, v in op.items()}

def remove_null(data):
    return {k:remove_null(v) if isinstance(dict, v) else v for k,v in data.items() if v is not None}


