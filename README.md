# django-blog-app-

<h1>:snowflake:Django Blog Web App:snowflake:</h1> 
<h3>**About**</h3><br>
> A Blog app using django where a user  can logged in, comment , like comments and many more.
<h3>**Features**</h3><br>
1. Login Features.<br>
2. Admin can update profile picture. :heart_eyes:, If you don't have one it will set the default one.<br>
3. User can comment.<br>
4. Like a comment:+1:, and the most liked one appears on the top.<br>
5 Admin can login through facebook .<br>
<h3>**Manual Setup**</h3>
Firstly, create a new directory and change to it:

<code>mkdir django-blog-app && cd blog_app1</code>

Then, clone this repository to the current directory:

<code>git clone https://github.com/Neeraj319/django-blog-app-.git</code>

Next, one needs to setup database like SQLite or PostgreSQL on a local machine. This project uses PostgreSQL by default (see Django documentation for different setup). This process may vary from one OS to another, eg. on Arch Linux one can follow a straightforward guide here.

Next, set up a virtual environment and activate it:

<code>python3 -m venv env && source env/bin/activate</code><br>
The setup is complete. Run a local server with

<code>python3 manage.py runserver --settings=website.settings.local</code>

<h4>That's it !! Happy coding..</h4>
