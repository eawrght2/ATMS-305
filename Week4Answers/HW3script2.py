#!/usr/bin/env python
import math
temp=float(input("Please input a temp in C: "))
numerator=17.625*temp
denominator=temp+243.04
svp=6.1094*math.exp(numerator/denominator)
print('Saturation Vapor Pressure is', svp)
