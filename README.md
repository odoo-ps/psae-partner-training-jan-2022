# psae-partner-training-jan-2022

# The Flower App 4

Sally came back to you with an additional request. Her business has been more successful than ever 
and she's been running out of stock more frequently. 

Therefore, she decided to start planting more flowers. This made it hard for her to keep track of 
watering times. Sally now wants to track every flower she has planted using serial numbers. Additionally, 
she wants to have a list tracking all the watering she have done.

Hints:
  * find the model responsible for serial numbers
  * create a new model for tracking watering flower.water
  * implement some mechanism on stock.production.lot to know when this quant was watered (maybe a computed field?)
  * add a button on stock.quant to create and link a new record of flower.water (Use fields.Date.today())
  * add a constraint on stock.production.lot to prevent the user from watering before they're supposed to (compare the last watering date with the watering frequency)
  * for more convenience, add a server action that automatically attempts to water all selected plants in a list view
