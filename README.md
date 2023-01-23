# Gibush management
Welcome to the K-9 unit Gibush site.
Here you can find all you need to know about the candidates, their status and manage their process during the Gibush.
# Installation Instructions
1. **Git clone.**
2. **Open vevn:**
	>     python -m venv venv

3. **Active venv:**
    >     ./venv/Scripts/active

4. **Install requirements:**
    >		pip list
    >		pip install -r requirements.txt
    >		pip list
 
5. **Migrations:**
    >		python manage.py makemigrations
    >		python manage.py migrate
    >		python manage.py createsuperuser

6. **Launch up the server:** 
    >		python manage.py runserver
    
7. **Login to admin and create the groups:**
    - Shalishut.
    - ShalishutAdmin.
    - Clinic.
    - ClinicAdmin.
    - Baror.
    - Commander.


# Workflow
## Shalishut:
- **Add a Soldier**.
- **Enter an IDF number:**
  - IDF is the “username” of the soldier.
- **Update the soldier details:**
	- Once you update, the soldier’s status changes to ‘Waiting for Clinic’.

## Clinic:
-	**Update:**
    - Unfit ---> File is not required ---> The soldier stops the process, the status changes to ‘Medically disqualified'.
    - Fit ---> File is required ---> Continue, the status changes to 'Waiting for Baror'.
    - You can open the PDF.

## Baror:
-	**Add rounds.**
-	**Edit rounds:** 
    - Add soldiers ---> Finish.
-	**Let’s go!:**
    - Start.
    - Press ‘Done’ when the soldier finishes the round.
    - You can view the round. 

## Commander:
-	**Chart & Tables:**
    - This page shows all the statuses and where the soldiers are now.
-	**Acceptance criteria:**
    - Select a number ---> Set.
-	**Access to user management.**

## User Management:
- **Add users.**
- **Edit users.**
- **Active/Inactive users.**
- **Permissions.**

## Models:
- **Soldier**
- **Shalishut**
- **Clinic**
- **BarOr**
- **BarorScore**


