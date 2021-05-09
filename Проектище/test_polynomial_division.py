from RefactoringP import *
from RefactoringQ import *


polynomial1 = "3x^4+2x^2-1"
polynomial2 = "x^2+x"
print(MOD_PP_P(polynomial1, polynomial2))
this_division = ""
division_result = ""

coefficients1, steps1 = coefficients_and_steps(polynomial1)

coefficients2, steps2 = coefficients_and_steps(polynomial2)

step_polynomial1 = DEG_P_N(polynomial1)
step_polynomial2 = DEG_P_N(polynomial2)

while SRAVN_Q(step_polynomial1, step_polynomial2) == "2" or SRAVN_Q(step_polynomial1, step_polynomial2) == "0":

    need_multiplier_step = SUB_QQ_Q(step_polynomial1, step_polynomial2)
    need_coefficient = MUL_QQ_Q(coefficients1[0], coefficients2[0])
    this_division = need_coefficient+"x^"+need_multiplier_step
    if this_division[0] != "-" and this_division[0] != "+":
        this_division = "+"+this_division
    division_result += this_division
    if this_division[0] == "+":
        this_division = this_division[1:]
    this_division = MUL_PP_P(polynomial2, this_division)
    this_division = polynomial_sort(this_division)
    this_division = list_to_sting(this_division[0], this_division[1])
    polynomial1 = SUB_PP_P(polynomial1, this_division)
    polynomial1 = polynomial_sort(polynomial1)
    polynomial1 = list_to_sting(polynomial1[0], polynomial1[1])
    coefficients1, steps1 = coefficients_and_steps(polynomial1)
    step_polynomial1 = DEG_P_N(polynomial1)
if division_result[0] == "+":
    division_result = division_result[1:]
division_result = polynomial_sort(division_result)
division_result = list_to_sting(division_result[0], division_result[1])
print(division_result)

