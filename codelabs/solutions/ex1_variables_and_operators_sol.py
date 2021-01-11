import math

# Task 1.: The volume of a sphere with radius r is (4/3)*πr^3.
# What is the volume of a sphere with radius 5?

radius = 5
pi = math.pi
print((4/3)*(radius**3)*pi)

# Task 2;. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?

cover = 24.95
discount = 0.6
shipping_first = 3
shipping_copy = 0.75
copies = 60
total = shipping_first + shipping_copy*(copies - 1) + cover*copies*discount
print(total)

# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
# what time do I get home for breakfast?

leave_time_secs = (6*60 + 52)*60
easy_miles = 2
tempo_miles = 3
easy_secs = 8*60 + 15
tempo_secs = 7*60 + 12

arrival_time_secs = leave_time_secs + easy_miles * easy_secs + tempo_miles * tempo_secs

arrival_hours = math.floor(arrival_time_secs / (60 * 60))
arrival_minutes = math.floor((arrival_time_secs % (60 * 60)) / 60)
arrival_secs = arrival_time_secs % 60

print(str(arrival_hours) + ":" + str(arrival_minutes).zfill(2) + ":" + str(arrival_secs).zfill(2))
