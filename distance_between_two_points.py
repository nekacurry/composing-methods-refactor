# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.

import math

def calc_distance():
  xc1 = 4
  yc1 = 4.25
  xc2 = 53
  yc2 = -5.35

  distance = math.sqrt((xc1-xc2)**2 + (yc1 - yc2)**2)

  print('distance', distance)

def calc_vector():
  xa = -36
  ya = 97
  xb = .34
  yb = .91

  length = math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))
  print('length', length)