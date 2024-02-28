# csv maker

Requirements:
- python3 
- poetry package manager

# Initialize the tool
Clone the repo and cd into the root directory.

    git clone git@github.com:deancochran/dummy_data_csv_maker.git

Run the following command:
    poetry install

Then start the virtual enviornment with 
    poetry shell

Run the jupyter lab session from your terminal with 
    jupyter lab

# Open the notebook.py file
Jupyter Notebooks contain indiviual cells of python that may be run OUT of order. 
The state of each cell is maintained, so running the cells in order is the only way to keep the tool running

# Configuration
There are some variables you may configure and change to build a csv file of devleopment data

- n = the number of rows to output
- reuired_columns = the number of columns required for the output file
- column_names = the name of each of the columns (note that each column will have it's index value attached to the end of the name)
- column_types = the type of the column (see ColumnType in generator.py) for each corresponding column name 

# Ouput
The output of each successful run of the notebook with result in a new .csv file titled

    output/
        fake_data_02-28-24_18:45:22.csv