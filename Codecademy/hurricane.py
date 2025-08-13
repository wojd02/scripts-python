#names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

def damage_conversion(damage_list):
    conversion = {"M": 1000000,
             "B": 1000000000}
    new_damage_list = []
    for damage in damage_list:
        if damage[-1] == 'M':
            damage = damage.replace('M', '')
            damage = float(damage) * conversion['M']
        elif damage[-1] == 'B':
            damage = damage.replace('B', '')
            damage = float(damage) * conversion['B']
        else:
            damage = damage
        new_damage_list.append(damage)
    return new_damage_list

def create_dictionary(list1, list2, list3, list4, list5, list6, list7):
    empty_dict = {}
    for index, name in enumerate(list1):
        empty_dict[name] = {'Name': list1[index], 'Month': list2[index], 'Year': list3[index], 'Max Sustained Wind': list4[index], 'Areas Affected': list5[index], 'Damage': list6[index], 'Deaths': list7[index]}
    return empty_dict

def create_dictionary_year(list1, list2, list3, list4, list5, list6, list7):
    empty_dict = {}
    for index, year in enumerate(list3):
        record = {'Name': list1[index], 'Month': list2[index], 'Max Sustained Wind': list4[index], 'Areas Affected': list5[index], 'Damage': list6[index], 'Deaths': list7[index]}
        if year not in empty_dict:
            empty_dict[year] = [record]
        elif year in empty_dict:
            empty_dict[year].append(record)
    return empty_dict

def count_affected_areas(list):
    empty_dict = {}
    for area in areas_affected:
        for local in area:
            if local not in empty_dict:
                empty_dict[local] = [local]
            elif local in empty_dict:
                empty_dict[local].append(local)
    empty_dict_2 = {}
    for key, area in empty_dict.items():
        empty_dict_2[key] = len(area)
    return empty_dict_2

def max_area_affected(dictionary):
    max_area = 0
    name_area = ''
    new_dictionary = {}
    for key, area in dictionary.items():
        if max_area == 0:
            max_area = area
            name_area = key
        elif max_area < area:
            max_area = area
            name_area = key
    new_dictionary[name_area] = max_area
    return new_dictionary

def max_counter_death(dictionary):
    count_deaths = 0
    name_of_hurricane = ''
    new_dictionary = {}
    for hurricane, values in dictionary.items():
        if count_deaths == 0:
            count_deaths = values['Deaths']
            name_of_hurricane = values['Name']
        elif count_deaths < values['Deaths']:
            count_deaths = values['Deaths']
            name_of_hurricane = values['Name']
    new_dictionary[name_of_hurricane] = {'Death': count_deaths}
    return new_dictionary

def death_metrics(dictionary):
    mortality_rating = 0
    new_dictionary = {}
    for hurricane, values in dictionary.items():
        if values['Deaths'] <= 100:
            mortality_rating = 1
            name_of_hurricane = values['Name']
            new_dictionary[mortality_rating]= values
        elif values['Deaths'] <= 500:
            mortality_rating = 2
            new_dictionary[mortality_rating]= values
        elif values['Deaths'] <= 1000:
            mortality_rating = 3
            new_dictionary[mortality_rating]= values
        elif values['Deaths'] <= 10000:
            mortality_rating = 4
            new_dictionary[mortality_rating]= values
        else:
            mortality_rating = 5
            new_dictionary[mortality_rating]= values
    return new_dictionary

def max_damage_hurricane(dictionary):
    most_damage = 0
    new_dictionary = {}
    name_of_hurricane = ''
    for hurricane, values in dictionary.items():
        if values['Damage'] == 'Damages not recorded':
            pass
        else:
            if most_damage == 0:
                most_damage = values['Damage']
                name_of_hurricane = values['Name']
            elif most_damage < values['Damage']:
                most_damage = values['Damage']
                name_of_hurricane = values['Name']
    new_dictionary[name_of_hurricane] = {'Damage': most_damage}
    return new_dictionary

def costs_metrics(dictionary):
    cost_rating = 0
    rating_by_damage = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for hurricane, values in dictionary.items():
        record = {'Name': values['Name'], 'Month': values['Month'], 'Max Sustained Wind': values['Max Sustained Wind'], 'Areas Affected': values['Areas Affected'], 'Damage': values['Damage'], 'Deaths': values['Deaths']}
        if values['Damage'] == 'Damages not recorded':
            cost_rating = 0
            rating_by_damage[cost_rating].append(record)
        else:
            if values['Damage'] <= 100000000:
                cost_rating = 1
                rating_by_damage[cost_rating].append(record)
            elif values['Damage'] <= 1000000000:
                cost_rating = 2
                rating_by_damage[cost_rating].append(record)
            elif values['Damage'] <= 10000000000:
                cost_rating = 3
                rating_by_damage[cost_rating].append(record)
            elif values['Damage'] <= 50000000000:
                cost_rating = 4
                rating_by_damage[cost_rating].append(record)
            else:
                cost_rating = 5
                rating_by_damage[cost_rating].append(record)
    return rating_by_damage

#converted damages
converted_list = damage_conversion(damages)
print(converted_list)
print()

#dictionary hurricanes
hurricane_info = create_dictionary(names, months, years, max_sustained_winds, areas_affected, converted_list, deaths)
print(hurricane_info)
print()

#dictionary hurricanes ordered by year
hurricane_info_year = create_dictionary_year(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
print(hurricane_info_year)
print()

#counting affected areas
counter_of_areas = count_affected_areas(areas_affected)
print(counter_of_areas)
print()

#most affected area
most_affected_area = max_area_affected(counter_of_areas)
print(most_affected_area)
print()

#deadliest hurricane
deaths_hurricane = max_counter_death(hurricane_info)
print(deaths_hurricane)
print()

#hurricane rating
hurricane_rating = death_metrics(hurricane_info)
print(hurricane_rating[5])
print()

#maximum damage
max_damage = max_damage_hurricane(hurricane_info)
print(max_damage)
print()

#cost rating
rating_costs = costs_metrics(hurricane_info)
print(rating_costs[5])
