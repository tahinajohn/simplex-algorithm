import re
import numpy as np

from simplex_calculation import simplex_calculation


# v = variables(target_function)
# nbr_split = len(v)


def target_split(target_funct, is_max):
    coeff_regex = r'([+-]?\d+)\s*\*?\s*([a-zA-Z0-9]+)\s*'
    #coeff_regex = r'([+-]?\d+)\*x\d+'
    signe_regex = r'([<>]=?|==)\s*([+-]?\d+)'
    target_catcher = re.findall(coeff_regex, target_funct)
    if is_max:
        target_coeff = [-int(match[0]) for match in target_catcher]
    else:
        target_coeff = [int(match[0]) for match in target_catcher]
        
    print("************TARGET SPLIT*********************")
    print(target_coeff)
    print("*********************************************")
    return target_coeff

def variables(target_funct):
    var_regex = r'([+-]?\d+)\s*\*?\s*([a-zA-Z0-9]+)\s*'
    variable_catcher = re.findall(var_regex, target_funct)
    target_var = [match[1] for match in variable_catcher]
    return target_var

#f = final_response(v, s)
def constraint_split(constraints):
    print("-------------------CONSTRAINTS----------------")
    print(constraints)
    print("----------------------------------------")
    constraint_one_by_one = constraints.split('\n')
    print("-------------------CONSTRAINTS--ONE-BY ONE-------------")
    print(constraint_one_by_one)
    print("----------------------------------------")
    #coeff_regex = r'([+-]?\d+)\s*\*?\s*([a-zA-Z0-9]+)\s*'
    #coeff_regex = r'([+-]?\d+)\*x\d+'
    coeff_regex = r'([+-]?\d+\.*\d*)\*x\d+'
    signe_regex = r'([<>]=?|==)\s*([+-]?\d+)'
    coeff_tab = []
    variables_tab = []
    signe_tab = []
    const_tab = []
    
    for constraint in constraint_one_by_one:
        coeff_catcher = re.findall(coeff_regex, constraint)
        signe_catcher = re.findall(signe_regex, constraint)
        coefficients = [float(match) for match in coeff_catcher]
        print("---------------COEFF---------------------")
        print(coefficients)
        print("-----------------------------------------")
        #variables = [match[1] for match in coeff_catcher]
        coeff_tab.append(coefficients)
        #variables_tab.append(variables)
        signe = [match[0] for match in signe_catcher]
        #signe = signe_catcher[0]

        constant = [int(match[1]) for match in signe_catcher]
        signe_tab.append(signe)
        const_tab.append(constant)

    print("--------------------COEFF TAB-----------------------------")
    print(coeff_tab)
    print("----------------------------------------------------------")
        
    output = {
        "coefficients": coeff_tab,
        "variables": variables_tab,
        "signes": signe_tab,
        "constantes": const_tab
    }
    return output



def sign_number(constraints):
    print("------CONSTRAINT ST FORM IN SIGN NUMBER---------------------")
    constraint = constraint_split(constraints)
    nbr_sign = count_sign(constraint["signes"])
    
    return nbr_sign

def add_zero(M, nbr_col):
    number_rows = M.shape[0]
    zero_array = np.zeros((number_rows, nbr_col))
    new_array = np.hstack((M, zero_array))
    return new_array

def count_sign(tab):
    cpt=0
    for sign in tab:
        if sign[0] == '<=' or sign[0] == '>=' or sign[0] == '>' or sign[0] == '<':
            cpt = cpt + 1
    return cpt

def target_standard_form(target_funct, constraint, is_max):
    print("---------------TARGET STANDARD FROM------------")
    nbr = sign_number(constraint)
    target = target_split(target_funct, is_max)
    target += [0] * nbr
    print("TARGET ", target)
    return target


def constraint_standard_form(constraints):
    print("---------CONSTRAINT STANDARD FORM IN CONSTRAINT ST F---------------")
    constraint = constraint_split(constraints)
    A = np.array(constraint["coefficients"])
    constantes = constraint["constantes"]
    variable = np.unique(constraint["variables"])
    nbr_sign = count_sign(constraint["signes"])
    
    new_arr = add_zero(A, nbr_sign)
    
    for a in enumerate(constraint["signes"]):
        print(a[1][0])
        #i = signe_tab.index(a)
        i = a[0]
        print("i = ",i)
        if a[1][0] == '<' or a[1][0] == '<=':
            new_arr[i][-nbr_sign] = 1
            nbr_sign -= 1
        elif a[1][0] == '>' or a[1][0] == '>=':
            new_arr[i][-nbr_sign] = -1
            nbr_sign -= 1
        print(new_arr[i])

    print("ENter Constraint STANDARD FORM")
    print("Matri standard form = ", new_arr)

    resp = {
        "matrix": new_arr,
        "constantes":constantes
    }
    
    return resp

def split_matrix(target, constraints_M, is_max):
    t = target_standard_form(target, constraints_M, is_max)
    c_M = constraint_standard_form(constraints_M)
    M = c_M["matrix"]
    c_const = c_M["constantes"]

    nbr_split = M.shape[0]
    
    base, hors_base = np.split(M, [nbr_split], axis=1)
    print("Base split mat = ", base)
    print("Hors Base split mat = ", hors_base)

    cb, cn = np.split(t, [nbr_split])  
    
    cb = np.array([cb])
    cn = np.array([cn])

    output = {
        "cb":cb,
        "cn":cn,
        "base":base,
        "hors_base":hors_base,
        "constatntes": c_const
    }
    
    return base, hors_base, cb, cn, c_const

def simplex_response(target, constraints, is_max):
    az = 1
    print("ENTER NEW SIMPLEX z =", is_max)

    b, hb, cb, cn, c = split_matrix(target, constraints, is_max)
    print("ENTER NEW BAse = ", b)
    print("ENTER NEW HorsBAse = ", hb)
    print("ENTER NEW CB = ", cb)
    print("ENTER NEW CN = ", cn)
    print("ENTER NEW CONST = ", c)
    az = az + 1
    return simplex_calculation(b, hb, cb, cn, c,1)
