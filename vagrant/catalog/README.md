ITEM-CATALOG Project - Udacity 9.6.19

#Project Description

In this project, you will be developing a web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users should have the ability to post, edit, and delete their own items.

You will be creating this project essentially from scratch, no templates have been provided for you. This means that you have free reign over the HTML, the CSS, and the files that include the application itself utilizing Flask.


1. In this sample project, the homepage displays all current categories with the latest added items.
2. Selecting a specific category shows you all the items available for that category.
3.Selecting a specific item shows you specific information about that item.
4. After logging in, a user has the ability to add, update, or delete item information. Users should be able to modify only those items that they themselves have created.

The application should provide a JSON endpoint at the very least.



Getting Started

1. Install Vagrant and VirtualBox
2. Clone the fullstack-nanodegree-vm repository. (There is a catalog folder provided for you, but no files have been included.)
3. Launch the Vagrant VM (by typing vagrant up in the directory fullstack/vagrant from the terminal).
4. Write the Flask application locally in the /vagrant/catalog directory (which will automatically be synced to /vagrant/catalog within the VM). Name it application.py.
5. Run your application within the VM by typing python /vagrant/catalog/application.py into the Terminal.
6. Access and test your application by visiting http://localhost:8000 locally on your browser.

Create Files:  

1. HTML (structure of the pages)
2. CSS (the style of the pages)
3. Flask Application (to put it online) it must include authentication/authorization to allow users to login before making changes
4. Database (to store and organize the information)

#CONTENTS
.vagrant(folder) - containing components for running vagrant file
pg_config.sh - script for installing compnents environment
Vagrantfile - configuations file for Vagrant
Catalog(folder):
  - database_setup.py - creates the sqlite database using sqlalchemy
  - populate_database.py - populates the datatbase with some cample projects
  - sample_data(folder) contains csv files used to populate_databa.py
  - application.py - contain flask Application
  - static(folder) - contains cdd, javascript and fonts used by bootstrap for sytling
  - templates (folder) contains HTML templates which are render by Flask
  - layout-sidebar.html - shared template for pages that display the sidebar
  -layout-form.html - used to share template for pafed with forms
-uploads(folder) folder where photos are uploaded to -contains images used in porject

#Creating database_setup
 To create the database with sqLite run:

 python database_setup.py

#Populate Examples:
  To prepopulate the database with examples project run:

 python populate_database.py

#Running application

To Start Flask  application run

python application.py

Then open the web browser and go to

http://locahost:8080
