#!/usr/bin/env python3

"""
0d253fc658439bdd9c338c663dcc677d
python
lab1
v3
jogg16
2018-08-29 09:45:43
v3.1.0 (2018-08-17)

Generated 2018-09-01 13:40:50 by dbwebb lab-utility v3.1.0 (2018-08-17).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 1 - python
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python manual](https://docs.python.org/3/library/index.html).
#
# There you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Integers, floats and basic arithmetics
#
# The foundation of numbers and basic arithmetic.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a variable called `num_one` and give it the value 17.
#
# Answer with the value of `num_one`.
#
# Write your code below and put the answer into the variable ANSWER.
#


num_one = 17



ANSWER = num_one

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create another variable called `num_two` and give it the value 51. Create a
# third variable called `result` and assign to it the sum of the first two
# variables.
#
# Answer with the `result` variable.
#
# Write your code below and put the answer into the variable ANSWER.
#

num_two = 51
result = num_one + num_two




ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a variable called `num_three` and give it the value 79.
#
# Create another variable called `num_four` and give it the value 31.
#
# Subtract `num_three` from `num_four` and add the `result` variable from
# above to result of the subtraction. Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

num_three = 79
num_four = 31

result3 = (num_four-num_three+result)





ANSWER = result3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Answer with the result of a multiplication of `num_one` and `num_three`.
#
# Write your code below and put the answer into the variable ANSWER.
#

result4 = num_one * num_three




ANSWER = result4

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a variable called `float_one` and give it the value 59.98.
#
# Create another variable called `float_two` and give it the value 27.69.
#
# Sum the two values and answer with the result, rounded to two decimals. Use
# the function `round()` to round the number.
#
# Write your code below and put the answer into the variable ANSWER.
#
float_one = 59.98
float_two = 27.69
result5 = round(float_one+float_two, 2)





ANSWER = result5

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# All variables used in the exercise below are defined above.
#
# Sum `num_three` with `num_one` and subtract `num_four`. Multiply the result
# by `num_two`, add `float_two` and subtract `float_one`.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#


result6 = (num_three + num_one - num_four) * num_two + (float_two - float_one)



ANSWER = result6

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, True)

# --------------------------------------------------------------------------
# Section 2. Strings and concatenation
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Concatenate (svenska: konkatenera) the two words 'program' and 'restaurant'
# and answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

str1 = "program"
str2 = "restaurant"
str3 = str1+str2




ANSWER = str3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Concatenate the word 'restaurant' with the integer 17, with a space between
# the two values.
# Answer with the new string.
#
# Write your code below and put the answer into the variable ANSWER.
#

result22 = "restaurant " + str(17)




ANSWER = result22

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Concatenate the integer 17 with the word 'program' with a space between. To
# the resulting string concatenate the string ' and '. To this string
# concatenate integer 51 and the word 'restaurant' with a space between
# between the two variables.
#
# Write your code below and put the answer into the variable ANSWER.
#


result23 = str(17) + " program and " + str(51) + " restaurant"




ANSWER = result23

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Assign the string value '30' to a variable called `string_number` and
# assign the integer value 5 to a variable called `actual_number`.
#
# Use `int()` to change the type of `string_number` to an integer and divide
# the integer value with `actual_number`. Answer with an integer by using the
# function `round()`.
#
# Write your code below and put the answer into the variable ANSWER.
#

string_number = str(30)
actual_number = int(5)
result24 = round(int(string_number) // actual_number)

ANSWER = result24

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, True)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# BTH have two plugin-hybrid cars. A new car and an old car. The new car has
# a fast charging mode where 80% of the battery can be charged in 30 minutes.
# The remaining 20% of the battery and the entire battery of the old car is
# charged by 5% every 30 minutes.
#
# During fast charging the effect of the charger is 200W and during normal
# charging the effect of the charger is 100W.
#
# The formula for calculating the amount of energy based on effect and time
# is: `energy = effect * time`. To get the amount of energy in kWh the
# formula is `energy = (effect in W * time in hours) / 1000`.
#
# Calculate the total amount of energy used to fully charge the two cars.
# Answer with the amount of energy in kWh.
#
# Write your code below and put the answer into the variable ANSWER.
#

energi1 = 100
energi2 = 200
time = 1

newcar1 = int(time*energi2)
newcar2 = int(time*4*energi1)

oldcar = int(time*20*energi1)

TotNewCar = (newcar2 + newcar1)
float(TotNewCar)
float(oldcar)

result31 = float(((TotNewCar+oldcar)/2)/1000)

ANSWER = result31

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Peter has the phonenumber '0731415926' and Anna has the phonenumber
# '0727182818'. They call each other every sunday afternoon for 9 minutes.
#
# Calculate the number of hours that they talk with each other pr year
# (assume 52 sundays pr year). Use that number in a string concatenation with
# the following format:
#
# 'Peter calls from [#Peter's phonenumber] to Anna on [#Anna's phonenumber]
# for [#hours] hours every year.'
#
# Replace the content inside [#] with the corresponding values.
#
# Answer with the concatenated string.
#
# Write your code below and put the answer into the variable ANSWER.
#

peter = "0731415926"
anna = "0727182818"
sundays = 52
minPerCall = 9
minutes = minPerCall*sundays
hours = minutes/60
result32 = "Peter calls from "+peter+" to Anna on "+anna+" for "+str(hours)+" hours every year."
ANSWER = result32

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, True)


dbwebb.exit_with_summary()
