# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January? -----> done
# 2. Find out your total expense in first quarter (first three months) of the year.----> done
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

my_list = [
    {'January': 2200},
    {'February': 2350},
    {'March': 2600}
]
if my_list[0]['January'] > my_list[1]['February']:
    extra_in_feb = int(my_list[0]['January'] - my_list[1]['February'])
else:
    extra_in_feb = int( my_list[1]['February'] - my_list[0]['January'])

print(f'1. dollars you spent extra in feb compare to January is',extra_in_feb)

first_quater_expense =int(my_list[0]['January'] + my_list[1]['February'] + my_list[2]['March'])

print(f'2. total expense in first quarter (first three months) of the year',first_quater_expense)

for i in range(my_list):
    if my_list[i]