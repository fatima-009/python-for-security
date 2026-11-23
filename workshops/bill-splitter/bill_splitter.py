# Bill Splitter Workshop
# Practicing numbers and mathematical operations

# Step 1: running total starts at 0
running_total = 0

# Step 2: number of people sharing the bill
num_of_friends = 5

# Step 3: cost of each course (floats, because they include cents)
appetizers = 42.15
main_courses = 68.72
desserts = 29.46
drinks = 51.83

# Step 4: add all the costs to the running total with +=
running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

# Step 5: calculate a 20% tip by multiplying by 0.20
tip = running_total * 0.20
print('Tip amount:', tip)

# Step 6: add the tip to the running total
running_total += tip
print('Total with tip:', running_total)

# Step 7: split the bill between the friends with division
final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

# Step 8: round to two decimal places, since this is money
each_pays = round(final_bill, 2)
print('Each person pays:', each_pays)