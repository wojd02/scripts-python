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

def charge_region(region_list, charge_list):
    charges_per_region = {}
    charges_per_region_2 = {}
    for key, region in enumerate(region_list):
        if region not in charges_per_region:
            charges_per_region[region] = [charge_list[key]]
        elif region in charges_per_region:
            charges_per_region[region].append(charge_list[key])
    for key in charges_per_region:
        charges_per_region_2[key] = sum(charges_per_region[key])
    for key in charges_per_region:
        charges_per_region[key] = sum(charges_per_region[key]) / len(charges_per_region[key])
    return charges_per_region, charges_per_region_2


#converting csv to dictionary
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
        
#search database in python
formated_dict = list_joint(ages, sex, bmi, children, smoker, region, charges)
print(formated_dict[0])

#total average
total = sum(charges) / len(charges)
print(f'AVG total: {total:.2f} USD')

#average per region
charge_per_region, charge_per_region_2 = charge_region(region, charges)
print(charge_per_region_2)
for row in charge_per_region.items():
    print(f'The average charge in the {row[0]} area is {row[-1]:,.2f} USD')