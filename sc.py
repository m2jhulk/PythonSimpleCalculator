value_1 = float(input("Please enter First value: "))
value_2 = float(input("Please enter Second value: "))
user_selection = int(input("please enter 1 for 'Addition', 2 for 'Substraction', 3 for 'Multiplication' Or 4 for 'Division': "))
if user_selection == 1:
  print(f"{value_1} + {value_2} = {value_1 + value_2}")
elif user_selection == 2:
  print(f"{value_1} - {value_2} = {value_1 - value_2}")
elif user_selection == 4:
  if value_2 == 0:
    print("undefined/division is not possible by zero")
  else:
    print(f"{value_1} / {value_2} = {value_1 - value_2}")
elif user_selection == 3:
  print(f"{value_1} * {value_2} = {value_1 * value_2}")
else:
  print("Please select 1/2/3/4. Run code again")