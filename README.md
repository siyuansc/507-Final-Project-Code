# SI 507 - Final Project Overview
For my SI-507 final project, here are something you may want to know.

- Theme content 
  - The project focuses on three states, California (#1 in state GDP in 2020), Ohio (top 10 in state GDP in 2020 (#7)), and Indiana (top 20 or so in state GDP in 2020 (#17)), in particular from the three recent decennial censuses (2000, 2010, 2020) in terms of total population data and the distribution of data in terms of demographics, particularly race and gender.
  
- Special Instructions
	- My complete final project has about 500 lines of code. To facilitate reading and scoring, I split my complete code into three parts: the data source part, the data structure - tree part, and the interaction part, and put the code of them into three folders under this repo. 
	- I also created a new file called wholeCode, where you can see all my code and run it through VScode.
		 <br />(sourcesCode.py + treeCode.py + interactionCode.py = WholeCode -> my whole code)
	- In addition, the Web APIs I used require an API key to access, so I put the key I requested via email on the next line, and you can use my key to get to those pages.
	  <br />My API key is cc61b6e624d3712a35feef6ae9d586762f971d6c
<img width="1038" alt="image" src="https://user-images.githubusercontent.com/113861839/207991743-b96fe171-8b3c-4e3c-aac7-eeddf54acd89.png">

- Brief Description of how to interact with my program
  - Users can choose to view the distribution of population data from four perspectives: year, state, race, and gender.
  - The program first prompts the user with the perspective of how to approach the data and then types the data according to the user's choice. It is worth mentioning that you need to rerun the whole program if you want to look at the data from the state perspective after understanding the year perspective.

- Required Python package:
  - requests
