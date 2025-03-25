"""
Pliki powstały przy pracy Matusiewicz, Z., & Mroczek, T. (2025). Attribute reduction method based on fuzzy relational equations and inequalities. International Journal of Approximate Reasoning, 178, 109355.
"""
def i_T_Y(a,b):
    if a*b>0:
        return pow(b,1/b)
    else:
        return 0
def i_F_MP(a,b):
    if a*a<=b:
        return 1
    else:
        return b/a

def i_geometric_mean(a,b):
    b2=b*b
    if a>b2:
        return b2/a
    else:
        return 1

def Godela(x, y):
    if x <= y:
        return 1
    else:
        return y


def Fodora(x, y):
    if x <= y:
        return 1
    else:
        return max(1 - x, y)


def Goguena(x, y):
    return min(y / x, 1)


def Kleene_Dienesa(x, y):
    return max(1 - x, y)


def Lukasiewicza(x, y):
    return min(1 - x + y, 1)


def Reichenbacha(x, y):
    return 1 - x + x * y


def Reschera(x, y):
    if x <= y:
        return 1
    else:
        return 0


def Webera(x, y):
    if x < 0:
        return 1
    elif x == 0:
        return 0


def Yagera(x, y):
    if x == 0 and y == 0:
        return 1
    elif x > 0 or y > 0:
        return y ** x


def Einsteina(x, y):
    if x <= y:
        return 1
    else:
        return (2 * y - x * y)/(x + y - x * y)

implication_functions = {'Einsteina':Einsteina,
  'Fodora':Fodora,
  'Godela':Godela,
  'Goguena':Goguena,
  'Kleene_Dienesa':Kleene_Dienesa,
  'Lukasiewicza':Lukasiewicza,
  'Reichenbacha':Reichenbacha,
  'Reschera':Reschera,
  'Webera':Webera,
  'Yagera':Yagera,
  'i_F_MP':i_F_MP,
  'i_T_Y':i_T_Y,
  'i_geometric_mean':i_geometric_mean,}

def implication_function(name: str, a,b):
    if name not in implication_functions:
        raise NameError(f'No {name} in implikacje.py - doublecheck function name or restart kernel to load file changes.')
    else:
        return implication_functions[name](a,b)
