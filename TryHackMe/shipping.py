"""
    In this project, you'll create a program that calculates the total
    cost of a customers shopping basket, including shipping.

    - If a customer spends over $100, they get free shipping
    - If a customer spends < $100, the shipping cost is $1.20 per kg of the baskets weight

    Print the customers total basket cost (including shipping) to complete this exercise.

"""

customer_basket_cost = 34
customer_basket_weight = 44

# if statement to calculate the total cost
if customer_basket_cost >= 100:
    total_cost = customer_basket_cost
else:
    shipping_cost = customer_basket_weight * 1.2
    total_cost = customer_basket_cost + shipping_cost

print("The total cost of the customer's shopping basket is $", total_cost)

# The flag is: THM{IF_STATEMENT_SHOPPING}