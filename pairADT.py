def cons(arg1, arg2):
    return (arg1, arg2)

def is_pair(pair):
    return (type(pair) is tuple) and (len(pair) == 2)

def car(pair):
    return pair[0]

def cdr(pair):
    return pair[1]

def set_car(pair, val):
    cdr_val = cdr(pair)
    return cons(val, cdr_val)

def set_cdr(pair, val):
    car_val = car(pair)
    return cons(car_val, val)