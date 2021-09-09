# Book Management
## Book Management is an application that helps users manage their book library. This application has the functions of adding, updating, editing and deleting books, besides it also helps users log in or log out of their accounts easily.
### Getting started with Book Management
### For a standard installation please follow the Setups.
##### 1.you need to have the IDE Visual Studio Code and python installed on your computer
**you can install it here , please select the version suitable for your computer to start the installation 
VSC : https://code.visualstudio.com/download
 and Python : https://www.python.org/** 
##### 2.Git 
The following requires git to be installed on your machine and that you have basic knowledge of git commands
`C:\> git clone https://github.com/NguyenTrieu903/Book`
##### 3.Python
During installation, check Add Python 3 to PATH, then click Customize Installation and make sure that pip is checked.
`C:\> python --version`
Verify also that pip is installed for this version.
`C:\> pip --version`
##### 4.PostgreSQL
 ##### Book Management uses PostgreSQL as database management system https://www.postgresql.org/download/ 
 **we need to create a new user and login with this username**
 - Open ***pgAdmin***
 - Double-click the server to create a connection.
 - Select ***Object*** ‣ ***Create*** ‣ ***Login/Group Role.***
 - Enter the username in the ***Role Name*** field.
 - Open the ***Definition*** tab and enter the password (e.g. odoo), then click ***Save.***
 - Open the ***Privileges*** tab and switch ***Can login?*** to `Yes` and ***Create database?*** to `Yes` . 
##### 5.Then start
- First , Find the folder where you just saved the file when you downloaded it on github. Then right click and choose ***open with Visual Studio Code*** . 
- Then find the `settings.py` in the Book folder , and then edit item again `DATBASES` according to the form below :
    ` 'ENGINE': 'django.db.backends.postgresql',`
    `'NAME': 'NameDB',` ***database name***
    `'USER': 'username',` ***user name***
    `'PASSWORD': '123',` ***password****
    `'HOST': 'localhost',`
- On ***Visual Studio Code*** select `Terminal` select` New terminal`
- Then `cd Book` , and then write `python manage.py runserver`
### You have successfully run the website, you can register for an account and use it normally

