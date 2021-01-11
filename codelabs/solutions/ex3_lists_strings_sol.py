# Task 1. Given a list, print the same list without the first and last element

t = [1, 2, 3, 4, 5, 6]

print(t[1:5])

# Task 2. Print every other character in the given string

text = "London Zoo have reportedly rejected Ricky Gervais’ wish to be fed to their lions after his death."

print(text[::2])

# Task 3. Check if 42 is in the list of numbers:

numbers = [11, 12, 19, 33, 36, 43, 64, 67, 74, 79, 101, 102, 109, 115, 116, 121, 154, 169, 174, 186, 199, 205, 223, 227, 234, 241, 250, 256, 266, 274, 276, 282, 294, 305, 307, 331, 347, 348, 369, 382, 385, 406, 410, 419, 423, 436, 456, 458, 460, 468, 485, 499, 503, 514, 526, 531, 540, 567, 573, 586, 587, 605, 607, 634, 636, 648, 661, 663, 666, 672, 685, 700, 712, 715, 721, 736, 742, 759, 767, 790, 818, 862, 863, 874, 876, 882, 887, 889, 890, 893, 894, 908, 910, 916, 917, 928, 955, 961, 972]

if 42 in numbers:
    print("Yes")
else:
    print("No")

# Task 4. Fill a list with all personal information given in the text (e.g.: ["Bruce","Wayne",...]):

text = "First Name:Tony;Last Name:Stark;Alias:Iron Man;Publisher: Marvel Comics;First appearance:Tales of Suspense;Created by:Stan Lee, Larry Lieber, Don Heck, Jack Kirby;Place of origin: Long Island, New York;Team affiliations: Avengers"

personal_info = []

split = text.split(";")
personal_info.append(split[0].split(":")[1])
personal_info.append(split[1].split(":")[1])
# etc.

print(personal_info)
