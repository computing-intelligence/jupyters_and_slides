# Created by mqgao at 2019/2/18

"""
Feature: #Enter feature name here
# Enter feature description here

Scenario: #Enter scenario name here
# Enter steps here

Test File Location: # Enter
"""


def get_simple_factors(n):
    simple_words = [2, 3, 5]

    if n in simple_words: return [n]

    for s in simple_words:
        if not n % s and get_simple_factors(n / s):
            return [s] + get_simple_factors(n / s)

    return None


print(get_simple_factors(6))
print(get_simple_factors(8))
print(get_simple_factors(14))
print(get_simple_factors(1845281250))
print(get_simple_factors(3690562500))
print(get_simple_factors(1230187500))
print(get_simple_factors(10023750))

