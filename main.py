from regex_processing import simplex_response
from response_check import is_constraint_true, solution_print


target_equation = "1*x1 +2*x2"
constraints = "-3*x1 +2*x2 <= 2\n-1*x1 +2*x2 <= 4\n1*x1 +1*x2<= 5"

simple_constraint = "x1 >= 0\nx2 >= 0"

is_max = True

resp = simplex_response(target_equation, constraints, is_max)

print("response = ", resp)

if is_constraint_true(simple_constraint, target_equation, resp):
    res = solution_print(target_equation, resp)
    print("Solution =", res)
else:
    print("non solution")