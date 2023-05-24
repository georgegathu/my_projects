
customer_basket_cost = 101
customer_basket_weight = 44

# if statement to calculate the total cost
if customer_basket_cost >= 100:
    total_cost = customer_basket_cost
else:
    shipping_cost = customer_basket_weight * 1.2
    total_cost = customer_basket_cost + shipping_cost

print("The total cost of the customer's shopping basket is $", total_cost)

# The flag is: THM{MY_FIRST_APP}