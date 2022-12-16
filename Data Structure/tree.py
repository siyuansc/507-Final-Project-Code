#### load json file created in the data sources part
f = open('final_cache_file.json')
data = json.load(f)

#### build a tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.populationdata = {}

class Tree:
    def __init__(self):
        self.root = TreeNode('Which year do you want to know the population of?')

tree = Tree()

# add child nodes for the years 2000, 2010, and 2020
year1 = TreeNode("year of 2000")
year2 = TreeNode("year of 2010")
year3 = TreeNode("year of 2020")
tree.root.children.append(year1)
tree.root.children.append(year2)
tree.root.children.append(year3)

# add child nodes for the year of 2000
year1_c = TreeNode("California_2000")
year1_o = TreeNode("Ohio_2000")
year1_i = TreeNode("Indiana_2000")
tree.root.children.append(year1_c)
tree.root.children.append(year1_o)
tree.root.children.append(year1_i)

# add population data for California_2000, Ohio_2000, and Indiana_2000
year1_c.populationdata.update({"Population for California": wholeList_2000[0][0]})
year1_o.populationdata.update({"Population for California": wholeList_2000[1][0]})
year1_i.populationdata.update({"Population for California": wholeList_2000[2][0]})

# add child nodes for California_2000, Ohio_2000, and Indiana_2000 ->race
year1_c_r = TreeNode("Race_California_2000")
year1_o_r = TreeNode("Race_Ohio_2000")
year1_i_r = TreeNode("Race_Indiana_2000")
tree.root.children.append(year1_c_r)
tree.root.children.append(year1_o_r)
tree.root.children.append(year1_i_r)

# add population data for each race of California_2000, Ohio_2000, and Indiana_2000
year1_c_r.populationdata.update({"White Group": wholeList_white1[0][0],"Black or Afican American Group": wholeList_black1[0][0],
                               "American Indian and Alaska Native Group": wholeList_native1[0][0], "Asian Group": wholeList_asian1[0][0],
                               "Native Hawaiian and Other Pacific Islander": wholeList_pacificisander1[0][0]})
year1_o_r.populationdata.update({"White Group": wholeList_white1[1][0],"Black or Afican American Group": wholeList_black1[1][0],
                               "American Indian and Alaska Native Group": wholeList_native1[1][0], "Asian Group": wholeList_asian1[1][0],
                               "Native Hawaiian and Other Pacific Islander": wholeList_pacificisander1[1][0]})
year1_i_r.populationdata.update({"White Group": wholeList_white1[2][0],"Black or Afican American Group": wholeList_black1[2][0],
                               "American Indian and Alaska Native Group": wholeList_native1[2][0], "Asian Group": wholeList_asian1[2][0],
                               "Native Hawaiian and Other Pacific Islander": wholeList_pacificisander1[2][0]})

# add child nodes for California_2000, Ohio_2000, and Indiana_2000 ->gender
year1_c_g = TreeNode("Gender_California_2000")
year1_o_g = TreeNode("Gender_Ohio_2000")
year1_i_g = TreeNode("Gender_Indiana_2000")
tree.root.children.append(year1_c_g)
tree.root.children.append(year1_o_g)
tree.root.children.append(year1_i_g)

# add population data for each gender of California_2000, Ohio_2000, and Indiana_2000
year1_c_g.populationdata.update({"Female Group": wholeList_female1[0][0], "Male Group": wholeList_male1[0][0]})
year1_o_g.populationdata.update({"Female Group": wholeList_female1[1][0], "Male Group": wholeList_male1[1][0]})
year1_i_g.populationdata.update({"Female Group": wholeList_female1[2][0], "Male Group": wholeList_male1[2][0]})


# add child nodes for the year of 2010
year2_c = TreeNode("California_2010")
year2_o = TreeNode("Ohio_2010")
year2_i = TreeNode("Indiana_2010")
tree.root.children.append(year2_c)
tree.root.children.append(year2_o)
tree.root.children.append(year2_i)

# add population data for California_2010, Ohio_2010, and Indiana_2010
year2_c.populationdata.update({"Population for California": wholeList_2010[0][0]})
year2_o.populationdata.update({"Population for Ohio": wholeList_2010[1][0]})
year2_i.populationdata.update({"Population for Indiana": wholeList_2010[2][0]})

# add child nodes for California_2010, Ohio_2010, and Indiana_2010 ->race
year2_c_r = TreeNode("Race_California_2010")
year2_o_r = TreeNode("Race_Ohio_2010")
year2_i_r = TreeNode("Race_Indiana_2010")
tree.root.children.append(year2_c_r)
tree.root.children.append(year2_o_r)
tree.root.children.append(year2_i_r)

# add population data for each race of California_2010, Ohio_2010, and Indiana_2010
year2_c_r.populationdata.update({"White Group": wholeList_white2[0][0],"Black or Afican American Group": wholeList_black2[0][0],
                               "American Indian and Alaska Native Group": wholeList_native2[0][0], "Asian Group": wholeList_asian2[0][0],
                               "Native Hawaiian and Other Pacific Islander": wholeList_pacificisander2[0][0]})
year2_o_r.populationdata.update({"White Group": wholeList_white2[1][0],"Black or Afican American Group": wholeList_black2[1][0],
                               "American Indian and Alaska Native Group": wholeList_native2[1][0], "Asian Group": wholeList_asian2[1][0],
                               "Native Hawaiian and Other Pacific Islander": wholeList_pacificisander2[1][0]})
year2_i_r.populationdata.update({"White Group": wholeList_white2[2][0],"Black or Afican American Group": wholeList_black2[2][0],
                               "American Indian and Alaska Native Group": wholeList_native2[2][0], "Asian Group": wholeList_asian2[2][0],
                               "Native Hawaiian and Other Pacific Islander": wholeList_pacificisander2[2][0]})

# add child nodes for California_2010, Ohio_2010, and Indiana_2010 ->gender
year2_c_g = TreeNode("Gender_California_2010")
year2_o_g = TreeNode("Gender_Ohio_2010")
year2_i_g = TreeNode("Gender_Indiana_2010")
tree.root.children.append(year2_c_g)
tree.root.children.append(year2_o_g)
tree.root.children.append(year2_i_g)

# add population data for each gender of California_2010, Ohio_2010, and Indiana_2010
year2_c_g.populationdata.update({"Female Group": wholeList_female2[0][0], "Male Group": wholeList_male2[0][0]})
year2_o_g.populationdata.update({"Female Group": wholeList_female2[1][0], "Male Group": wholeList_male2[1][0]})
year2_i_g.populationdata.update({"Female Group": wholeList_female2[2][0], "Male Group": wholeList_male2[2][0]})


# add child nodes for the year of 2020
year3_c = TreeNode("California_2020")
year3_o = TreeNode("Ohio_2020")
year3_i = TreeNode("Indiana_2020")
tree.root.children.append(year3_c)
tree.root.children.append(year3_o)
tree.root.children.append(year3_i)

# add population data for California_2000, Ohio_2000, and Indiana_2000
year3_c.populationdata.update({"Population for California": wholeList_2020[0][0]})
year3_o.populationdata.update({"Population for Ohio": wholeList_2020[1][0]})
year3_i.populationdata.update({"Population for Indiana": wholeList_2020[2][0]})

# add child nodes for California_2020, Ohio_2020, and Indiana_2020 ->race
year3_c_r = TreeNode("Race_California_2020")
year3_o_r = TreeNode("Race_Ohio_2020")
year3_i_r = TreeNode("Race_Indiana_2020")
tree.root.children.append(year3_c_r)
tree.root.children.append(year3_o_r)
tree.root.children.append(year3_i_r)

# add population data for each race of California_2020, Ohio_2020, and Indiana_2020
year3_c_r.populationdata.update({"White Group": wholeList_white3[0][0],"Black or Afican American Group": wholeList_black3[0][0],
                               "American Indian and Alaska Native Group": wholeList_native3[0][0], "Asian Group": wholeList_asian3[0][0],
                               "Native Hawaiian and Other Pacific Islander": wholeList_pacificisander3[0][0]})
year3_o_r.populationdata.update({"White Group": wholeList_white3[1][0],"Black or Afican American Group": wholeList_black3[1][0],
                               "American Indian and Alaska Native Group": wholeList_native3[1][0], "Asian Group": wholeList_asian3[1][0],
                               "Native Hawaiian and Other Pacific Islander": wholeList_pacificisander3[1][0]})
year3_i_r.populationdata.update({"White Group": wholeList_white3[2][0],"Black or Afican American Group": wholeList_black3[2][0],
                               "American Indian and Alaska Native Group": wholeList_native3[2][0], "Asian Group": wholeList_asian3[2][0],
                               "Native Hawaiian and Other Pacific Islander": wholeList_pacificisander3[2][0]})

# add child nodes for California_2020, Ohio_2020, and Indiana_2020 ->gender
year3_c_g = TreeNode("Gender_California_2010")
year3_o_g = TreeNode("Gender_Ohio_2010")
year3_i_g = TreeNode("Gender_Indiana_2010")
tree.root.children.append(year3_c_g)
tree.root.children.append(year3_o_g)
tree.root.children.append(year3_i_g)

# add population data for each gender of California_2020, Ohio_2020, and Indiana_2020
year3_c_g.populationdata.update({"Female Group": wholeList_female3[0][0], "Male Group": wholeList_male3[0][0]})
year3_o_g.populationdata.update({"Female Group": wholeList_female3[1][0], "Male Group": wholeList_male3[1][0]})
year3_i_g.populationdata.update({"Female Group": wholeList_female3[2][0], "Male Group": wholeList_male3[2][0]})
