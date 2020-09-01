================================================================================
Solutions: Type Checking
================================================================================

.. sectnum::
   :start: 1
   :suffix: .
   :depth: 2

.. contents:: Contents:
   :depth: 2
   :backlinks: entry
   :local:


Type Checking
================================================================================


Exercises: Closures
---------------------

Exercise 1: Taxes
~~~~~~~~~~~~~~~~~

.. code:: python

   def get_tax_percentage(income: int) -> int:
       if income < 20000:
           return 0
       elif income <= 50000:
           return 30
       else:
           return 60

   def print_tax_percentage(income: int) -> None:
       print("Your taxes " + str(get_tax_percentage(income)))

   income = int(input("How much do you earn? "))
   print_tax_percentage(income)

Exercise 2: Students
~~~~~~~~~~~~~~~~~

.. code:: python

   from typing import Dict, Tuple, Union
   import statistics
   grades = {'John': [8, 2, 3, 6, 8],
             'Annie': [5, 8, 7, 8, 5],
             'Pete': [8, 8, 6, 7, 9],
             'Lucy': [2, 4, 5, 6, 7],
             'Bob': [6, 7, 5, 6, 7]}

   # Write a function get_average(name) that takes the name of a student
   # and returns their average. Add type checking to this function.

   def get_average(name: str) -> float:
       grades_for_student = grades[name]
       return sum(grades_for_student)/len(grades_for_student)

   #
   # Write a function best_student() that returns
   # the name of the student with the highest average
   # AND their highest grade. Add type checking to this function as well.


   def best_student(student: Dict) -> Tuple[str, int]:
       best_grade = 0
       best_student_name = ''
       for student in grades:
           if get_average(student) > best_grade:
               best_grade = max(grades[student])
               best_student_name = student
       return (best_student_name, best_grade)


   print(best_student(grades))


Exercise 3: Shop
~~~~~~~~~~~~~~~~~~~

.. code:: python

   from typing import Dict, List, Any, Optional

   inventory = [{'name': 'bread', 'price': 2, 'stock': 100},
                {'name': 'coffee', 'price': 3, 'stock': 40},
                {'name': 'cheese', 'price': 3, 'stock': 30},
                {'name': 'milk', 'price': 1, 'stock': 80}]


   def print_table(table: List[Dict[str, Any]]) -> None:
       print("Name     Price    Stock")
       print("--------------------------")
       for prod in inventory:
           print(prod['name'], "\t", prod['price'], '\t', prod['stock'])


   def find_prod_by_name(name: str) -> Optional[Dict[str, Any]]:
       for prod in inventory:
           if prod['name'] == name.lower():
               return prod
       return None


   print_table(inventory)
   choice = input("Select a product? ")
   product = find_prod_by_name(choice)
   if product:
       amount = int(input("Amount in stock? "))
       product['stock'] = amount
       print_table(inventory)
   else:
       print("Unknown product")
