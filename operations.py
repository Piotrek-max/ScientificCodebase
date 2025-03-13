import math as m
def T_Y(a,b):
    if a>0 and b>0:
        return pow(b,a)
    elif b==0:
        return 0
    else:
        return 1

def F_MP(a,b):
    return a*min(a,b)
def geometric_mean(a,b):
    return m.sqrt(a*b)
def T_M(x, y):
    return min(x, y)


def T_P(x, y):
    return x * y


def T_L(x, y):
    return max(x + y - 1, 0)

def T_F(x, y):
    if x + y > 1:
        return min(x, y)
    else:
        return 0

def T_E(x, y):
    return (x * y)/(2 - x - y + x * y)

operation_functions = {'T_Y':T_Y,
  'F_MP':F_MP,
  'geometric_mean':geometric_mean,
  'T_M':T_M,
  'T_P':T_P,
  'T_L':T_L,
  'T_F':T_F,
  'T_E':T_E,
}

def operation_function(name: str, a,b):
    if name not in operation_functions:
        raise NameError(f'No {name} in operations.py - doublecheck function name or restart kernel to load file changes.')
    else:
        return operation_functions[name](a,b)
