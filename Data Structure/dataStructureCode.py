import requests
import json
import random as random


# In dataSourcesCode.py, I got the population data for the specific three states I wanted to use, and now I'm loading the data here.
with open('data_sources_file.json', 'r') as f:
    data = json.load(f)

# Build a tree based on the data from dataSourcesCode.py
class TreeNode():
    def __init__(self, value):
        self.value = value
        self.children = []
        self.populationdata = {}
        self.year = {}

class Tree:
    def __init__(self):
        self.root = TreeNode('Which year do you want to know the population of?')


tree = Tree()

# Add child nodes for 'Which year do you want to know the population of?'
year1 = TreeNode("year of 2000")
year2 = TreeNode("year of 2010")
year3 = TreeNode("year of 2020")
tree.root.children.append(year1)
tree.root.children.append(year2)
tree.root.children.append(year3)

# Add child nodes for 'year of 2000'
year1_c = TreeNode("California_2000")
year1_o = TreeNode("Ohio_2000")
year1_i = TreeNode("Indiana_2000")
tree.root.children.append(year1_c)
tree.root.children.append(year1_o)
tree.root.children.append(year1_i)
# Add population data for Callifornia_2000, Ohio_2000, and Indiana_2000
year1_c.populationdata.update({"Population for California": data["Total Population Counts in 2000"]["California"]})
year1_o.populationdata.update({"Population for Ohio": data["Total Population Counts in 2000"]["Ohio"]})
year1_i.populationdata.update({"Population for Indiana": data["Total Population Counts in 2000"]["Indiana"]})


# Add child nodes 'race' for 'Callifornia_2000, Ohio_2000, and Indiana_2000'
year1_c_r = TreeNode("Race_California_2000")
year1_o_r = TreeNode("Race_Ohio_2000")
year1_i_r = TreeNode("Race_Indiana_2000")
tree.root.children.append(year1_c_r)
tree.root.children.append(year1_o_r)
tree.root.children.append(year1_i_r)
# Add population data for Race_California_2000, Race_Ohio_2000, and Race_Indiana_2000
year1_c_r.populationdata.update({"White Group": data["White Group Population Counts in 2000"]["California"],
                                 "Black or Afican American Group":data["Black or African American Group Population Counts in 2000"]["California"],
                                 "American Indian and Alaska Native Group":data["American Indian and Alaska Native Group Population Counts in 2000"]["California"],
                                 "Asian Group": data["Asian Group Population Counts in 2000"]["California"],
                                 "Native Hawaiian and Other Pacific Islander": data["Native Hawaiian and Other Pacific Islander Group Population Counts in 2000"]["California"]})

year1_o_r.populationdata.update({"White Group": data["White Group Population Counts in 2000"]["Ohio"],
                                 "Black or Afican American Group":data["Black or African American Group Population Counts in 2000"]["Ohio"],
                                 "American Indian and Alaska Native Group":data["American Indian and Alaska Native Group Population Counts in 2000"]["Ohio"],
                                 "Asian Group": data["Asian Group Population Counts in 2000"]["Ohio"],
                                 "Native Hawaiian and Other Pacific Islander": data["Native Hawaiian and Other Pacific Islander Group Population Counts in 2000"]["Ohio"]})

year1_i_r.populationdata.update({"White Group": data["White Group Population Counts in 2000"]["Indiana"],
                                 "Black or Afican American Group":data["Black or African American Group Population Counts in 2000"]["Indiana"],
                                 "American Indian and Alaska Native Group":data["American Indian and Alaska Native Group Population Counts in 2000"]["Indiana"],
                                 "Asian Group": data["Asian Group Population Counts in 2000"]["Indiana"],
                                 "Native Hawaiian and Other Pacific Islander": data["Native Hawaiian and Other Pacific Islander Group Population Counts in 2000"]["Indiana"]})

# Add child nodes 'gender' for 'Callifornia_2000, Ohio_2000, and Indiana_2000'
year1_c_g = TreeNode("Gender_California_2000")
year1_o_g = TreeNode("Gender_Ohio_2000")
year1_i_g = TreeNode("Gender_Indiana_2000")
tree.root.children.append(year1_c_g)
tree.root.children.append(year1_o_g)
tree.root.children.append(year1_i_g)
# Add population data for Gender_California_2000, Gender_Ohio_2000, Gender_Indiana_2000
year1_c_g.populationdata.update({"Female Group": data["Total Female Group Population Counts in 2000"]["California"],
                                 "Male Group": data["Total Male Group Population Counts in 2000"]["California"]})

year1_o_g.populationdata.update({"Female Group": data["Total Female Group Population Counts in 2000"]["Ohio"],
                                 "Male Group": data["Total Male Group Population Counts in 2000"]["Ohio"]})

year1_i_g.populationdata.update({"Female Group": data["Total Female Group Population Counts in 2000"]["Indiana"],
                                 "Male Group": data["Total Male Group Population Counts in 2000"]["Indiana"]})

# Initial a new dictionary for tree printing
# Add all 2000's data into the dict
dict_2000= {}
dict_2000['Population size from a state perspective in 2000'] = {"California": year1_c.populationdata, "Ohio": year1_o.populationdata, "Indiana": year1_i.populationdata} 
dict_2000['Population size from a race perspective in 2000'] = {"California": year1_c_r.populationdata, "Ohio": year1_o_r.populationdata, "Indiana": year1_i_r.populationdata} 
dict_2000['Population size from a gender perspective in 2000'] = {"California": year1_c_g.populationdata, "Ohio": year1_o_g.populationdata, "Indiana": year1_i_g.populationdata} 
year1.populationdata.update({"Population for 2000": year1_i})

# Add child nodes for 'year of 2010'
year2_c = TreeNode("California_2010")
year2_o = TreeNode("Ohio_2010")
year2_i = TreeNode("Indiana_2010")
tree.root.children.append(year2_c)
tree.root.children.append(year2_o)
tree.root.children.append(year2_i)
# Add population data for Callifornia_2010, Ohio_2010, and Indiana_2010
year2_c.populationdata.update({"Population for California": data["Total Population Counts in 2010"]["California"]})
year2_o.populationdata.update({"Population for Ohio": data["Total Population Counts in 2010"]["Ohio"]})
year2_i.populationdata.update({"Population for Indiana": data["Total Population Counts in 2010"]["Indiana"]})

# Add child nodes 'race' for 'Callifornia_2010, Ohio_2010, and Indiana_2010'
year2_c_r = TreeNode("Race_California_2010")
year2_o_r = TreeNode("Race_Ohio_2010")
year2_i_r = TreeNode("Race_Indiana_2010")
tree.root.children.append(year2_c_r)
tree.root.children.append(year2_o_r)
tree.root.children.append(year2_i_r)
# Add population data for Race_California_2010, Race_Ohio_2010, and Race_Indiana_2010
year2_c_r.populationdata.update({"White Group": data["White Group Population Counts in 2010"]["California"],
                                 "Black or Afican American Group":data["Black or African American Group Population Counts in 2010"]["California"],
                                 "American Indian and Alaska Native Group":data["American Indian and Alaska Native Group Population Counts in 2010"]["California"],
                                 "Asian Group": data["Asian Group Population Counts in 2010"]["California"],
                                 "Native Hawaiian and Other Pacific Islander": data["Native Hawaiian and Other Pacific Islander Group Population Counts in 2010"]["California"]})

year2_o_r.populationdata.update({"White Group": data["White Group Population Counts in 2010"]["Ohio"],
                                 "Black or Afican American Group":data["Black or African American Group Population Counts in 2010"]["Ohio"],
                                 "American Indian and Alaska Native Group":data["American Indian and Alaska Native Group Population Counts in 2010"]["Ohio"],
                                 "Asian Group": data["Asian Group Population Counts in 2010"]["Ohio"],
                                 "Native Hawaiian and Other Pacific Islander": data["Native Hawaiian and Other Pacific Islander Group Population Counts in 2010"]["Ohio"]})

year2_i_r.populationdata.update({"White Group": data["White Group Population Counts in 2010"]["Indiana"],
                                 "Black or Afican American Group":data["Black or African American Group Population Counts in 2010"]["Indiana"],
                                 "American Indian and Alaska Native Group":data["American Indian and Alaska Native Group Population Counts in 2010"]["Indiana"],
                                 "Asian Group": data["Asian Group Population Counts in 2010"]["Indiana"],
                                 "Native Hawaiian and Other Pacific Islander": data["Native Hawaiian and Other Pacific Islander Group Population Counts in 2010"]["Indiana"]})

# Add child nodes 'gender' for 'Callifornia_2010, Ohio_2010, and Indiana_2010'
year2_c_g = TreeNode("Gender_California_2010")
year2_o_g = TreeNode("Gender_Ohio_2010")
year2_i_g = TreeNode("Gender_Indiana_2010")
tree.root.children.append(year2_c_g)
tree.root.children.append(year2_o_g)
tree.root.children.append(year2_i_g)
# Add population data for Gender_California_2010, Gender_Ohio_2010, Gender_Indiana_2010
year2_c_g.populationdata.update({"Female Group": data["Total Female Group Population Counts in 2010"]["California"],
                                 "Male Group": data["Total Male Group Population Counts in 2010"]["California"]})

year2_o_g.populationdata.update({"Female Group": data["Total Female Group Population Counts in 2010"]["Ohio"],
                                 "Male Group": data["Total Male Group Population Counts in 2010"]["Ohio"]})

year2_i_g.populationdata.update({"Female Group": data["Total Female Group Population Counts in 2010"]["Indiana"],
                                 "Male Group": data["Total Male Group Population Counts in 2010"]["Indiana"]})

# Initial a new dictionary for tree printing
# Add all 2010's data into the dict
dict_2010= {}
dict_2010['Population size from a state perspective in 2010'] = {"California": year2_c.populationdata, "Ohio": year2_o.populationdata, "Indiana": year2_i.populationdata} 
dict_2010['Population size from a race perspective in 2010'] = {"California": year2_c_r.populationdata, "Ohio": year2_o_r.populationdata, "Indiana": year2_i_r.populationdata} 
dict_2010['Population size from a gender perspective in 2010'] = {"California": year2_c_g.populationdata, "Ohio": year2_o_g.populationdata, "Indiana": year2_i_g.populationdata} 


# Add child nodes for 'year of 2020'
year3_c = TreeNode("California_2020")
year3_o = TreeNode("Ohio_2020")
year3_i = TreeNode("Indiana_2020")
tree.root.children.append(year3_c)
tree.root.children.append(year3_o)
tree.root.children.append(year3_i)
# Add population data for Callifornia_2020, Ohio_2020, and Indiana_2020
year3_c.populationdata.update({"Population for California": data["Total Population Counts in 2020"]["California"]})
year3_o.populationdata.update({"Population for Ohio": data["Total Population Counts in 2020"]["Ohio"]})
year3_i.populationdata.update({"Population for Indiana": data["Total Population Counts in 2020"]["Indiana"]})

# Add child nodes 'race' for 'Callifornia_2020, Ohio_2020, and Indiana_2020'
year3_c_r = TreeNode("Race_California_2020")
year3_o_r = TreeNode("Race_Ohio_2020")
year3_i_r = TreeNode("Race_Indiana_2020")
tree.root.children.append(year3_c_r)
tree.root.children.append(year3_o_r)
tree.root.children.append(year3_i_r)
# Add population data for Race_California_2020, Race_Ohio_2020, and Race_Indiana_2020
year3_c_r.populationdata.update({"White Group": data["White Group Population Counts in 2020"]["California"],
                                 "Black or Afican American Group":data["Black or African American Group Population Counts in 2020"]["California"],
                                 "American Indian and Alaska Native Group":data["American Indian and Alaska Native Group Population Counts in 2020"]["California"],
                                 "Asian Group": data["Asian Group Population Counts in 2020"]["California"],
                                 "Native Hawaiian and Other Pacific Islander": data["Native Hawaiian and Other Pacific Islander Group Population Counts in 2020"]["California"]})

year3_o_r.populationdata.update({"White Group": data["White Group Population Counts in 2020"]["Ohio"],
                                 "Black or Afican American Group":data["Black or African American Group Population Counts in 2020"]["Ohio"],
                                 "American Indian and Alaska Native Group":data["American Indian and Alaska Native Group Population Counts in 2020"]["Ohio"],
                                 "Asian Group": data["Asian Group Population Counts in 2020"]["Ohio"],
                                 "Native Hawaiian and Other Pacific Islander": data["Native Hawaiian and Other Pacific Islander Group Population Counts in 2020"]["Ohio"]})

year3_i_r.populationdata.update({"White Group": data["White Group Population Counts in 2020"]["Indiana"],
                                 "Black or Afican American Group":data["Black or African American Group Population Counts in 2020"]["Indiana"],
                                 "American Indian and Alaska Native Group":data["American Indian and Alaska Native Group Population Counts in 2020"]["Indiana"],
                                 "Asian Group": data["Asian Group Population Counts in 2020"]["Indiana"],
                                 "Native Hawaiian and Other Pacific Islander": data["Native Hawaiian and Other Pacific Islander Group Population Counts in 2020"]["Indiana"]})

# Add child nodes 'gender' for 'Callifornia_2010, Ohio_2010, and Indiana_2010'
year3_c_g = TreeNode("Gender_California_2010")
year3_o_g = TreeNode("Gender_Ohio_2010")
year3_i_g = TreeNode("Gender_Indiana_2010")
tree.root.children.append(year3_c_g)
tree.root.children.append(year3_o_g)
tree.root.children.append(year3_i_g)
# Add population data for Gender_California_2010, Gender_Ohio_2010, Gender_Indiana_2010
year3_c_g.populationdata.update({"Female Group": data["Total Female Group Population Counts in 2020"]["California"],
                                 "Male Group": data["Total Male Group Population Counts in 2020"]["California"]})

year3_o_g.populationdata.update({"Female Group": data["Total Female Group Population Counts in 2020"]["Ohio"],
                                 "Male Group": data["Total Male Group Population Counts in 2020"]["Ohio"]})


year3_i_g.populationdata.update({"Female Group": data["Total Female Group Population Counts in 2020"]["Indiana"],
                                 "Male Group": data["Total Male Group Population Counts in 2020"]["Indiana"]})

# Initial a new dictionary for tree printing
# Add all 2020's data into the dict
dict_2020= {}

dict_2020['Population size from a state perspective in 2020'] = {"California": year3_c.populationdata, "Ohio": year3_o.populationdata, "Indiana": year3_i.populationdata}
dict_2020['Population size from a race perspective in 2020'] = {"California": year3_c_r.populationdata, "Ohio": year3_o_r.populationdata, "Indiana": year3_i_r.populationdata} 
dict_2020['Population size from a gender perspective in 2020'] = {"California": year3_c_g.populationdata, "Ohio": year3_o_g.populationdata, "Indiana": year3_i_g.populationdata} 
dict = {}
dict = dict_2000 | dict_2010 | dict_2020


# Create a json cache to save the tree
json_cache = json.dumps(dict)
file = open("tree_structure_file.json", "w")
file.write(json_cache)
file.close() 
