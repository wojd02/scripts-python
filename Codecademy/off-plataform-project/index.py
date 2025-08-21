import csv
#goals
 # average total charge and by region
 # total of smoker and non-smoker

#age,sex,bmi,children,smoker,region,charges
ages = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

def list_joint(list_1, list_2, list_3, list_4, list_5, list_6, list_7):
    empty_dict = {}
    for key, row in enumerate(list_1):
        empty_dict[key] = [{'age': row, 'sex': list_2[key], 'bmi': list_3[key], 'children': list_4[key], 'smoker': list_5[key], 'region': list_6[key], 'charges': list_7[key]}]
    return empty_dict

def patients_per_region(region_list, age_list):
    average_patients = {}
    for key, region in enumerate(region_list):
        if region not in average_patients:
            average_patients[region] = [age_list[key]]
        elif region in average_patients:
            average_patients[region].append(age_list[key])
    return average_patients

def charge_region(region_list, charge_list):
    charges_per_region = {}
    charges_per_region_total = {}
    for key, region in enumerate(region_list):
        if region not in charges_per_region:
            charges_per_region[region] = [charge_list[key]]
        elif region in charges_per_region:
            charges_per_region[region].append(charge_list[key])
    for key in charges_per_region:
        charges_per_region_total[key] = sum(charges_per_region[key])
    for key in charges_per_region:
        charges_per_region[key] = sum(charges_per_region[key]) / len(charges_per_region[key])
    return charges_per_region, charges_per_region_total

def avg_age(region_list, ages_list):
    average_age = {}
    for key, region in enumerate(region_list):
        if region not in average_age:
            average_age[region] = [ages_list[key]]
        elif region in average_age:
            average_age[region].append(ages_list[key])
    for key in average_age:
        average_age[key] = sum(average_age[key]) / len(average_age[key])
    return average_age

def patients_w_child(list):
    empty_dict = {'One child': [], 'Two children': [], 'Three children': [], '4 or more children': []}
    counter = 0
    for patient in list:
        if patient != 0:
            counter += 1
        else:
            pass
    for patient in list:
        if patient == 1:
            empty_dict['One child'].append(patient)
        elif patient == 2:
            empty_dict['Two children'].append(patient)
        elif patient == 3:
            empty_dict['Three children'].append(patient)
        elif patient > 3:
            empty_dict['4 or more children'].append(patient)
    return counter, empty_dict

def total_smokers(region_list, smoker_list):
    total_smoker_per_region = {}
    for key, region in enumerate(region_list):
        if smoker_list[key] == 'yes':
            if region not in total_smoker_per_region:
                    total_smoker_per_region [region] = [smoker_list[key]]
            elif region in total_smoker_per_region :
                total_smoker_per_region [region].append(smoker_list[key])
        else:
            pass
    return total_smoker_per_region

def avg_bmi_per_region(region_list, bmi_list):
    average_bmi= {}
    for key, region in enumerate(region_list):
        if region not in average_bmi:
            average_bmi[region] = [bmi_list[key]]
        elif region in average_age:
            average_bmi[region].append(bmi_list[key])
    for key in average_age:
        average_bmi[key] = sum(average_bmi[key]) / len(average_bmi[key])
    return average_bmi

def classification_bmi(bmi_list):
    empty_dict = {'Underweight': [], 'Normal range': [], 'Overweight': [], 'Obese 1': [], 'Obese 2': [], 'Obese 3': []}
    for patient in bmi_list:
        if patient <= 18.5:
            empty_dict['Underweight'].append(patient)
        elif  18.5 < patient <= 24.9:
            empty_dict['Normal range'].append(patient)
        elif 24.9 < patient <= 29.9:
            empty_dict['Overweight'].append(patient)
        elif 29.9 < patient <= 34.9:
            empty_dict['Obese 1'].append(patient)
        elif 34.9 < patient <= 39.9:
            empty_dict['Obese 2'].append(patient)
        elif patient > 39.9:
            empty_dict['Obese 3'].append(patient)
    return empty_dict

def costs_age(age_list, charge_list):
    empty_dict = {'25 years': [], '26-35 years': [], '36-45 years': [], '46-55 years': [], '56-65 years': [], '66 years': []}
    for key, patient in enumerate(age_list):
        if patient <= 25:
            empty_dict['25 years'].append(charge_list[key])
        elif  25 < patient <= 35:
            empty_dict['26-35 years'].append(charge_list[key])
        elif 35 < patient <= 45:
            empty_dict['36-45 years'].append(charge_list[key])
        elif 45 < patient <= 55:
            empty_dict['46-55 years'].append(charge_list[key])
        elif 55 < patient <= 65:
            empty_dict['56-65 years'].append(charge_list[key])
        elif patient > 65:
            empty_dict['66 years'].append(charge_list[key])
    for key in empty_dict:
        empty_dict[key] = sum(empty_dict[key])
    return empty_dict

def count_age(age_list):
    empty_dict = {'25 years': [], '26-35 years': [], '36-45 years': [], '46-55 years': [], '56-65 years': [], '+66 years': []}
    for key, patient in enumerate(age_list):
        if patient <= 25:
            empty_dict['25 years'].append(age_list[key])
        elif  25 < patient <= 35:
            empty_dict['26-35 years'].append(age_list[key])
        elif 35 < patient <= 45:
            empty_dict['36-45 years'].append(age_list[key])
        elif 45 < patient <= 55:
            empty_dict['46-55 years'].append(age_list[key])
        elif 55 < patient <= 65:
            empty_dict['56-65 years'].append(age_list[key])
        elif patient > 65:
            empty_dict['66 years'].append(age_list[key])
    return empty_dict

def counter_children_per_region(region_list, children_list):
    average_children= {}
    for key, region in enumerate(region_list):
        if region not in average_children:
            average_children[region] = [children_list[key]]
        elif region in average_children:
            average_children[region].append(children_list[key])
    for key in average_children:
        average_children[key] = sum(average_children[key])
    return average_children

#converting csv to dictionary:
with open('Codecademy/off-plataform-project/insurance.csv') as insurance_db:
    insurances = csv.DictReader(insurance_db)
    #formatting and separation of data
    for row in insurances:
        ages.append(int(row['age']))
        sex.append(row['sex'])
        bmi.append(float(row['bmi']))
        children.append(int(row['children']))
        smoker.append(row['smoker'])
        region.append(row['region'])
        charges.append(float(row['charges']))
        
#search database in python:
formated_dict = list_joint(ages, sex, bmi, children, smoker, region, charges)
print(formated_dict[7])

print()

#total patients per region:
total_patients_per_region = patients_per_region(region, ages)
for row in total_patients_per_region.items():
    print(f'The total os patients in the {row[0]} region is {len(row[-1])}')

print()

#total average
total = sum(charges) / len(charges)
print(f'AVG total: {total:.2f} USD')

print()

#average per region:
charge_per_region, charge_per_region_total = charge_region(region, charges)
for row in charge_per_region.items():
    print(f'The average charge in the {row[0]} area is {row[-1]:,.2f} USD')

print()

#total per region:
for row in charge_per_region_total.items():
    print(f'The total charge in the {row[0]} area is {row[-1]:,.2f} USD')

print()

#average age and average age per region:
average_age = avg_age(region, ages)
average_age_total = sum(ages) / len(ages)
print(f'The average age of all regions is {int(average_age_total)} years')

print()

counter_age = count_age(ages)
for row in counter_age.items():
    print(f'The total patients with {row[0]} is {len(row[-1])}')

print()

#cost by age:
cost_by_bmi = costs_age(ages, charges)
for row in cost_by_bmi.items():
    print(f'The total costs to {row[0]} years is {row[-1]:,.2f}')

print()

#patients with child:
number_children_per_region = counter_children_per_region(region, children)
counter_childs, age_of_childs = patients_w_child(children)
percentage_patients_w_children = (counter_childs * 100) / len(ages)
print(f'{counter_childs} registered patients have children, which represent {int(percentage_patients_w_children)}% of the total')
for child in age_of_childs.items():
    print(f'{child[0]}: {len(child[-1])} patients')
print()
for row in number_children_per_region.items():
    print(f'The number of children in the {row[0]} region is {row[-1]}')


print()

#smokers per region:
smokers_per_region = total_smokers(region, smoker)
smoker_total = 0
for row in smokers_per_region.items():
    smoker_total += len(row[-1])
print(f'The total number of smoking patients is {smoker_total}')
print()
for row in smokers_per_region.items():
    percentage_smokers = (len(row[-1]) * 100) / smoker_total
    print(f'The {row[0]} region has {len(row[-1])} registered smokers, which represent approximately {percentage_smokers:.2f}% of the total')

print()

#average bmi per region
average_bmi_per_region = avg_bmi_per_region(region, bmi)
for row in average_bmi_per_region.items():
    print(f'The average bmi in the {row[0]} area is {row[-1]:,.2f}')

print()

class_bmi = classification_bmi(bmi)
for bmi in class_bmi.items():
    print(f'{bmi[0]}: {len(bmi[-1])} patients')

