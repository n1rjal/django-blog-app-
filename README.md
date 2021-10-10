# django-blog-app

# :snowflake:Django Blog Web App:snowflake:
### **About** 
> A Blog app using django where a user  can logged in, comment , like comments and many more.

### **Features** 
+ Login Features.
+ Admin can update profile picture. :heart_eyes:, If you don't have one it will set the default one.
+ User can comment.
+ Like a comment:+1:, and the most liked one appears on the top.
+ Admin can login through facebook.

### **Manual Setup**
Firstly, create a new directory and change to it:

```bash
mkdir django-blog-app && cd blog_app1
```

Then, clone this repository to the current directory:

```bash
git clone https://github.com/Neeraj319/django-blog-app-.git
```

Next, one needs to setup database like SQLite or PostgreSQL on a local machine. This project uses PostgreSQL by default (see Django documentation for different setup). This process may vary from one OS to another, eg. on Arch Linux one can follow a straightforward guide here.

Next, set up a virtual environment and activate it:

```bash
python3 -m venv env && source env/bin/activate
```

The setup is complete. Run a local server with

```bash
python3 manage.py runserver --settings=website.settings.local
```

#### That's it !! Happy coding..
