# Flask

Practicing the Frontend and Backend

Backend - Flask
Database - MySQL
Frontend - Html & Css

Creating Full Stack Website (Flask)

Setting up Required programs
-pip3 install requests ---> Use for getting requests
-python -m venv .venv ---> Creating Virtual enviroment

-source .venv/Scripts/activate = using git bash
-source .venv/bin/activate = using poweshell or cmd (Linux)

- . .venv\Scripts\Activate = for cmd or powershell windows

-pip3 install flask --> installing the flask for backend
-pip3 install flask-sqlalchemy --> For connecting to databases

Setting up the website...
terminal -->
export FLASK_APP=application.py
export FLASK_ENV=development
flask run --> To run the website

[For updating the database for changes use this]
pip install alembic
alembic init migrations

adds --> [migrations] Folder = [versions] folder, contains [env.py] ........
--> [alembic.ini] file

---

Naming Folders..

----------- BackEnd -------------
[bp] = Blueprint routes
[inventory] = Inventory Functions

[migration] = Work with updating changes in database
alembic.ini = for database updates
env.py = for database updates

[processor] = Contains Order Processor logic
[model] = Database tables

school_db.db = database
config.py = database configuration
extension.py = use for importing the sql alchemy flask
seed.py = for creating sample items only
check_tables.py = for vieweing tables in database

main.py = Main App Initializer

----------- FrontEnd -------------
[static] = contains Images

[templates] = contains html & css files
--> [category] = contains categories
--> home.html = Default first page
--> menu.html = Displaying category choices

[apife] = display for blueprints
