#how many ohms are the program allowed to overshoot your given value
overshoot = 0.15

# Creating starting values for the resistors
resistor_values_E = [1, 1.2, 2.2, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2, 10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82, 100, 120, 150, 220, 270, 330, 390, 470, 560, 680, 820]
resistor_values_K = [1, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2, 10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82, 100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 820]

# creating a list with of resistors as characters and or with 'k' added to the end of each resistor
resistor_values_Es = [element for element in list(map(str, resistor_values_E))]
resistor_values_Ks = [element + 'k' for element in list(map(str, resistor_values_K))]

# adding correct multiplication to the K and M resistors
resistor_values_K = [element * 10**3 for element in resistor_values_K]

# compile resistors into lists
compiled_resistor_values = []
compiled_resistor_values.extend(resistor_values_E)
compiled_resistor_values.extend(resistor_values_K)

compiled_resistor_value_names = []
compiled_resistor_value_names.extend(resistor_values_Es)
compiled_resistor_value_names.extend(resistor_values_Ks)

resistor_combination = []
resistor_combination_value = []
resistor_count = len(compiled_resistor_values)

# calculating the parallel pair values
resistor_values = []
for i in range(resistor_count):
    for j in range(resistor_count-i):
        resistor_a = compiled_resistor_values[i]
        resistor_b = compiled_resistor_values[j+i]
        resistor_a_name = compiled_resistor_value_names[i]
        resistor_b_name = compiled_resistor_value_names[j+i]
        
        resistor_values.append((resistor_a*resistor_b)/(resistor_a+resistor_b))
        resistor_combination.append((resistor_a_name,resistor_b_name))

print('Enter your value ')

requested_value = input()

if requested_value[-1] == 'k':
    requested_value = int(requested_value[:-1])*1000
else:
    requested_value = int(requested_value)

select = 0
for value in range(len(resistor_values)-1):
    if (abs(requested_value - resistor_values[select]) > abs(requested_value - resistor_values[value+1])) and ((requested_value + overshoot) > resistor_values[value+1]):
        select = (value+1)
    else:
        pass

if resistor_values[select] < 1000:
    if requested_value in compiled_resistor_values:
        print(f'You only need one {requested_value} O resistor')
    else:
        # prints 2 decimals correctly, rounding may prevent this
        actual_value = round(resistor_values[select],2)
        actual_value = "{:.3f}".format(actual_value)
        
        print(resistor_combination[select])
        print(f'Actual Value: {actual_value} O')
else:
    if requested_value in compiled_resistor_values:
        print(f'You only need one {requested_value/1000} kO resistor')
    else:
        # prints 2 decimals correctly, rounding may prevent this
        actual_value = round(resistor_values[select]/1000,2)
        actual_value = "{:.3f}".format(actual_value)
        
        print(resistor_combination[select])
        print(f'Actual Value: {actual_value} kO')












