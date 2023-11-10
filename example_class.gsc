######## SHAPE ########
def shape_density(instance, weight):
    area = call(instance, "area")
    return weight / area

Shape = {
    'density': shape_density, 
    '_classname': 'Shape',
    '_parent': None
}

######## SQUARE ########
def square_area(instance):
    return instance["side"] ** 2

Square = {
    'area': square_area,  
    '_classname': 'Square',
    '_parent': Shape
}

def square_new(name, side):
    square_obj = {
        'name': name,
        'side': side,
        '_class': Square
    }
    return square_obj

######## CIRCLE ########
def circle_area(instance):
    return instance['radius'] ** 2 * 3.14

Circle = {
    'area': circle_area,  
    '_classname': 'Circle',
    '_parent': Shape
}

def circle_new(name, radius):
    circle_obj = {
        'name': name,
        'radius': radius,
        '_class': Circle
    }
    return circle_obj

######## Implementation ########
def call(instance, method_name, *args):
    method = find(instance["_class"], method_name)
    return method(instance, *args)

def find(cls, method_name):
    if method_name in cls:
        return cls[method_name]
    else:
        if cls['_parent'] is None:
            raise NotImplementedError(f"{method_name} is not implemented in {cls['_classname']}")
        else:
            return find(cls["_parent"], method_name)

########### EXECUTION #############
sq = square_new('sq', 3)
ci = circle_new('ci', 2)

sum_density = call(sq, "density", 5) + call(ci, "density", 5)

print("Sum of densities:", sum_density)
