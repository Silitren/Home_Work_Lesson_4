# Task_1
from sys import argv

Calc_zp, stavka, vurob, premia = argv
print(f"Заработная плата: {int(stavka) * int(vurob) + int(premia)}")
