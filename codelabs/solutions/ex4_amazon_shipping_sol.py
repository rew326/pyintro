# You are an owner of a cargo plane with capacity of 500kg. Amazon has asked you
# to transport as many of the items given in a specific order (their order
# cannot change) as possible from the US to Europe. They have given you a list
# of corresponding values which they will pay you for transporting. The total
# cost of shipping for you is .

capacity = 500

weights = [94,27,94,50,79,67,43,87,75,84]
values = [200,343,472,141,616,681,932,194,430,482]

shipping_cost = 3500

# Answer the following questions:
# 1. How many items can you ship to Europe
# 2. What is their total weight
# 3. Would you earn any money by acepting Amazon's request?

current_weight = 0
total_value = 0
i = 0

while current_weight < capacity:
    if capacity - current_weight >= weights[i]:
        current_weight += weights[i]
        total_value += values[i]
        i += 1
    else:
        break

print("We can ship",i,"items")
print("Their total weight is",current_weight)

if total_value > shipping_cost:
    print("We would earn money if we shipped eligible items")
else:
    print("Let's refer Amazon to our competitor FedEx")
