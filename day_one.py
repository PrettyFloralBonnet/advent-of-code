import math
from typing import List

PUZZLE_INPUT = '''
109506
140405
139135
110950
84296
123991
59438
85647
81214
100517
100910
57704
83368
50777
85523
95788
127699
138908
95502
81703
67317
108468
58394
72202
121580
86908
72705
86578
83714
114900
142915
51332
69054
97039
143539
61143
113534
98335
58533
83893
127138
50844
88397
133591
83563
52435
96342
109491
81148
127397
86200
92418
144842
120142
97531
54449
91004
129115
142487
68513
140405
80111
139359
57486
116973
135102
59737
144040
95483
134470
60473
113142
78189
53845
124139
78055
63791
99879
58630
111233
80544
76932
79644
116247
54646
85217
110795
142095
74492
93318
122300
82755
147407
98697
98105
132055
67856
109731
75747
135700
'''
ALL_MODULES = [int(x) for x in PUZZLE_INPUT.split()]


def _fuel_requirement_formula(mass: int) -> int:
    fuel_needed = math.floor(mass / 3) - 2
    return fuel_needed


def calculate_fuel(modules: List[int]) -> int:
    """
    :return: amount of fuel needed to launch all modules (without taking weight of fuel itself into account)
    """
    fuel_needed = 0
    for module in modules:
        fuel_needed += _fuel_requirement_formula(module)
    return fuel_needed


def _calculate_meta_fuel_single_module(module_mass: int) -> int:
    fuel_single_module = _fuel_requirement_formula(module_mass)
    meta_fuel = _fuel_requirement_formula(fuel_single_module)
    while meta_fuel > 0:
        fuel_single_module += meta_fuel
        meta_fuel = _fuel_requirement_formula(meta_fuel)
    return fuel_single_module


def calculate_meta_fuel_all_modules(modules: List[int]) -> int:
    """
    :return: amount of fuel needed to launch all modules, including the weight of the fuel itself
    """
    fuel_all_modules = 0
    for module in modules:
        fuel_all_modules += _calculate_meta_fuel_single_module(module)
    return fuel_all_modules


if __name__ == '__main__':
    fuel = calculate_fuel(ALL_MODULES)
    total_fuel = calculate_meta_fuel_all_modules(ALL_MODULES)
    print(fuel, total_fuel)
