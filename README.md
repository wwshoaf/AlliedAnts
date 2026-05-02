# AlliedAnts
440 Project


Team:
- William Shoaf
- Lingjian Zheng
- Zachary Haufe
- Ashur Joseph

Tech Stack: 
- Languague: Python
- Framework: Flask
- Database: MySQL
- Database Tool: MySQL Workbench

Step 1:
- create database and user following configuration in db.py
DB_CONFIG = {
    "host": "localhost",
    "user": "allied_ant",
    "password": "AlliedAnts4321!",
    "database": "440_project"
}

Step 2: 
- Connect to the database
- Run SQL scripts in the following order:
1. sql/schema.sql
    - this makes the tables
2. sql/seed.sql
    - this adds values to the tables
3. sql/views.sql
    - this makes views for the tables
4. sql/procedures.sql
    - this makes the EnrollStudent() procedure
5. sql/indexes.sql
    - this makes an index for Teacher table

Step 3: 
- Make a venv and install dependencies
- Choose latest version of python for interpreter
- install dependencies from requirements.txt file
    - pip install -r requirements.txt

Step 4: 
- Run the application by executing app.py

Step 5:
- open in browser from the generated localhost link in your terminal


Project File structure:
AlliedAnts/
├─ modules/
│  ├─ classes.py # Person, Teacher, Customer CRUD
│  ├─ persons.py # Classes, Enrollment CRUD
│  ├─ reports.py # Sale CRUD
│  └─ sales.py   # Report queries
├─ sql/
│  ├─ indexes.sql    # index creation for number of classes taught
│  ├─ procedures.sql # stored procedure
│  ├─ schema.sql     # Create tables
│  ├─ seed_data.sql  # Add values to tables
│  └─ views.sql      # Database views
├─ static/
│  ├─ calm-aesthetic-desktop.jpg # background image
│  ├─ image (1).png              # background image
│  ├─ styles.css                 # formatting styles
│  ├─ yoga.png                   # background image
│  └─ yoga2.png                  # background image
├─ templates/
│  ├─ base.html         # shared layout
│  ├─ classes.html      # classes and enrollment
│  ├─ customers.html 
│  ├─ details.html      # 
│  ├─ index.html        # dashboard
│  ├─ reports.html  
│  ├─ sales.html
│  └─ teachers.html
├─ app.py # flask routes
├─ db.py  # database connection helper
├─ README.md
└─ requirements.txt # dependencies

