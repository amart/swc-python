# notes from writing in ipython

def for_each(func,values):
     result = []
     for v in values:
         temp = func(v)
         result.append(temp)

     return(result)

# can call for_each with a function and a list of values (of any type)

def pipeline(what_to_do, starting_value):
     current = starting_value
     for func in what_to_do:
         current = func(current)

     return(current)

def double(x):
    return(2 * x)

def triple(x):
    return(3 * x)

def sub_one(x):
    return(x-1)


pipeline([double,sub_one,triple],5)



def scale(value,factor)
    return(value * factor)

def scale_half(value)
    return(scale(value,0.5))


# want squish(plus,[1,2,3]) is 6
#      squish(times,[1,2,3]) is 6
#      squish(times,[4,5,6]) is 120
#      squish(plus,[1,-1,2,3]) is 5

def plus(x,y):
    return(x+y)

def times(x,y):
    return(x*y)


def squish(func_arg,list_arg):
     result = list_arg[0]
     if len(list_arg) > 1:
         for l in list_arg[1:]:
             result = func_arg(result,l)

     return(result)



