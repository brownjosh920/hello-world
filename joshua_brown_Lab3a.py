# Input the conversion of US metric measurement

# Input the miles to kilometers
miles = float(input("Tell me the amount of miles you want to convert to km's "))
# calculate to kilometers
miles_to_km = miles * 1.6

# Get results based on various range
if miles > 0 and miles <= 2:
    # Display the results that are two or less miles
    print(miles_to_km,"kilometers. That's a block away from here")
# Get results that are greater than two but no more than 5 miles
elif miles > 2 and miles <= 5:
    # Display printed results
    print(miles_to_km, 'kilometers You could travel by riding a bicycle')
# Get results that are greater tham five but no more than 20 miles
elif miles > 5 and miles <= 20:
    # Display printed results
    print(miles_to_km, "kilometers. You can travel by driving a car")
# Get results that are greater and twenty but no more than 75 miles
elif miles > 20 and miles <= 75:
    # Display printed results
    print(miles_to_km, "kilometers. It is pretty far don't you think?")
# Get results greater than 75 miles
elif miles > 75:
    # Display printed results
    print(miles_to_km, 'kilometers. You might want to take a plane or train')
elif miles < 0:
    print('Invalid input')

# Input the gallons to liters
gallons = float(input('Tell me the amount of gallons you want to convert to liters: '))
# Calculate to liters
gallons_to_liters = gallons * 3.9

# Get the results based on various range
if gallons == 1:
    print(gallons_to_liters, 'liters is large enough for a large bottled soda or one milk')
elif gallons > 1 and gallons <= 5:
    print(gallons_to_liters, 'liters is alot of milk and too many large bottled sodas')
elif gallons > 5:
    print(gallons_to_liters, 'liters can buy you enough gas for your vehicle')
elif gallons < 1:
    print('Invalid input')
    
# Input the pounds to kilograms
pounds = float(input('Tell me the number of pounds you want to convert to kilograms: '))
# Calculate to kilograms
pounds_to_kilograms = pounds * 0.45

# Get the results based on various range
if pounds > 0 and pounds <= 5:
    print(pounds_to_kilograms, 'kilograms is light')
elif pounds > 5 and pounds <= 20:
    print(pounds_to_kilograms, 'kilograms is enough to budge a scale')
elif pounds > 20 and pounds <= 50:
    print(pounds_to_kilograms, 'kilograms is kind of heavy like a supply box or midclass dumbbell')
elif pounds > 50 and pounds <= 100:
    print(pounds_to_kilograms, 'kilograms is pretty haavy')
elif pounds > 100 and pounds <= 500:
    print(pounds_to_kilograms, 'kilograms is very heavy')
elif pounds > 500:
    print(pounds_to_kilograms, 'kilograms exceeds the hundred amount of kilograms')
elif pounds < 0:
    print('Invalid input')

# Input inches to centimeters
inches = float(input('Enter the amount of inches you want me to convert to centimeters: '))
# Calculate to centimeters
inches_to_cm = inches * 2.54

# Get the results based on various range
if inches > 0 and inches < 12:
    print(inches_to_cm, 'centimeters is less than a foot long')
elif inches >= 12 and inches <= 24:
    print(inches_to_cm, 'centimeters is between one and two feet')
elif inches > 24 and inches <= 48:
    print(inches_to_cm, 'centimeters is a height of an average child')
elif inches > 48 and inches <= 72:
    print(inches_to_cm, 'centimeters is between a height of a teenager and a fully grown man')
elif inches > 72 and inches <= 120:
    print(inches_to_cm, 'centimeters is a height of a tall basketball player and a traffic lights pole')
elif inches > 120:
    print(inches_to_cm, 'centimeters can be as tall as a house or empire state building')
elif inches < 0:
    print('Invalid input')
    
# Input Fahrenheit to Celsius
Fahrenheit = float(input('Enter the Fahrenheit degree you want me to convert to Celsius: '))
# Calculate to Celsius
F_to_C = (Fahrenheit - 32) * 5/9

# Get the results based on various range
if Fahrenheit >= 0 and Fahrenheit <= 10:
    print(F_to_C, 'degrees Celsius is subzero or below')
elif Fahrenheit > 10 and Fahrenheit <= 20:
    print(F_to_C, 'degrees Celsius is a little below zero')
elif Fahrenheit > 20 and Fahrenheit <= 31:
    print(F_to_C, 'degrees Celsius is between below zero and absolute zero')
elif Fahrenheit >= 32 and Fahrenheit <= 50:
    print(F_to_C, 'degrees Celsius is from subzero to freezing cold')
elif Fahrenheit > 50 and Fahrenheit <= 100:
    print(F_to_C, 'degrees Celsius is form very cold to breezy weather')
elif Fahrenheit > 100 and Fahrenheit <= 200:
    print(F_to_C, 'degrees Celsius is from breezy to very nice weather')
elif Fahrenheit > 200 and Fahrenheit <= 300:
    print(F_to_C, 'degrees Celsius is from room temperature, boiling point somehere to sizzling hot')
elif Fahrenheit > 300 and Fahrenheit <= 1000:
    print(F_to_C, 'degrees Celsius is either a freaky weather or sun')
elif Fahrenheit > 1000:
    print('Invalid input')
