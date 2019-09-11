#usr/mxor111/Udacity item_catalog project

Item Catalog project:
An Udacity Full Stack Web Developer Nanodegree Project # 2 : Michele Novack

Project Description

In this project, you will be developing a web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users should have the ability to post, edit, and delete their own items.

You will be creating this project essentially from scratch, no templates have been provided for you. This means that you have free reign over the HTML, the CSS, and the files that include the application itself utilizing Flask.


Features:
- Proper authentication and authorization check
-Full CRUD support using SQLAlchemy and Flask
-JSON Endpoints
-Implements oAuth using google Sign-in API

PROJECT Structure:

- database_setup.py
- itemcatalog.db
- style.css
- README.md
- .HTMLfiles:
- .json file


Steps to Run this PROJECT

1. Download and install vagrant

2. Download and Install VirtualBox

3. Clone of download the vagrant VM Confirguation file from here
https://github.com/udacity/fullstack-nanodegree-vm

4. Open the above directory and navigate to the vagrant/ sub directory

5. Open terminal and type:
    vagrant up

6. Sign into vagrant: connect to new VM
    vagrant ssh

7. type cd /vagrant to go into shared directory

8. Download or clone this repository and navigate to it

9 install or upgrade Flask:

    sudo python3 -m pip install --upgrade flask

10. Set up the database:

    python3 database_set.py

11


12. Run Application

    python3 app.py

13 Open http://localhost:5000 in your favorite browser and have fun.

Known Issue:


Created: 
