# Chest-manager

Swiss Chest tournament manager  

> The script is a tournament manager in-line command  
> The database is stocked in ***db.json*** file  
> It's possible to generate a flake8 report

### Require repository

`git clone https://github.com/AlxandrV/Chest-manager.git ./`

### Create a virtual environnement

`python -m venv env`

### Execute virtual env

For Windows  

`source env/Scripts/activate`

For Linux  

`source env/bin/activate`

### Add requirements

`pip install -r requirements.txt`

#### Execute script

`python chest_manager.py`

### Generate report of flake8

1. Generate a report in directory ***flake-report***:  
`flake8 --format=html --htmldir=flake-report`
2. In directory ***flake-report*** open **index.html**