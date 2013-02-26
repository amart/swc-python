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

