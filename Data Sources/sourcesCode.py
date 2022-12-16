import requests
import json
import random as random
from collections import Counter

### create a filter to seperate each states' population
def filter(pop_data):
    list1, list2, list3 = [], [], []
    for inner_list in pop_data:
        if 'California' in inner_list:
            list1.append(inner_list)
        if 'Ohio' in inner_list:
            list2.append(inner_list)
        if 'Indiana' in inner_list:
            list3.append(inner_list)
    wholeList = list1 + list2 + list3
    return wholeList

dictonary ={}

#### 2000 - Population for California, Ohio, and Indiana
url_2000 ="https://api.census.gov/data/2000/dec/sf1?get=P001001,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
popData_2000 = requests.get(url_2000).json()[0:1000]
wholeList_2000 = filter(popData_2000)
print("Population for California, Ohio, and Indiana in 2000:", "\n", wholeList_2000, "\n")
dictonary['Total Population Counts in 2000'] = {"California": wholeList_2000[0][0], "Ohio": wholeList_2000[1][0], "Indiana": wholeList_2000[2][0]}


## 2000 - Population Structure - Race
# White group
url_2000_white = "https://api.census.gov/data/2000/dec/sf1?get=P003003,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
white_pop = requests.get(url_2000_white).json()[0:1000]
wholeList_white1 = filter(white_pop)
print("Population of one race - <White> for California, Ohio, and Indiana in 2000:", "\n", wholeList_white1)
dictonary['White Group Population Counts in 2000'] = {"California": wholeList_white1[0][0], "Ohio": wholeList_white1[1][0], "Indiana": wholeList_white1[2][0]}

# Black or African American group
url_2000_black = "https://api.census.gov/data/2000/dec/sf1?get=P003004,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
black_pop = requests.get(url_2000_black).json()[0:1000]
wholeList_black1 = filter(black_pop)
print("Population of one race - <Black or African American> for California, Ohio, and Indiana in 2000:", "\n", wholeList_black1)
dictonary['Black or African American Group Population Counts in 2000'] = {"California": wholeList_black1[0][0], "Ohio": wholeList_black1[1][0], "Indiana": wholeList_black1[2][0]}

# American Indian and Alaska Native group
url_2000_native = "https://api.census.gov/data/2000/dec/sf1?get=P003005,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
native_pop = requests.get(url_2000_native).json()[0:1000]
wholeList_native1 = filter(native_pop)
print("Population of one race - <American Indian and Alaska Native> for California, Ohio, and Indiana in 2000:", "\n", wholeList_native1)
dictonary['American Indian and Alaska Native Group Population Counts in 2000'] = {"California": wholeList_native1[0][0], "Ohio": wholeList_native1[1][0], "Indiana": wholeList_native1[2][0]}

# Asian group
url_2000_asian = "https://api.census.gov/data/2000/dec/sf1?get=P003006,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
asian_pop = requests.get(url_2000_asian).json()[0:1000]
wholeList_asian1 = filter(asian_pop)
print("Population of one race - <Asian> for California, Ohio, and Indiana in 2000:", "\n", wholeList_asian1)
dictonary['Asian Group Population Counts in 2000'] = {"California": wholeList_asian1[0][0], "Ohio": wholeList_asian1[1][0], "Indiana": wholeList_asian1[2][0]}

# Native Hawaiian and Other Pacific Islander group
url_2000_pacificislander = "https://api.census.gov/data/2000/dec/sf1?get=P003007,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
pacificisander_pop = requests.get(url_2000_pacificislander).json()[0:1000]
wholeList_pacificisander1 = filter(pacificisander_pop)
print("Population of one race - <Native Hawaiian and Other Pacific Islander> for California, Ohio, and Indiana in 2000:", "\n", wholeList_pacificisander1, "\n")
dictonary['Native Hawaiian and Other Pacific Islander Group Population Counts in 2000'] = {"California": wholeList_pacificisander1[0][0], "Ohio": wholeList_pacificisander1[1][0], "Indiana": wholeList_pacificisander1[2][0]}


## 2000 - Population Structure - Gender
# Female group
url_2000_female = "https://api.census.gov/data/2000/dec/sf1?get=P012026,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
female_pop = requests.get(url_2000_female).json()[0:1000]
wholeList_female1 = filter(female_pop)
print("Population of <female> for California, Ohio, and Indiana in 2000:", "\n", wholeList_female1)
dictonary['Total Female Group Population Counts in 2000'] = {"California": wholeList_female1[0][0], "Ohio": wholeList_female1[1][0], "Indiana": wholeList_female1[2][0]}

# Male group
url_2000_male = "https://api.census.gov/data/2000/dec/sf1?get=P012002,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
male_pop = requests.get(url_2000_male).json()[0:1000]
wholeList_male1 = filter(male_pop)
print("Population of <male> for California, Ohio, and Indiana in 2000:", "\n", wholeList_male1, "\n")
dictonary['Total Male Group Population Counts in 2000'] = {"California": wholeList_male1[0][0], "Ohio": wholeList_male1[1][0], "Indiana": wholeList_male1[2][0]}



#### 2010 - Population for California, Ohio, and Indiana
url_2010 = "https://api.census.gov/data/2010/dec/sf1?get=P001001,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
popData_2010 = requests.get(url_2010).json()[0:100]
wholeList_2010 = filter(popData_2010)
print("Population for California, Ohio, and Indiana in 2010:", "\n", wholeList_2010, "\n")
dictonary['Total Population Counts in 2010'] = {"California": wholeList_2010[0][0], "Ohio": wholeList_2010[1][0], "Indiana": wholeList_2010[2][0]}


## 2010 - Population Structure - Race
# White group
url_2010_white = "https://api.census.gov/data/2010/dec/sf1?get=P003002,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
white_pop = requests.get(url_2010_white).json()[0:1000]
wholeList_white2 = filter(white_pop)
print("Population of one race - <White> for California, Ohio, and Indiana in 2010:", "\n", wholeList_white2)
dictonary['White Group Population Counts in 2010'] = {"California": wholeList_white2[0][0], "Ohio": wholeList_white2[1][0], "Indiana": wholeList_white2[2][0]}

# Black or African American group
url_2010_black = "https://api.census.gov/data/2010/dec/sf1?get=P003003,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
black_pop = requests.get(url_2010_black).json()[0:1000]
wholeList_black2 = filter(black_pop)
print("Population of one race - <Black or African American> for California, Ohio, and Indiana in 2010:", "\n", wholeList_black2)
dictonary['Black or African American Group Population Counts in 2010'] = {"California": wholeList_black2[0][0], "Ohio": wholeList_black2[1][0], "Indiana": wholeList_black2[2][0]}

# American Indian and Alaska Native group
url_2010_native = "https://api.census.gov/data/2010/dec/sf1?get=P003004,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
native_pop = requests.get(url_2010_native).json()[0:1000]
wholeList_native2 = filter(native_pop)
print("Population of one race - <American Indian and Alaska Native> for California, Ohio, and Indiana in 2010:", "\n", wholeList_native2)
dictonary['American Indian and Alaska Native Group Population Counts in 2010'] = {"California": wholeList_native2[0][0], "Ohio": wholeList_native2[1][0], "Indiana": wholeList_native2[2][0]}

# Asian group
url_2010_asian = "https://api.census.gov/data/2010/dec/sf1?get=P003005,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
asian_pop = requests.get(url_2010_asian).json()[0:1000]
wholeList_asian2 = filter(asian_pop)
print("Population of one race - <Asian> for California, Ohio, and Indiana in 2010:", "\n", wholeList_asian2)
dictonary['Asian Group Population Counts in 2010'] = {"California": wholeList_asian2[0][0], "Ohio": wholeList_asian2[1][0], "Indiana": wholeList_asian2[2][0]}

# Native Hawaiian and Other Pacific Islander group
url_2010_pacificislander = "https://api.census.gov/data/2010/dec/sf1?get=P003006,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
pacificisander_pop = requests.get(url_2010_pacificislander).json()[0:1000]
wholeList_pacificisander2 = filter(pacificisander_pop)
print("Population of one race - <Native Hawaiian and Other Pacific Islander> for California, Ohio, and Indiana in 2010:", "\n", wholeList_pacificisander2, "\n")
dictonary['Native Hawaiian and Other Pacific Islander Group Population Counts in 2010'] = {"California": wholeList_pacificisander2[0][0], "Ohio": wholeList_pacificisander2[1][0], "Indiana": wholeList_pacificisander2[2][0]}


# 2010 - Population Structure - Gender
# Female group
url_2010_female = "https://api.census.gov/data/2010/dec/sf1?get=P012026,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
female_pop = requests.get(url_2010_female).json()[0:1000]
wholeList_female2 = filter(female_pop)
print("Population of <female> for California, Ohio, and Indiana in 2010:", "\n", wholeList_female2)
dictonary['Total Female Group Population Counts in 2010'] = {"California": wholeList_female2[0][0], "Ohio": wholeList_female2[1][0], "Indiana": wholeList_female2[2][0]}

# Male group
url_2010_male = "https://api.census.gov/data/2010/dec/sf1?get=P012002,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
male_pop = requests.get(url_2010_male).json()[0:1000]
wholeList_male2 = filter(male_pop)
print("Population of <male> for California, Ohio, and Indiana in 2010:", "\n", wholeList_male2, "\n")
dictonary['Total Male Group Population Counts in 2010'] = {"California": wholeList_male2[0][0], "Ohio": wholeList_male2[1][0], "Indiana": wholeList_male2[2][0]}



#### 2020 - Population for California, Ohio, and Indiana
url_2020 = "https://api.census.gov/data/2020/acs/acs5?get=B01003_001E,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
popData_2020 = requests.get(url_2020).json()[0:1000]
wholeList_2020 = filter(popData_2020)
print("Population for California, Ohio, and Indiana in 2020:", "\n", wholeList_2020, "\n")
dictonary['Total Population Counts in 2020'] = {"California": wholeList_2020[0][0], "Ohio": wholeList_2000[1][0], "Indiana": wholeList_2020[2][0]}


## 2020 - Population Structure - Race
# White group
url_2020_white = "https://api.census.gov/data/2020/dec/pl?get=P1_003N,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
white_pop = requests.get(url_2020_white).json()[0:1000]
wholeList_white3 = filter(white_pop)
print("Population of one race - <White> for California, Ohio, and Indiana in 2020:", "\n", wholeList_white3)
dictonary['White Group Population Counts in 2020'] = {"California": wholeList_white3[0][0], "Ohio": wholeList_white3[1][0], "Indiana": wholeList_white3[2][0]}

# Black or African American group
url_2020_black = "https://api.census.gov/data/2020/dec/pl?get=P1_004N,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
black_pop = requests.get(url_2020_black).json()[0:1000]
wholeList_black3 = filter(black_pop)
print("Population of one race - <Black or African American> for California, Ohio, and Indiana in 2020:", "\n", wholeList_black3)
dictonary['Black or African American Group Population Counts in 2020'] = {"California": wholeList_black3[0][0], "Ohio": wholeList_black3[1][0], "Indiana": wholeList_black3[2][0]}

# American Indian and Alaska Native group
url_2020_native = "https://api.census.gov/data/2020/dec/pl?get=P1_005N,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
native_pop = requests.get(url_2020_native).json()[0:1000]
wholeList_native3 = filter(native_pop)
print("Population of one race - <American Indian and Alaska Native> for California, Ohio, and Indiana in 2020:", "\n", wholeList_native3)
dictonary['American Indian and Alaska Native Group Population Counts in 2020'] = {"California": wholeList_native3[0][0], "Ohio": wholeList_native3[1][0], "Indiana": wholeList_native3[2][0]}

# Asian group
url_2020_asian = "https://api.census.gov/data/2020/dec/pl?get=P1_006N,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
asian_pop = requests.get(url_2020_asian).json()[0:1000]
wholeList_asian3 = filter(asian_pop)
print("Population of one race - <Asian> for California, Ohio, and Indiana in 2010:", "\n", wholeList_asian3)
dictonary['Asian Group Population Counts in 2020'] = {"California": wholeList_asian3[0][0], "Ohio": wholeList_asian3[1][0], "Indiana": wholeList_asian3[2][0]}

# Native Hawaiian and Other Pacific Islander group
url_2020_pacificislander = "https://api.census.gov/data/2020/dec/pl?get=P1_007N,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
pacificisander_pop = requests.get(url_2020_pacificislander).json()[0:1000]
wholeList_pacificisander3 = filter(pacificisander_pop)
print("Population of one race - <Native Hawaiian and Other Pacific Islander> for California, Ohio, and Indiana in 2020:", "\n", wholeList_pacificisander3, "\n")
dictonary['Native Hawaiian and Other Pacific Islander Group Population Counts in 2020'] = {"California": wholeList_pacificisander3[0][0], "Ohio": wholeList_pacificisander3[1][0], "Indiana": wholeList_pacificisander3[2][0]}


## 2020 - Population Structure - Gender
url_2020_female = "https://api.census.gov/data/2020/acs/acs5?get=B01001_026E,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
female_pop = requests.get(url_2020_female).json()[0:1000]
wholeList_female3 = filter(female_pop)
print("Population of <female> for California, Ohio, and Indiana in 2020:", "\n", wholeList_female3)
dictonary['Total Female Group Population Counts in 2020'] = {"California": wholeList_female3[0][0], "Ohio": wholeList_female3[1][0], "Indiana": wholeList_female3[2][0]}

# Male group
url_2020_male = "https://api.census.gov/data/2020/acs/acs5?get=B01001_002E,NAME&for=state:*&key=cc61b6e624d3712a35feef6ae9d586762f971d6c"
male_pop = requests.get(url_2020_male).json()[0:1000]
wholeList_male3 = filter(male_pop)
print("Population of <male> for California, Ohio, and Indiana in 2020:", "\n", wholeList_male3, "\n")
dictonary['Total Male Group Population Counts in 2020'] = {"California": wholeList_male3[0][0], "Ohio": wholeList_male3[1][0], "Indiana": wholeList_male3[2][0]}



### create a json cache
json_cache = json.dumps(dictonary)
file = open("final_cache_file.json", "w")
file.write(json_cache)
file.close()
