"""Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list"""

numbers=list(range(1,11))
print("Original list:",numbers)
first_five_numbers=numbers[:5]
print("Extracted first Five element:",first_five_numbers)
Reversed_number=first_five_numbers[::-1]
print("Reversed extracted elements:",Reversed_number)
