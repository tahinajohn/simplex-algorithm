
from regex_processing import simplex_response, variables
from itertools import zip_longest
#nbr_split = len(v)


def check_constraints(c_s,v, resp):
    if len(v) > len(resp):
        for vari, resp in list(zip_longest(v, resp, fillvalue=0)):
            c_s = c_s.replace(vari, str(resp))
    else:
        for vari, resp in zip(v, resp):
            c_s = c_s.replace(vari, str(resp))
    return c_s

def is_constraint_true(c_s, target, resp):
    v = variables(target)

    f = final_response(v, resp)
    check_c = check_constraints(c_s, v, f)
    tab_split = check_c.split("\n")
    print("tab_split = ", tab_split)
    check = True
    for c in tab_split:
        if not eval(c):
            check = False
            break
    
    return check

def final_response(v, s):
    if len(v) > len(s):
        l = len(s)
    else:
        l = len(v) 
    response_tab = []
    for i in range(l):
        response_tab.append(s[i][0])
    return response_tab

def solution_print(phr, resp):
    v = variables(phr)
    f = final_response(v, resp)
    if len(v) > len(resp):
        for variable, resp in list(zip_longest(v, f, fillvalue=0)):
            phr = phr.replace(variable, str(round(resp,2)))
    else:
        for variable, resp in zip(v, f):
            phr = phr.replace(variable, str(round(resp,2)))
    
    #sol = phr,"= ",eval(phr)
    sol = f"Solution : z : {phr} = {round(eval(phr), 2)}"

    tab_rep = []
    #for variable, resp in zip(v, f):
    for i in range(len(variable)):
        new_elem = f"{v[i]} = {round(f[i],2)}"
        tab_rep.append(new_elem)
        #tab_rep = str(variable, " = ", resp, "\n")
    
    tab_response = "\n".join([f"{element}" for element in tab_rep])

    return tab_response, sol

