# SI 507 - Final Project Overview
For my SI-507 final project, here are something you may want to know.

- Theme content 
  - The project focuses on the population data from three states, California (#1 in state GDP in 2020), Ohio (top 10 in state GDP in 2020 (#7)), and Indiana (top 20 or so in state GDP in 2020 (#17)), in three recent decennial censuses (2000, 2010, 2020). Analyses are conducted primarily around population distribution regarding the years, state, and demographics, especially race and gender.
  
- Special Instructions
	- My complete final project is divided into three parts, they are data source part, data structure-tree part, and interaction part. So I created three folders under this repo, and put the code of each part into each folder. You can use VSCode to run each part's code separately, and they can all be run with no bug. In addition, I also uploaded the json file generated by dataSourcesCode.py and the json generated by the dataStructureCode.py to the corresponding folder.
	- In addition, the Web APIs I used require an API key to access, so I put the key I requested via email on the next line, and you can use my key to get to those pages.
	  <br />My API key is cc61b6e624d3712a35feef6ae9d586762f971d6c
<img width="1038" alt="image" src="https://user-images.githubusercontent.com/113861839/207991743-b96fe171-8b3c-4e3c-aac7-eeddf54acd89.png">

- Brief Description of how to interact with my program
  - Users can choose to view or not view a pop-up URL link direct to the miro to get an overview of how my program is arranged.
  - Users can choose to view the distribution of population data from four perspectives: year, state, race, and gender.
  - The program prompts the user with the perspective of how to approach the data and then types the data according to the user's choice. It is worth mentioning that you need to rerun the whole program if you want to look at the data from the state perspective after understanding the year perspective.

- Required Python package:
  - import requests
  - from json2txttree import json2txttree 
  (use 'pip install json2txttree' in the terminal first)
  - import webbrowser
