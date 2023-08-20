
from regex_processing import simplex_response, variables

#nbr_split = len(v)


def check_constraints(c_s,v, resp):
    for vari, resp in zip(v, resp):
        c_s = c_s.replace(vari, str(resp))
    return c_s

def is_constraint_true(c_s, target, resp):
    v = variables(target)

    f = final_response(v, resp)
    check_c = check_constraints(c_s, v, f)
    tab_split = check_c.split("\n")
    check = True
    for c in tab_split:
        if not eval(c):
            check = False
            break
    
    return check

def final_response(v, s): 
    response_tab = []
    for i in range(len(v)):
        response_tab.append(s[i][0])
    return response_tab

def solution_print(phr, resp):
    v = variables(phr)
    f = final_response(v, resp)
    for variable, resp in zip(v, f):
        phr = phr.replace(variable, str(resp))
    
    sol = " > ",phr,"= ",eval(phr)
    return sol

