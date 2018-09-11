#!/usr/bin/env python3

"""
0f2beacbabc1e43b80d1583ba5d36932
python
lab2
v3
jogg16
2018-09-08 13:32:57
v3.1.2 (2018-09-06)

Generated 2018-09-08 15:32:57 by dbwebb lab-utility v3.1.2 (2018-09-06).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - python
#
# In this exercise we will look into flow-control. If-statements, for-loops
# and while-loops.
#



# --------------------------------------------------------------------------
# Section 1. Boolean operators and if-statements
#
# The basics of boolean operators and if-statements.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create three variables representing dice values: `dice1` = 2, `dice2` = 3
# and `dice3` = 5.
#
# Answer with the boolean value of the expression '`dice1` is greater than
# `dice2`'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice1 = 2
dice2 = 3
dice3 = 5
finaldice = bool(dice1 > dice2)






ANSWER = finaldice

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Sum the three variables `dice1`, `dice2` and `dice3`.
#
# Use an if-statement to decide if the sum of the three variables i greater
# than 11. If the sum is greater than 11 answer with 'big' otherwise answer
# with 'small'.
#
# Write your code below and put the answer into the variable ANSWER.
#

threedice = dice1+dice2+dice3

if threedice > 11:
    result1_2 = 'big'
else:
    result1_2 = 'small'

ANSWER = result1_2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Add the sum of `dice4` = 3 and `dice5` = 6 to the sum of the three other
# dices.
#
# Use an if, elseif, else statement to check the total value of the dices.
# Answer with 'small' if the sum is smaller than 11, 'intermediate' if the
# sum is greater than or equal to 11 but smaller than 21. If the sum is
# greater than or equal to 21 answer with 'big'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice4 = 3
dice5 = 6
totdice = dice1 + dice2 + dice3 + dice4 + dice5

if totdice < 11:
    result1_3 = "small"
elif 21 > totdice <= 11 :
    result1_3 = "intermediate"
else:
    result1_3 = "big"


ANSWER = result1_3


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a variable `summer_word` containing the word 'water'.
#
# Answer with True if `summer_word` contains the letter 's' otherwise answer
# with False.
#
# Tip: Use the `in` operator.
#
# Write your code below and put the answer into the variable ANSWER.
#

summer_word = 'water'

if summer_word in 's':
    result1_4 = bool(1)
else:
    result1_4 = bool(0)

ANSWER = result1_4

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. For-loops
#
# The basics of iteration and for-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Loop through the numbers 0 to 10 (10 included) and concatenate a string
# with the numbers comma-separated. You should have a comma at the end of the
# string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

result2_1 = ""

for value2_1 in range(0, 11):
    result2_1 = result2_1 + str(value2_1) + ","

ANSWER = result2_1

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Loop through the letters of the variable `summer_word` from above.
# Concatenate the consonants from `summer_word` and answer with the new word.
#
# Tip: Create a string that contains consonants and check if each letter is
# in it.
#
# Write your code below and put the answer into the variable ANSWER.
#

consonant = summer_word[0]
consonant2 = summer_word[2]
consonant3 = summer_word[4]
result2_2 = consonant + consonant2 + consonant3

if result2_2 in summer_word:
    print(result2_2)


ANSWER = result2_2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Loop through all numbers from 30 to 76 both numbers included. Add all odd
# (udda) numbers together and answer with the result.
#
# Tip: Use the modulus % operator.
#
# Write your code below and put the answer into the variable ANSWER.
#

result2_3 = 0
for value2_3 in range(30, 77):
    if value2_3 % 2 != 0:
        result2_3 += value2_3


ANSWER = result2_3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, True)

# --------------------------------------------------------------------------
# Section 3. While-loops
#
# The basics of while-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (1 points)
#
# Create a while-loop that starts at value 9 and ends when the value is
# greater than 76, the value should be incremented by 3 for each iteration.
# Concatenate a string with the values comma-separated. You should have a
# comma at the end of the string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

value3_1 = 9
result3_1 = ""
while value3_1 <= 76:
    result3_1 += str(value3_1) + ","
    value3_1 += 3


ANSWER = result3_1

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (1 points)
#
# Create a while-loop that adds 9 to the number 15, 76 times. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#

start = 15
result3_2 = ""
ninetimes = (9*76)

while (start > 0):
    result3_2 = start + ninetimes
    break



ANSWER = result3_2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.3 (1 points)
#
# Create a while-loop that subtracts 5 from 91, 32 times. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#

result3_3 = 91-(5*32)

while (result3_3 > 0):
    print(result3_3)

ANSWER = result3_3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 4. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.1 (3 points)
#
# Use a for-loop or a while-loop to reverse the word 'disproportionality'.
#
# Answer with the reversed word.
#
# Write your code below and put the answer into the variable ANSWER.
#

word4_1 = 'disproportionality'

while (word4_1[0] == 'd'):
    result4_1 = 'disproportionality'[::-1]
    break


ANSWER = result4_1

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.2 (3 points)
#
# Swedish numberplates consist of three letters and three numbers. The
# numbers range from 001 to 999. Using one of the four common rules of
# arithmetics (+, -, *, /), on how many of the numberplates can the two first
# numbers give the third number?
#
# Examples:
# 'ABC123' can be combined to 1 + 2 = 3. So this numberplate is good.
# 'ABC129' 1 and 2 cannot be combined to give 9 using the four rules of
# arithmetics, so this does not work.
#
# Order matters, so only use 1 +-*/ 2 = 3 and not 2 +-/* 1 = 3.
#
# Do not count multiple times if more than one rule of arithmetics work.
#
# Answer with the number of numberplates.
#
# Write your code below and put the answer into the variable ANSWER.
#

allnumbers = range(0, 1000)
twonumbers = range(0, 100)



ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.2", ANSWER, True)


dbwebb.exit_with_summary()
