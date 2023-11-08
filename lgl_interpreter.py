import sys
import json

#TODO
#Multiplication, Division, and Power operations
def do_multiplizieren(envs, args):
    assert len(args)==2
    return do(envs,args[0])*do(envs,args[1])

def do_dividieren(envs, args):
    assert len(args)==2
    assert do(envs,args[1]) != 0, "Cannot divide by zero!"
    return do(envs,args[0]) / do(envs,args[1])

def do_hochstellen(envs, args):
    assert len(args)==2
    return do(envs,args[0])**do(envs,args[1])


#2. Print statements
def do_drucken(envs, args):
    for i in args:
        print( do(envs,i ) ) #TODO we can also just force it to only print one, here we print all args on new lines

#  ["waehrend", [["abrufen", "a"] < 5 ], ["abfolge", ["drucken", ["abrufen", "a"]], ["setzen", "a", ["addieren", ["abrufen", "a"], 1 ]]   ]]

#3. While loops
def do_waehrend(envs,args):
    assert len(args) == 2
    while_statement = args[0]
    body = args[1]
    while do(envs, while_statement) < 5: #TODO do we want to implement "<" or some other boolean evals?
        do(envs, body)
    

#4. Arrays:
# Creating a new array of fixed size 
#Fixed size could mean we use the lenght of the args as the lenght of the array, or the first argument has to be the lenght of the array
def do_liste(envs,args):

    pass #TODO

# Getting the value at position i of an array
def do_abrufen_listenObj(envs,args):
    pass #TODO
# Setting the value at position i of an array to a new value
def do_setzen_listenObj(envs,args):
    pass #TODO


#5. Dictionaries:
#• Creating a new dictionary
#• Getting the value of a key
#• Setting the value of a key to a new value
#• Merging two dictionaries (i.e, implement the | operator of Python)
def do_woerterbuch(envs,args): 
    pass #TODO

def do_setzen_schluessel(envs,args):
    pass #TODO


#classe def, obj instantiation
def do_klasse(envs,args):
    pass #TODO


def do_klassen_instanz(envs, args):
    pass #TODO






####### BELOW IS FROM THE LECTURE ##########################

def do_funktion(envs,args):
    assert len(args) == 2
    params = args[0]
    body = args[1]
    return ["funktion",params,body]

def do_aufrufen(envs,args):
    assert len(args) >= 1
    name = args[0]
    arguments = args[1:]
    # eager evaluation
    values = [do(envs,arg) for arg in arguments]

    func = envs_get(envs,name)
    assert isinstance(func,list)
    assert func[0] == "funktion"
    func_params = func[1]
    assert len(func_params) == len(values)

    local_frame = dict(zip(func_params,values))
    envs.append(local_frame)
    body = func[2]
    result = do(envs,body)
    envs.pop()

    return result

def envs_get(envs, name):
    assert isinstance(name,str)
    for e in reversed(envs):
        if name in e:
            return e[name]
        
    # python like version
    # if name in envs[-1]:
    #    return e[name]
    #if name in envs[0]:
    #    return e[name]
    assert False, f"Unknown variable name {name}"

def envs_set(envs,name,value):
    assert isinstance(name,str)
    # for e in reversed(envs):
    #     if name in e:
    #         e[name] = value
    #         return
    envs[-1][name] = value
        


def do_setzen(envs,args):
    assert len(args) == 2
    assert isinstance(args[0],str)
    var_name = args[0]
    value = do(envs,args[1])
    envs_set(envs,var_name, value)
    return value

def do_abrufen(envs,args):
    assert len(args) == 1
    return envs_get(envs,args[0])

def do_addieren(envs,args):
    assert len(args) == 2
    left = do(envs,args[0])
    right = do(envs,args[1])
    return left + right

def do_absolutwert(envs,args):
    assert len(args) == 1
    value = do(envs,args[0])
    return abs(value)

def do_subtrahieren(envs,args):
    assert len(args) == 2
    left = do(envs,args[0])
    right = do(envs,args[1])
    return left - right

def do_abfolge(envs,args):
    assert len(args) > 0
    for operation in args:
        result = do(envs,operation)
    return result


OPERATIONS = {
    func_name.replace("do_",""): func_body
    for (func_name, func_body) in globals().items()
    if func_name.startswith("do_")
}


def do(envs,expr):
    if isinstance(expr,int):
        return expr
   
    assert isinstance(expr,list)
    assert expr[0] in OPERATIONS, f"Unknown operation {expr[0]}"
    func = OPERATIONS[expr[0]]
    return func(envs, expr[1:])


def main():
    assert len(sys.argv) == 2, "Usage: funcs-demo.py filename.gsc"
    with open(sys.argv[1], "r") as source_file:
        program = json.load(source_file)
    assert isinstance(program,list)
    envs = [{}]
    result = do(envs,program)
    print(f"=> {result}")

if __name__ == "__main__":
    main()