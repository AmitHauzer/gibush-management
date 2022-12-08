# Gibush management
# Installation Instructions
1. **Git clone.**
2. **Open vevn:**
	>     python -m venv venv
3. **Active venv:**
    >     ./venv/Scripts/active
5. **Install requirements:**
    >		pip list
    >		pip install -r requirements.txt
    >		pip list
 
6. **Migrations:**
    >		python manage.py makemigrations
    >		python manage.py migrate
    >		python manage.py createsuperuser
7.	**Launch up the server:** 
    >		python manage.py runserver
# Workflow
## Shalishut:
- **Add a Soldier**.
- **Enter an IDF number.**
  - IDF is the “username” of the soldier.
- **Update the soldier details**
	- Once you update, the soldier’s status changes to ‘Waiting for Clinic’.
## Clinic:
-	**Update:**
    - Unfit ---> File not required ---> The soldier stops the process, the status changes to ‘Medically disqualified'.
    -	Unfit ---> File not required ---> Continue, the status changes to 'Waiting for Baror'.
    - You can open the PDF.
## Baror:
-	**Add a round.**
-	**Edit round.** 
    - Add soldiers ---> Finish.
-	**Let’s go!**
    - Start
    - Press ‘Done’ when the soldier finishes the round.
    - You can view the round. 
## Commander:
-	**Chart & Tables.**
    - This page shows all the statuses and where the soldiers are now.
-	**Acceptance criteria.**
    - Select a number  Set.

## Models:
- **Soldier**
- **Shalishut**
- **Clinic**
- **BarOr**
- **BarorScore**


