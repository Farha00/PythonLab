# -*- coding: utf-8 -*-
"""Q4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lUby-0bzL3zL86Ihyes6lLcQfswf08DM

Q4.Develop a program to perform the following task:

a. Define a function to check whether a number is happy or not.

b. Define a function to print all happy numbers within a range.

c. Define a function to print first N happy numbers.
"""

def check_happy(n):
  for i in range(0,101):
    sum=0

    while(n>0):
      dig=n%10
      n=n//10
      sum=sum+dig**2
    n=sum
    if(sum==1):
      return True
  else:
      return False

n=int(input('Enter a number : '))
if(check_happy(n)):
  print('Happy')
else:
  print('Sad')

l=int(input('Enter lower limit : '))
u=int(input('Enter upper limit : '))
def happy():
  for i in range(l,u+1):
     if check_happy(i):
      print(i,end=' ')
happy()

N=int(input('\nEnter the number of happy numbers required : '))

def happy_list():
  count=1
  i=0
  while(count<=N):
    if check_happy(i):
      print(i,end=' ')
      count+=1
    i+=1
happy_list()