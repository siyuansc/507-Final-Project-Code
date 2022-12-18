import json
from json2txttree import json2txttree
import webbrowser

with open('tree_structure_file.json', 'r') as f:
    dataset = json.load(f)

def interaction():
    print("Welcome to my final project - U.S. Demographic Data Analysis! This project focuses on the population "
          "data of California, Ohio, and Indiana in the three decadal censuses (2000, 2010, 2020)")

    ques = input("Before we start, do you wanna get a overview of how this interaction arranged? Type 'yes' or 'no': ")
    if ques == "yes":
        url = "https://miro.com/app/board/uXjVP5ZHRYg=/"
        webbrowser.open(url)
    elif ques == "no":
        print("Okay, let's get rid of that.")
    else:
        print("Please enter a valid yes or no!")

    startq = input("First, please type whether you want to know the demographic data in terms of year, or state, or race, or gender: ")

    if startq == "year":
        secq = input("Please enter the year you want to know, 2000, 2010, or 2020: ")
        if secq == "2000":
            print("The total population for California, Ohio, and Indiana are listed below: ", "\n", 
                  dataset["Population size from a state perspective in 2000"]["California"],
                  dataset["Population size from a state perspective in 2000"]["Ohio"], 
                  dataset["Population size from a state perspective in 2000"]["Indiana"])
        elif secq == "2010":
            print("The total population for California, Ohio, and Indiana are listed below: ", "\n", 
                  dataset["Population size from a state perspective in 2010"]["California"],
                  dataset["Population size from a state perspective in 2010"]["Ohio"], 
                  dataset["Population size from a state perspective in 2010"]["Indiana"])
        elif secq == "2020":
            print("The total population for California, Ohio, and Indiana are listed below: ", "\n", 
                  dataset["Population size from a state perspective in 2020"]["California"],
                  dataset["Population size from a state perspective in 2020"]["Ohio"], 
                  dataset["Population size from a state perspective in 2020"]["Indiana"])
        else:
            print("Please enter a valid element!")

    elif startq == "state":
        secq = input("Please enter the state you want to know, California, Ohio, or Indiana: ")
        if secq == "California":
            print("The total population for California in 2000, 2010, and 2020 are listed below: ", "\n",
                  "2000: ", dataset["Population size from a state perspective in 2000"]["California"]["Population for California"],
                  "     2010: ", dataset["Population size from a state perspective in 2010"]["California"]["Population for California"],
                  "     2020: ", dataset["Population size from a state perspective in 2020"]["California"]["Population for California"])
        elif secq == "Ohio":
            print("The total population for Ohio in 2000, 2010, and 2020 are listed below: ", "\n", 
                  "2000: ", dataset["Population size from a state perspective in 2000"]["Ohio"]["Population for Ohio"],
                  "     2010: ", dataset["Population size from a state perspective in 2010"]["Ohio"]["Population for Ohio"],
                  "     2020: ", dataset["Population size from a state perspective in 2020"]["Ohio"]["Population for Ohio"])
        elif secq == "Indiana":
            print("The total population for Indiana in 2000, 2010, and 2020 are listed below: ", "\n", 
                  "2000: ", dataset["Population size from a state perspective in 2000"]["Indiana"]["Population for Indiana"],
                  "     2010: ", dataset["Population size from a state perspective in 2010"]["Indiana"]["Population for Indiana"],
                  "     2020: ", dataset["Population size from a state perspective in 2020"]["Indiana"]["Population for Indiana"])
        else:
            print("Please enter a valid element!")

    elif startq == "race":
            secq = input("Please enter the race you want to know, White Group, Black or Afican American Group, "
                         "American Indian and Alaska Native Group, Asian Group, Native Hawaiian and Other Pacific Islander:")

            if secq == "White":
                print("The total population for <White> Group in 2000, 2010, and 2020 from <California> are listed below:", "\n",
                      dataset["Population size from a race perspective in 2000"]["California"]["White Group"],
                      dataset["Population size from a race perspective in 2010"]["California"]["White Group"],
                      dataset["Population size from a race perspective in 2020"]["California"]["White Group"])
                print ("The total population for <White> Group in 2000, 2010, and 2020 from <Ohio> are listed below: ", "\n",
                      dataset["Population size from a race perspective in 2000"]["Ohio"]["White Group"],
                      dataset["Population size from a race perspective in 2010"]["Ohio"]["White Group"],
                      dataset["Population size from a race perspective in 2020"]["Ohio"]["White Group"])
                print("The total population for <White> Group in 2000, 2010, and 2020 from <Indiana> are listed below: ", "\n",
                      dataset["Population size from a race perspective in 2000"]["Indiana"]["White Group"],
                      dataset["Population size from a race perspective in 2010"]["Indiana"]["White Group"],
                      dataset["Population size from a race perspective in 2020"]["Indiana"]["White Group"])

            elif secq == "Black or Afican American":
                print("The total population for <Black or Afican American> Group in 2000, 2010, and 2020 from <California> are listed below:", "\n",
                      dataset["Population size from a race perspective in 2000"]["California"]["Black or Afican American Group"],
                      dataset["Population size from a race perspective in 2010"]["California"]["Black or Afican American Group"],
                      dataset["Population size from a race perspective in 2020"]["California"]["Black or Afican American Group"])
                print("The total population for <Black or Afican American> Group in 2000, 2010, and 2020 from <Ohio> are listed below: ", "\n",
                      dataset["Population size from a race perspective in 2000"]["Ohio"]["Black or Afican American Group"],
                      dataset["Population size from a race perspective in 2010"]["Ohio"]["Black or Afican American Group"],
                      dataset["Population size from a race perspective in 2020"]["Ohio"]["Black or Afican American Group"])
                print("The total population for <Black or Afican American> Group in 2000, 2010, and 2020 from <Indiana> are listed below: ","\n",
                      dataset["Population size from a race perspective in 2000"]["Indiana"]["Black or Afican American Group"],
                      dataset["Population size from a race perspective in 2010"]["Indiana"]["Black or Afican American Group"],
                      dataset["Population size from a race perspective in 2020"]["Indiana"]["Black or Afican American Group"])

            elif secq == "American Indian and Alaska Native":
                print("The total population for <American Indian and Alaska Native> Group in 2000, 2010, and 2020 from <California> are listed below:", "\n",
                      dataset["Population size from a race perspective in 2000"]["California"]["American Indian and Alaska Native Group"],
                      dataset["Population size from a race perspective in 2010"]["California"]["American Indian and Alaska Native Group"],
                      dataset["Population size from a race perspective in 2020"]["California"]["American Indian and Alaska Native Group"])
                print ("The total population for <American Indian and Alaska Native> Group in 2000, 2010, and 2020 from <Ohio> are listed below: ", "\n",
                      dataset["Population size from a race perspective in 2000"]["Ohio"]["American Indian and Alaska Native Group"],
                      dataset["Population size from a race perspective in 2010"]["Ohio"]["American Indian and Alaska Native Group"],
                      dataset["Population size from a race perspective in 2020"]["Ohio"]["American Indian and Alaska Native Group"])
                print("The total population for <American Indian and Alaska Native> in 2000, 2010, and 2020 from <Indiana> are listed below: ", "\n",
                      dataset["Population size from a race perspective in 2000"]["Indiana"]["American Indian and Alaska Native Group"],
                      dataset["Population size from a race perspective in 2010"]["Indiana"]["American Indian and Alaska Native Group"],
                      dataset["Population size from a race perspective in 2020"]["Indiana"]["American Indian and Alaska Native Group"])

            elif secq == "Asian":
                print("The total population for <Asian> Group in 2000, 2010, and 2020 from <California> are listed below:", "\n",
                      dataset["Population size from a race perspective in 2000"]["California"]["Asian Group"],
                      dataset["Population size from a race perspective in 2010"]["California"]["Asian Group"],
                      dataset["Population size from a race perspective in 2020"]["California"]["Asian Group"])
                print ("The total population for <Asian> Group in 2000, 2010, and 2020 from <Ohio> are listed below: ", "\n",
                      dataset["Population size from a race perspective in 2000"]["Ohio"]["Asian Group"],
                      dataset["Population size from a race perspective in 2010"]["Ohio"]["Asian Group"],
                      dataset["Population size from a race perspective in 2020"]["Ohio"]["Asian Group"])
                print("The total population for <Asian> Group in 2000, 2010, and 2020 from <Indiana> are listed below: ", "\n",
                      dataset["Population size from a race perspective in 2000"]["Indiana"]["Asian Group"],
                      dataset["Population size from a race perspective in 2010"]["Indiana"]["Asian Group"],
                      dataset["Population size from a race perspective in 2020"]["Indiana"]["Asian Group"])

            elif secq == "Native Hawaiian and Other Pacific Islander":
                print("The total population for <Native Hawaiian and Other Pacific Islander> Group in 2000, 2010, and 2020 from <California> are listed below:", "\n",
                      dataset["Population size from a race perspective in 2000"]["California"]["Native Hawaiian and Other Pacific Islander"],
                      dataset["Population size from a race perspective in 2010"]["California"]["Native Hawaiian and Other Pacific Islander"],
                      dataset["Population size from a race perspective in 2020"]["California"]["Native Hawaiian and Other Pacific Islander"])
                print ("The total population for <Native Hawaiian and Other Pacific Islander> Group in 2000, 2010, and 2020 from <Ohio> are listed below: ", "\n",
                      dataset["Population size from a race perspective in 2000"]["Ohio"]["Native Hawaiian and Other Pacific Islander"],
                      dataset["Population size from a race perspective in 2010"]["Ohio"]["Native Hawaiian and Other Pacific Islander"],
                      dataset["Population size from a race perspective in 2020"]["Ohio"]["Native Hawaiian and Other Pacific Islander"])
                print("The total population for <Native Hawaiian and Other Pacific Islander> Group in 2000, 2010, and 2020 from <Indiana> are listed below: ", "\n",
                      dataset["Population size from a race perspective in 2000"]["Indiana"]["Native Hawaiian and Other Pacific Islander"],
                      dataset["Population size from a race perspective in 2010"]["Indiana"]["Native Hawaiian and Other Pacific Islander"],
                      dataset["Population size from a race perspective in 2020"]["Indiana"]["Native Hawaiian and Other Pacific Islander"])

            else:
                print("Please enter a valid element and re-run!")

    elif startq == "gender":
            secq = input("Please enter the gender you want to know, female, or male :")
            if secq == "female":
                print("The total population of female for California in 2000, 2010, and 2020 are listed below:", "\n",
                     dataset["Population size from a gender perspective in 2000"]["California"]["Female Group"],
                     dataset["Population size from a gender perspective in 2010"]["California"]["Female Group"],
                     dataset["Population size from a gender perspective in 2020"]["California"]["Female Group"])
                print("The total population of female for Ohio in 2000, 2010, and 2020 are listed below:", "\n",
                     dataset["Population size from a gender perspective in 2000"]["Ohio"]["Female Group"],
                     dataset["Population size from a gender perspective in 2010"]["Ohio"]["Female Group"],
                     dataset["Population size from a gender perspective in 2020"]["Ohio"]["Female Group"])
                print("The total population of female for Indiana in 2000, 2010, and 2020 are listed below:", "\n",
                     dataset["Population size from a gender perspective in 2000"]["Indiana"]["Female Group"],
                     dataset["Population size from a gender perspective in 2010"]["Indiana"]["Female Group"],
                     dataset["Population size from a gender perspective in 2020"]["Indiana"]["Female Group"])

            elif secq == "male":
                print("The total population of male for California in 2000, 2010, and 2020 are listed below:", "\n",
                     dataset["Population size from a gender perspective in 2000"]["California"]["Male Group"],
                     dataset["Population size from a gender perspective in 2010"]["California"]["Male Group"],
                     dataset["Population size from a gender perspective in 2020"]["California"]["Male Group"])
                print("The total population of male for Ohio in 2000, 2010, and 2020 are listed below:", "\n",
                     dataset["Population size from a gender perspective in 2000"]["Ohio"]["Male Group"],
                     dataset["Population size from a gender perspective in 2010"]["Ohio"]["Male Group"],
                     dataset["Population size from a gender perspective in 2020"]["Ohio"]["Male Group"])
                print("The total population of male for Indiana in 2000, 2010, and 2020 are listed below:", "\n",
                     dataset["Population size from a gender perspective in 2000"]["Indiana"]["Male Group"],
                     dataset["Population size from a gender perspective in 2010"]["Indiana"]["Male Group"],
                     dataset["Population size from a gender perspective in 2020"]["Indiana"]["Male Group"])
            else:
                print("Please enter a valid element and re-run!")
    else:
        print("Please enter a valid element and re-run!")

    thiq = input("I do bulid a tree graph in text mode, do you wanna see it?")
    if thiq == "yes":
        print(json2txttree(dataset))
    elif thiq == "no":
        print("Okay..")
    else:
        print("Please enter yes or no!")

    print("Bye!")

interaction()


