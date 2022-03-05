# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

def inputs(n_student):
  grade_list = []
  for _ in range(n_student):
    grade_list.append(int(input('Enter a number: ')))

  return grade_list

def calc_mean(grade_list):
  total = 0
  for grade in grade_list:
    total += grade
  mean = total / len(grade_list)

  return mean

def calc_standard_dev(grade_list, mean):
  sum_of_sqrs = 0
  for grade in grade_list:
    sum_of_sqrs += (grade - mean) ** 2
  sd = math.sqrt(sum_of_sqrs / len(grade_list))

  return sd

def output(mean, sd):
  print('****** Grade Statistics ******')
  print("The grades's mean is:", mean)
  print('The population standard deviation of grades is: ', round(sd, 3))
  print('****** END ******')

def print_stat():
  n_student = 5
  grade_list = inputs(n_student)
  mean = calc_mean(grade_list)
  sd = calc_standard_dev(mean, grade_list)

  output(mean, sd)

print_stat()