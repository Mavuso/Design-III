# Design-III

To get started download NodeJS
  install npm
  Install express
  install firestore admin
  install bodyparse + other libraries.
Do not run any python script since the cred.js file on the NodeJS folder is a token with admin credential for servers side to query the DB
The .py file are for staging and loading the data file.
  insert_* file deal with data base insertions.
The Data_Process folder is the staging folder, the data_analysis.py script on that folder cleans the data and prepares it for database insertions.

The clean_data file is when the database insertion scripts look for file to insert.

run index.js and visit : 5000/wits_energy/ for the dashboard. 

if you really want to run the python scripts
