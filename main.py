# Using the list sandwich_orders from Exercise 7-8,
# make sure the sandwich 'pastrami' appears in the
# list at least three times. Add code near the
# beginning of your program to print a message saying
# the deli has run out of pastrami and then use a
# while loop to remove all occurrences of 'pastrami'
# from sandwich_orders. Make sure no pastrami
# sandwiches end up in finished_sandwiches.
sandwich_orders = [
    "pastrami sandwich",
    "tuna sandwich",
    "turkey sandwich",
    "pastrami sandwich",
    "chicken sandwich",
    "steak sandwich",
    "pastrami sandwich",
]
finished_sandwiches = []

print("\nI am sorry, the deli has run out of pastrami "
      "sandwiches.")

while "pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("pastrami sandwich")

# print(sandwich_orders)

for sandwich_order in sandwich_orders:
    print(f"\nI made your {sandwich_order} sandwich.")
    finished_sandwiches.append(sandwich_order)

print(f"\nHere is a list of your finished "
      f"{finished_sandwiches} sandwiches.")
