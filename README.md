# Meeting-Bot

<h1 align = "center" > SumAction </h1>
<h3 align = "center" > Plan your week and get ahead of everyone! </h3>
<p align = "center" >
    <img title="SumAction" img src = "Resources/sumaction-logo.svg" alt = "SumAction" width = "300"/>
    </p>

## Executive Summary  

The **SumAction** AI Productivity tool analyzes your uploaded meeting notes (formats supported: text, video, audio) and uses AI to deliver a concise summary of the meetings, key learnings, along with a list of action items and a estimate of the task. The tool allows you to increase your productivity by taking care of the menial tasks of emailing attendees their specific tasks, giving you the opportunity to be more productive or just a rest from the daily rigmarole.

We leveraged OpenAI, its LLMs, and engineered prompts that were effective in creating our productivity tool to summarize uploaded meeting notes (Audio, Video, Text) and to extract action items.  

## Table of Contents  

- [Project Overview](#project-overview)  
  - [Project Requirements](#project-requirements)  
  - [Data Collection](#data-collection)  
  - [Data Analysis](#data-analysis)
  - [Identify Correlation](#identify-correlation)
- [Findings](#conclusion)
  - [Statistical Significance](#statistical-significance)
  - [Lessons Learned](#lessons-learned)
  - [Next Steps](#next-steps)  
- [Data Sources](#data-sources) 
- [Team Mambers](#team-members)
- [Presentation](#presentation)

## Project Overview  
  
The Lunar Madness project Team is investigating the urban legend that correlates erratic behavior when the moon is in its Full phase. By comparing moon phase data against reported crime and traffic data for multiple major metropolitan cities, the project seeks to determine if there is a statistically significant correlation. If a strong correlation is identified, this preliminay proof of concept could be used as a basis for future investigation.  Businesses and municipalities could benefit from the investigative work of the Lunar Madness Team to help inform optimized staffing levels, fleet preparations, and advising on supply inventories for public departments such as law enforcement, emergency services, and hospitals during specific lunar phases.

## Hypothesis
In research, there are two types of hypotheses: null (H0) and alternative (Ha). They work as a complementary pair, each stating that the other is wrong.

- *Null Hypothesis (H0)* – This can be thought of as the implied hypothesis. “Null” meaning “nothing.”  This hypothesis states that there is no difference between groups or no relationship between variables. The null hypothesis is a presumption of status quo or no change. In our case, H0 = The full moon does not influence behavior, full moon or other moon days will approximately display the same level of erratic behavior.

- *Alternative Hypothesis (Ha)* – This hypothesis should state what we expect the data to show, based on our research on the topic. This is also known as the claim and in our case, Ha = Full moon days will have a higher number of erratic behavior incidents in comparision to other moon days.

Erratic behavior is defined as "unpredictable, irregular, or inconsistent behavior that deviates from what is considered normal. It wan include mood swings, impulsive actions, and exaggerated emotional responses. Crime data and traffic violations datasets were used in our case as close analogies to represent erratic behavior. 

The Lunar Madness team sought to test the validity of the lunar lunacy effect by comparing crime data against full moon dates in 4 major metropolitan cities (Austin, Denver, Houston and Los Angeles) and traffic viloation across the entire the state of Maryland. If our hypothesis is true, we should see a higher volume of erratic behavior incidents, crime and traffic viloations, on days with a full moon.

## Project Requirements
Please review the 'requirements.txt' file in the Resources folder to get a complete overview of the entire set of libraries that are needed to run the program.
Use the single line to run the command within the Jyupter Notebook | [!pip install -r requirements.txt. ]
- **Software Requirements:**
  - [Python 3.12.9 or greater](https://www.python.org/)   
  - [Jupyter Notebook](https://jupyter.org/)
  - GitHub account   
  - Load Dependancies: 
    ```
    from langchain_openai import ChatOpenAI
    from dotenv import load_dotenv
    import os
    from langchain.agents import initialize_agent, load_tools
    from langchain.chains.llm import LLMChain
    from langchain_core.prompts import ChatPromptTemplate
    from langchain.docstore.document import Document
    from langchain.chains.summarize import load_summarize_chain
    from langchain_core.prompts import PromptTemplate
    import pandas as pd
    from datasets import load_dataset
    from openai import OpenAI
    from rouge import Rouge
    from rouge_score import rouge_scorer
    from pprint import pprint
    import nltk
    import evaluate
    import tiktoken
    from transformers import pipeline
    import matplotlib.pyplot as plt
    ```
- **GitHub Repository Structure:**
``` Markdown for Clean display of GitHub Repository Structure
  📦Meeting-Bot 
      ┣ 📂Nik_folder  (Project Notebooks: Summarizer, Action Extractor, Email Developer / Collector and MailAgent)
      ┣ 📂Zain_folder (Project Notebooks: Summarizer, Action Extractor, Evaluator, TaskEstimateBot, Q&A Query)
      ┣ 📂Resources (Meeting recordings, CommonTasks.csv) 
      ┣ 📜.utils.py
      ┣ 📜.gitignore
      ┣ 📜LICENSE 
      ┣ 📜README.md 
      ┗ 📜SumAction.svg
```
- **For Project Files, see:**
    - /Zain/Zain_meeting_ai_workspace.ipynb
    - /Nik/meeting_ai_workspace.ipynb

  
## Data Collection 
- (Also See [Data Sources](#data-sources))  
1. Public Meetings:  
    - Initial assessment conducted to understand the data and identify any issues
        - Read in each year from 2013-2024 and convert to a new DataFrame
        - Combined into Moon Phase DataFrame to be used for analysis 
        ![moon_data_export](Resources\combined_moon_data.png)
      
2. Zain's Meeting Notes:
    - Initial assess


## Data Analysis
- GOAL: Determine if there is a statistically significant correlation between moon phases and crime rates in sampled metropolitan areas (Chicago, Houston, Austin, Denver, Los Angeles, and Traffic in Baltimore)).
- Identify any specific crime types that may be more strongly influenced by the lunar cycle. Explore potential explanations for any observed correlations (e.g., increased visibility during full moon).

- Aggregation Example:  
![crime_count](Resources\crime_count.png)
- Comparison:  
![comparison_example](Resources/los_angeles_comparison.png)

## Visualizations  

- Plot of Los Angeles Crime Data by Day,
  Sliced data for 2020-2024
![la_plot](Resources/los_angeles_crime_plot.png)

- Full Moon Normalized
![Full Moon Normalized](Resources/full_moon_normalized.png)

- Full Moon Traffic Normalized
![Traffic Normalized](Resources/full_moon_traffic_plot.png)

- Outlier Crime Data
![outlier_crime_data](Resources/los_angeles_crime_outlier.png)
![outlier_example](Resources/outlier_query.png)



## Identify Correlation
No obvious statistical pattern identified.  Mean, Ratios, Statistical, Confidence Interval analyses all indicate a LOW to NO relationship between Erratic Behaviors (Crime & Traffic incidents) and Moon Phases.  Null Hypothesis proved:
Full Moon Crimes / Divided by / Other Moon Phase Crime rates found distinct tendencies towards ‘1.0.’  This indicates there is a LOW correlation in four of the five city/Moon phase datasets (and in the traffic/Moon phase dataset). Permutation tests indicate a 33% chance of erratic incidents when Moon phases are compared.
 


## Findings 
Outside of Denver, CO crime data displayed a hint of a relation (still not strong enough), the majority of our data results proved our H0, or Null, Hypothesis to be proven, i.e. NO RELATIONSHIP EXISTs between Full Moon and Erratic behavior. 
Multiple realtionship measurements were applied (Mean, Ratios, Statistical Significance, CI, P-value) across the dataset and each confirmed Full Moon days are just like any other moon days and do NOT dramatically influence or cause erratic behavior.  In this investigation, there was no significant correlation between in crime or automobile traffic incidents.

While at the higher level the Null Hypothesis proved, our disappointment was used as fuel to investigate deeper to see if any micro-influeces (eg. Type of Crime) were present. This is where we found it quite interesting to see that Murder Rate in Denver, CO was a little bit higher (2% increase) on Full Moon days vs. Other moon days.  Another interesting trend was a marked increase in Tresspassing violations during Full moon phases. 

## Lessons Learned
Obtaining Data that is accurate and reliable early on is important.  Authoratative public data can hold interesting patterns.  Data can have irregularities and data needs to be normalized.  Different types of statistical analyses, graphing and plotting reveal interesting patterns within the data.  Processing data files takes time and diligence to normalize as there are time zone, UTC and formatting issues to overcome.  Communicatiing roles and responsibilities with expected deliverable dates will help on future projects to best utilize resources.  Version control and using github can be a challenge; the .DSstore file from the Apple IOS proved to be problematic and 'dot ignore' file is mandatory at this level of programming.  

**Cost Of Project**
Using the following average Colorado salary scales for team member roles, we were able to calculate the cost of conducting this project. 
- Data Scientist (1): $104,771 | *(per week cost = $2014.82)*
- Data Engineer (2): $117,223 | *(per week cost = $2254.29)*
- Project Manager (1): $93,823 | *(per week cost = $1804.29)* 

Total Internal Cost for Conducting Analysis (2 weeks) = $16,655.38 

Having proven that there isn't a relationship that exists between Full Moons and Erratic Beahvior *(Crime/Traffic Violations)*, we hope to reach out to the **6000** 911 call centers, also known as Public Safety Answering Points [PSAs](https://health.wusf.usf.edu/health-news-florida/2024-07-18/the-nations-911-system-is-on-the-brink-of-its-own-emergency) that may be prone to overstaffing their call centers with additional resources to handle a percieved increase in erratic behavior, especially surrounding full moon days *(3 days: 1 day prior, day of full moon, 1 day after)* that are still percieved by many to be a full moon. 

**Tax Payer Savings**
Assume we save the need to overstaff just by a single dispatcher across the 3 days of percieved full moons *(3 days: 1 day prior, day of full moon, 1 day after)*  
- Average call center dispatcher makes [$18/hour](https://www.ziprecruiter.com/Salaries/Customer-Service-Dispatcher-Salary). 
    - We'd save tax payers around *~$486/person* for a single dispatcher working over the 3 days they plan to overstaff to handle the alledge additional call volume. 
- There are roughly **6000** [911 call Centers](https://health.wusf.usf.edu/health-news-florida/2024-07-18/the-nations-911-system-is-on-the-brink-of-its-own-emergency) in the US.
- 36 Alleged Full Moon days (12 actual Full Moons in a year. +/- 1 day surrounding the full moon)
- Savings of even 1 staff member across 36 Full Moon Days in a Year across 6000 PSAs could save the tax payers =  *$34,992,000*     *(12 x $486 x 6000 locations)*
  

## Next Steps:
If a organization, public or private, are willing to sponsor and provide authoratative raw data on local crime, traffic, 911, Emergency rooms and other first responder data, the Lunar Madness Team ("LM") could be contracted to combine the data and further refine this proof of concept template.  The LM framework includes moon phase data, and has several models to plug in local and regional data to uncover statistical correlations.  The Lunar Madness team will scour the data for high correlation events such as crime with other local events or phenomena, research is not limited to just moon phase data.  Set our team to the task of investigating revenue patterns, custom projects, or explore for unidentified trends.  Correlated information that leads to efficient management and can be predicted can make the difference between success vs. surviving.  Let us know the problem you wish to solve and we will do the analysys and presentation for you and your organization.

## Appendix
## Data Sources:
### Full Moon Data Sources:
- [National Weather Service](https://www.weather.gov/box/sunmoon)
 (National Oceanic and Atmospheric Administration)  
Data Points:  Daily moon phase information (e.g., new moon, full moon, first quarter, last quarter, percentage of illumination)  

- [US Naval Observatory Moon Phases](https://aa.usno.navy.mil/calculated/moon/phases?date=2024-01-10&nump=50&format=t&submit=Get+Data)  
Data Points:  Daily moon phase information (e.g., new moon, full moon, first quarter, last quarter)   

### Crime Data Sources:
- [US Government provided data](https://catalog.data.gov/dataset/?tags=crime)  
Data Points: Date and time of each reported crime incident, Crime type  

- [Los Angeles Crime Data](https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8/about_data)  
Data Points: Date and time of each reported crime incident, Crime type | 1004683 rows of data

- [Houston Crime Data](https://www.kaggle.com/datasets/iamkevin/raw-aggregate-houston-crime-report-data)  
Data Points: Date and time of each reported crime incident, Crime type | 1185476 rows of data 

- [Denver Crime Data](https://www.kaggle.com/code/paulo098/denver-crime-data-analysis-and-prediction)  
Data Points: Date and time of each reported crime incident, Crime type | 386867 rows of data 

- [Austin Crime Data](https://catalog.data.gov/dataset/crime-reports-bf2b7)  
Data Points: Date and time of each reported crime incident, Crime type | 2522587 rows of data

### Traffic Data Source
- [Maryland Traffic Data](https://data.montgomerycountymd.gov/Public-Safety/Traffic-Violations/4mse-ku6q/about_data)
Data Points: Date and time of each reported traffic violation, Violation type | 1048608 rows of data

## Team Members:  
Data Engineer: Sheila Mathews  
Data Analyst: Raymond Stover  
Data Scientist: Michael Brady  
Data Scientist: Zain Master  
