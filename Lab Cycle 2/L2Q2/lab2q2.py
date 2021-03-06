# -*- coding: utf-8 -*-
"""Lab2Q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fk_6wNSEaPwbhlEGmEYyvDNJigQNk4wc

Q2.Write a program to read a string containing numbers separated by a space and convert it as a list of integers. Perform the following operations on it.

1.Rotate elements in a list by 'k' position to the right

2.Convert the list into a tuple using list comprehension

3.Remove all duplicates from the tuple and convert them into a list again.

4.Create another list by putting the results of the evaluation of the function 𝑓(𝑥) = 𝑥 2 – 𝑥 with each element in the final list

5.After sorting them individually, merge the two lists to create a single sorted list
"""

string = input("Enter the list of numbers : ")
list_numbers = list(string.split(" "))

int_list = []
for i in list_numbers:
  int_list.append(int(i))
print("The list of integers = ",int_list)

k = int(input("Enter the number you want to rotate : "))
print("The list after rotating by",k,"position to right is ",end = " = ")
print(int_list[-k:]+int_list[:-k])

int_tup = tuple(int_list)
print("List to Tuple = ",int_tup)

int_tup = tuple(set(int_tup))
int_list = list(int_tup)
print("List after removing duplicates ",end = " = ")
print(int_list)

square = []
for i in int_list:
  square.append((i**2)-i)
print("Lists of results of the Function ",end = " = ")
print(square)

sorted_list = int_list + square
sorted_list.sort()
print("Final Sorted List ",end = " = ")
print(sorted_list)