# -*- coding: utf-8 -*-
"""lab2Q1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a8thp4rM2jGuoceynEYHaB5QShZxU-xb

1.Suppose a newly born pair of rabbits, one male and one female, are put in a field. Rabbits can mate at the age of one month so that at the end of its second month, a female has produced another pair of rabbits. Suppose that our rabbits never die and that the female always produces one new pair every month from the second month. 

Develop a program to show a table containing the number of pairs of rabbits in the first N months
"""

n=int(input("Enter the number of months required : "))
month_1=0
month_2=1
print("Month\t\tNo of pairs of rabbit")
for i in range(n):
  temp=month_2
  month_2+=month_1
  month_1=temp
  print(i+1,"\t\t",month_1)