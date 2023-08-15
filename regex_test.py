import re
import numpy as np

constraints = "2*x1 -3*x2 +9*x4 -0*x6 >= 4\n3*x1 +5*x2 -6*x4 < 6\n1*x1 -7*x2 +10*x3 == 1"
constraint_one_by_one = constraints.split('\n')

pattern = r'([+-]?\d+)\s*\*?\s*([a-zA-Z0-9]+)\s*([<>]=?|==)\s*([+-]?\d+)'

coeff_regex = r'([+-]?\d+)\s*\*?\s*([a-zA-Z0-9]+)\s*'
signe_regex = r'([<>]=?|==)\s*([+-]?\d+)'

coeff_tab = []
variables_tab = []
signe_tab = []
const_tab = []

for constraint in constraint_one_by_one:
    coeff_catcher = re.findall(coeff_regex, constraint)
    signe_catcher = re.findall(signe_regex, constraint)
    coefficients = [int(match[0]) for match in coeff_catcher]
    variables = [match[1] for match in coeff_catcher]
    coeff_tab.append(coefficients)
    variables_tab.append(variables)
    signe = [match[0] for match in signe_catcher]
    constant = [int(match[1]) for match in signe_catcher]
    signe_tab.append(signe)
    const_tab.append(constant)


print(np.array(coeff_tab))  # Output: [2, -3]
print(variables_tab)     # Output: ['x1', 'x2']

print(signe_tab)
print(const_tab)

print(constraints)
print(constraint_one_by_one[0])