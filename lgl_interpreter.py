import sys
import json
import argparse
import random
import logging
from datetime import datetime

# Multiplication, Division, and Power operations
def do_multiplizieren(envs, args):
    assert len(args) == 2
    return do(envs, args[0]) * do(envs, args[1])

# Division
#divide #but not by ZERO
def do_dividieren(envs, args):
    assert len(args) == 2
    assert do(envs, args[1]) != 0, "Cannot divide by zero!"
    return do(envs, args[0]) / do(envs, args[1])


# Power
def do_hochstellen(envs, args):
    assert len(args) == 2
    return int(do(envs, args[0]))**int(do(envs, args[1]))


# Print statements
def do_drucken(envs, args):
    for i in args:
        print(do(envs, i )) #TODO we can also just force it to only print one, here we print all args on new lines

# less than bool 
def do_kleiner_als(envs, args):
    assert len(args)==2, f"Need exactly 2 args to compare, not {len(args)}"
    left = do(envs, args[0])
    right = do(envs, args[1])
    return left < right

#3. While loops
def do_waehrend(envs, args):
    assert len(args) == 2
    while_statement = args[0]
    body = args[1]
    while do(envs, while_statement): #TODO do we want to implement "<" or some other boolean evals?
        do(envs, body)

#4. Arrays:
# Creating a new array of fixed size 
# accept input ["liste", 2,3,4,5] == list of lenght 4
# also accepts an empty list ["liste"] #no comma for empty list!
def do_liste(envs,args):
    return [do(envs,arg) for arg in args]

# Getting the value at position i of an array
# ["abrufen_listenObj", "listenName", i] where I starts from 0 cause python
def do_abrufen_listenObj(envs,args):
    assert len(args) == 2, "Need a list name and an index"
    assert isinstance(do(envs,args[1]), int), "Need an interger index"
    list_name = [args[0]]
    i_list = do_abrufen(envs, list_name)
    return i_list[args[1]]

# Setting the value at position i of an array to a new value
def do_setzen_listenObj(envs,args):
    assert len(args) == 3, "Need a list name and an index and value"
    assert isinstance(do(envs,args[1]), int), "Need an interger index"
    list_name, list_id, value  = args 
    temp_list = do_abrufen(envs,[list_name])
    temp_list[list_id] = do(envs, value) # This also changes the origial list value in the env, aliases for the win
    return value


#5. Dictionaries:
# Creating a new dictionary ["woerterbuch", ["liste", 2,3,4,5] , ["liste", 20,30,40,50]]
def do_woerterbuch(envs,args): 
    keys = do(envs, args[0])
    values = do(envs, args[1])
    assert len(keys)==len(values), "Keys and values should have the same length"
    return {do(envs,keys[i]):do(envs,values[i]) for i in range(len(keys))}

# Getting the value of a key
def do_abrufen_schluessel(envs,args):
    assert len(args) == 2, "Need a dictionary name and an key"
    dict_name = [args[0]]
    i_dict = do_abrufen(envs, dict_name)
    return i_dict[args[1]]

# Setting the value of a key to a new value
def do_setzen_schluessel_wert(envs,args):
    assert len(args) == 3, "Need a dict name and a key and a new value"
    dict_name, key, value = args 
    temp_dict = do_abrufen(envs,[dict_name])
    temp_dict[key] = do(envs, value) # This also changes the origial dict value in the env, aliases for the win
    return value

# Merging two dictionaries (i.e, implement the | operator of Python)
def do_woerterbuch_vereinigung(envs, args):
    dict0 = do(envs, args[0])
    dict1 = do(envs, args[1])
    return dict0 | dict1


# Supporting class functionalities
def do_klasse(envs, args):
    assert len(args) == 1
    do(envs, args[0])


def do_klassen_instanz(envs, args):
    assert len(args) == 1
    do(envs, args[0])


# Use this call function instead of the generic call function for inheritance related operations
def do_klassen_aufrufen(envs, args):
    assert len(args) >= 2
    thing = args[0]
    assert isinstance(args[1], str)
    method_name = args[1]
    arguments = args[2:]

    values = [do(envs, arg) for arg in arguments]

    func = do_klassen_finden(do(envs, thing)['_class'], method_name)
    assert isinstance(func, list)
    assert func[0] == "funktion"

    func_params = func[1]
    assert len(func_params) == len(values)
    local_frame = dict(zip(func_params, values))
    envs.append(local_frame)

    body = func[2]
    result = do(envs, body)
    envs.pop()

    return result


# Support function to look for parent object recursively
def do_klassen_finden(thing_class, name):
    assert isinstance(thing_class, dict)
    assert isinstance(name, str)
    if name in thing_class:
        return thing_class[name]
    if thing_class['_parent'] == 'None':
        raise NotImplementedError(f" {name} is not implemented")
    return do_klassen_finden(thing_class['_parent'], name)


######## BELOW IS FROM THE LECTURE ########
def do_funktion(envs, args):
    assert len(args) == 2
    params = args[0]
    body = args[1]
    return ["funktion", params, body]


# function call
def do_aufrufen(envs, args):
    assert len(args) >= 1
    name = args[0]
    arguments = args[1:]
    # eager evaluation
    values = [do(envs, arg) for arg in arguments]

    func = envs_get(envs, name)
    assert isinstance(func, list)
    assert func[0] == "funktion"
    func_params = func[1]
    assert len(func_params) == len(values)

    local_frame = dict(zip(func_params, values))
    envs.append(local_frame)
    body = func[2]
    result = do(envs, body)
    envs.pop()

    return result


def envs_get(envs, name):
    assert isinstance(name, str)
    for e in reversed(envs):
        if name in e:
            return e[name]
        # for value in e.values():
        #     if isinstance(value, dict):
        #         result = envs_get([value], name)
        #         if result is not None:
        #             return result
    # python like version
    # if name in envs[-1]:
    #    return e[name]
    # if name in envs[0]:
    #    return e[name]
    assert False, f"Unknown variable name {name}"


def envs_set(envs, name, value):
    assert isinstance(name,str)
    envs.append({name: value})


def do_setzen(envs, args):
    assert len(args) == 2
    assert isinstance(args[0], str)
    var_name = args[0]
    value = do(envs, args[1])
    envs_set(envs, var_name, value)
    return value


def do_abrufen(envs, args):
    assert len(args) == 1
    return envs_get(envs, args[0])


def do_addieren(envs, args):
    assert len(args) == 2
    left = do(envs, args[0])
    right = do(envs, args[1])
    return left + right


def do_absolutwert(envs, args):
    assert len(args) == 1
    value = do(envs, args[0])
    return abs(value)


def do_subtrahieren(envs, args):
    assert len(args) == 2
    left = do(envs, args[0])
    right = do(envs, args[1])
    return left - right


def do_abfolge(envs, args):
    assert len(args) > 0
    for operation in args:
        result = do(envs, operation)
    return result


OPERATIONS = {
    func_name.replace("do_", ""): func_body
    for (func_name, func_body) in globals().items()
    if func_name.startswith("do_")
}


def do(envs, expr):
    if not isinstance(expr, list):
        return expr
   
    assert isinstance(expr, list)
    assert expr[0] in OPERATIONS, f"Unknown operation {expr[0]}"
    try:
        envs_get(envs, 'trace')
        func = trace_decorator(OPERATIONS[expr[0]]) 
    except AssertionError:
        func = OPERATIONS[expr[0]]
    return func(envs, expr[1:])


# Fixed the id so that a 6 digit number is generated
def trace_decorator(original_func):
    def wrapper(*args, **kwargs):
        rand = str(random.random())
        # rand = random.random()
        id = int(float(rand) * 10000000) if rand[2] == '0' else int(float(rand) * 1000000)
        # id = round(rand * 1000000)

        logging.info(f'{id}, {original_func.__name__}, start, {datetime.now()}')
        result = original_func(*args, **kwargs)
        logging.info(f'{id}, {original_func.__name__}, stop, {datetime.now()}')
        return result
    return wrapper


def get_args():
    parser = argparse.ArgumentParser('log the result of your interpreter')
    parser.add_argument('operations', help='pass in your example operations')
    parser.add_argument('--trace', default=None, help='log the result of your interpreter')

    args = parser.parse_args()
    return args


# One modification for the envs, not necessary to create [{}], just append dict when do_setzen
def main(args):
    assert len(sys.argv) >= 2, "Usage: funcs-demo.py filename.gsc"
    with open(sys.argv[1], "r") as source_file:
        program = json.load(source_file)
    assert isinstance(program, list)
    envs = []

    if args.trace:
        FORMAT = '%(message)s'
        conf_log = logging.basicConfig(filename=args.trace, level=logging.INFO, format=FORMAT)
        logging.info("id,function_name,event,timestamp")
        envs.append({'trace': conf_log})

    do(envs, program)



if __name__ == "__main__":
    args = get_args()
    main(args)


