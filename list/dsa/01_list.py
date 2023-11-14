# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,


# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

my_list = [
    {'January': 2200},
    {'February': 2350},
    {'March': 2600}
    {'April' : 2130}
    {'May' : 2190}
]
if my_list[0]['January'] > my_list[1]['February']:
    extra_in_feb = int(my_list[0]['January'] - my_list[1]['February'])
else:
    extra_in_feb = int( my_list[1]['February'] - my_list[0]['January'])

# 1. In Feb, how many dollars you spent extra compare to January? -----> done

print(f'1. dollars you spent extra in feb compare to January is',extra_in_feb)

# 2. Find out your total expense in first quarter (first three months) of the year.----> done

first_quater_expense =int(my_list[0]['January'] + my_list[1]['February'] + my_list[2]['March'])

print(f'2. total expense in first quarter (first three months) of the year',first_quater_expense)

# 3. Find out if you spent exactly 2000 dollars in any month

spent_2000 = False

for month in my_list:
    for expense in month.values():
        if expense == 2000:
            spent_2000 = True
            break  # Exit the inner loop once we find a match
    if spent_2000:
        break  # Exit the outer loop once we find a match

print(f'3. Did you spend exactly 2000 dollars in any month? {"Yes" if spent_2000 else "No"}.')

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

my_list.append({'June': 1980})
print(my_list)



