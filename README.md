"# Django_teaching_project" 
try to cover technical steps of all topics in django

INITIALIZATION:
    create a virtuanl env for django project using "virtualenv <envname>" or "python -m venv <envname>"
    
    activate virtualenv using <envname>\Scripts\activate

    then run to install necessary package in a single shot using requirements.txt(by adding all the libraries such as djano, mysqlclient...etc)by
    running "pip install -r requirements.txt"

    then calll "django-admin startproject <projectname>"

    once after we created the project get inside of project using "cd <project_name>"
    to run the server use "python manage.py runserver",
    to create app use "python manage.py startapp <appname>"
    to create a model use models.py with in the app we created
    once done with the model definition
    do "python manage.py makemigrations" create the sql query code files with the name of "migration__001.py"
    do "python manage.py migrate" which will execute the codes from the migrations files and create the tables in the connected database


GIT IGNORE TO SKIP THE VENV FILES:(steps)
    in your folder open the terminal and run "echo > .gitignore" and add the files which you don't want to push
    for ex: "django_course/"
     which is the env i don't want to pushe into git

    apart from that the file which you changed that much it will show on the staged files

THIRD PARTY DATABASE CONNECTION(mysql):
    run "pip install mysqlclient", in setting DATABASES dictionary key the name-dbname, user-root, password, host, port to configure

    before do migrations if you want to override inbuild user model do that by creating a app and in the model override in this project i did
    that in userapp model and also adding the config in settings such as "AUTH_USER_MODEL = "userapp.CustomUser" "

CREATING THE LOGIN, LOGOUT, SIGNUP VIEWS;
    these are django by default django provides us default forms and functions for this we used in this user app views which connected with forms 



"