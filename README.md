# Global Shark Attacks _(Work in Progress)_

__*A data analysis of shark attacks records*__

*source : https://www.kaggle.com/teajay/global-shark-attacks*

## Description

### What
* This project intends to show a way of __*cleaning, exploring and visualizing*__ a kaggle dataset.
* Due to the messy dataset and the lack of previous knowledge of the subject, there will be no initial hypothesis. 
* Thus the final outcome of this work is expected to generate insights and hypothesis that could be tested in a future study.

### How
* The dataset manipulation and cleaning will be implemented on a jupyter notebook.
* The visualizations will be displayed using streamlit library.

### Why
* The biggest motivation of this work is to enhance my Python skills.

## Usage

### Requisite
In order to get the most value out of this analysis, visualizing graphs and using dynamic filters, streamlit library is a requisite.
So, for that you just neeed to execute:
```bash
pip install streamlit
```
__NOTE__: Currently (March 2021), there is an installation issue with Python 3.9 and Streamlit.  
* For a alternative method of installation other than downgrading python, see:  
_https://discuss.streamlit.io/t/note-installation-issues-with-python-3-9-and-streamlit/6946_  
* For another issues:  
_https://docs.streamlit.io/en/stable/troubleshooting/clean-install.html_

### Just Seeing Results
If all you want is to visualize the final result of this analysis and play with filters:

1- Create a folder in your Desktop area and name it as "SharkAttack"

2- Download the following files and save in the folder created:  
* Shark_ST.py _(visualization script)_  
* attacks.csv _(original dataset)_  
* db_attack.xlsx _(clean dataset)_  

3- Use command prompt to run:
```bash
streamlit run C:\Users\YOURUSERNAME\Desktop\SharkAttack\Shark_ST.py
```

4- Voilà! 

### The Whole Process
If you want to take a look at the data cleaning and understand the way we got here:

1- Run the jupyter-notebook script *__"SharkAttack"__*

3- Use command prompt to run:
```bash
streamlit run C:\Users\YOURUSERNAME\Desktop\SharkAttack\Shark_ST.py
```

## Next Steps

The analysis is at its early stage. The next steps for now are:

* Normalizing shark size to 'meters'(converting other unit measures).
* Relating fatality of attacks to shark size.
* Standarizing another classifications/columns to further analysis.
* Using a complementary database with more information about countries to enrich analysis. 

