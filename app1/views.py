from django.shortcuts import render,HttpResponse  # type: ignore
from django.contrib.auth.models import User  #type:ignore
from django.contrib.auth import views as auth_views #type:ignore
from django.urls import path #type:ignore
import mysql.connector #type:ignore
from django.db import connection #type:ignore


# Create your views here.
def HomePage(request):
    return render(request,'home.html')

un=''
em=''
ps=''
cp1=''
def SignupPage(request):
    global un,em,ps,cp1
    if request.method=="POST":
        m=mysql.connector.connect(host="localhost",user="root",passwd="Anand@123",database='registration')
        cursor=m.cursor()
        un = request.POST.get('Username', '')  
        em = request.POST.get('Email', '')
        ps= request.POST.get('Password', '')
        cp1= request.POST.get('Confirm_Password', '')
        
        if ps==cp1:
           
           c="insert into analyst Values('{}','{}','{}','{}')".format(un,em,ps,cp1)
           cursor.execute(c)
           m.commit()
           return render(request, "welcome.html")
        else:

            return render(request, "passnotmatch.html")

        

    return render(request,'signup.html')
# Create your views here.

            




# Create your views here.
def LoginPage(request):
    if request.method == "POST":
        try:
            # Connect to the MySQL database
            m = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Anand@123",
                database='registration'
            )
            cursor = m.cursor()

            # Get username and password from the request
            username = request.POST.get('Username', '')
            password = request.POST.get('Password', '')

            # Use parameterized query to prevent SQL injection
            query = "SELECT * FROM analyst WHERE Username = %s AND Password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            # Check if the user exists
            if result:
                return render(request, "welcome.html")
            else:
                return render(request, "error.html")
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return render(request, "error.html", {"error_message": "Database connection error."})
        finally:
            # Close the database connection
            if m.is_connected():
                cursor.close()
                m.close()

    # Render the login page for GET request
    return render(request, 'login.html')


def Reviewer_SignupPage(request):
    global un,em,ps,cp1
    if request.method=="POST":
        m=mysql.connector.connect(host="localhost",user="root",passwd="Anand@123",database='registration')
        cursor=m.cursor()
        un = request.POST.get('Username', '')  
        em = request.POST.get('Email', '')
        ps= request.POST.get('Password', '')
        cp1= request.POST.get('Confirm_Password', '')
        
        if ps==cp1:
           
           c="insert into reviewer Values('{}','{}','{}','{}')".format(un,em,ps,cp1)
           cursor.execute(c)
           m.commit()
           return render(request, "welcome.html")
        else:

            return render(request, "passnotmatch.html")

        

    return render(request,'reviewer_signup.html')

def Reviewer_LoginPage(request):
    if request.method == "POST":
        try:
            # Connect to the MySQL database
            m = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Anand@123",
                database='registration'
            )
            cursor = m.cursor()

            # Get username and password from the request
            username = request.POST.get('Username', '')
            password = request.POST.get('Password', '')

            # Use parameterized query to prevent SQL injection
            query = "SELECT * FROM reviewer WHERE Username = %s AND Password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            # Check if the user exists
            if result:
                return render(request, "welcome.html")
            else:
                return render(request, "error.html")
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return render(request, "error.html", {"error_message": "Database connection error."})
        finally:
            # Close the database connection
            if m.is_connected():
                cursor.close()
                m.close()

    # Render the login page for GET request
    return render(request, 'reviewer_login.html')



def Controller_SignupPage(request):
    global un,em,ps,cp1
    if request.method=="POST":
        m=mysql.connector.connect(host="localhost",user="root",passwd="Anand@123",database='registration')
        cursor=m.cursor()
        un = request.POST.get('Username', '')  
        em = request.POST.get('Email', '')
        ps= request.POST.get('Password', '')
        cp1= request.POST.get('Confirm_Password', '')
        
        if ps==cp1:
           
           c="insert into controller Values('{}','{}','{}','{}')".format(un,em,ps,cp1)
           cursor.execute(c)
           m.commit()
           return render(request, "welcome.html")
        else:

            return render(request, "passnotmatch.html")

        
    return render(request,'controller_signup.html')

def Controller_LoginPage(request):
    if request.method == "POST":
        try:
            # Connect to the MySQL database
            m = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Anand@123",
                database='registration'
            )
            cursor = m.cursor()

            # Get username and password from the request
            username = request.POST.get('Username', '')
            password = request.POST.get('Password', '')

            # Use parameterized query to prevent SQL injection
            query = "SELECT * FROM controller WHERE Username = %s AND Password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            # Check if the user exists
            if result:
                return render(request, "welcome.html")
            else:
                return render(request, "error.html")
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return render(request, "error.html", {"error_message": "Database connection error."})
        finally:
            # Close the database connection
            if m.is_connected():
                cursor.close()
                m.close()

    # Render the login page for GET request
    return render(request, 'controller_login.html')



def Approver_SignupPage(request):
    global un,em,ps,cp1
    if request.method=="POST":
        m=mysql.connector.connect(host="localhost",user="root",passwd="Anand@123",database='registration')
        cursor=m.cursor()
        un = request.POST.get('Username', '')  
        em = request.POST.get('Email', '')
        ps= request.POST.get('Password', '')
        cp1= request.POST.get('Confirm_Password', '')
        
        if ps==cp1:
           
           c="insert into approver Values('{}','{}','{}','{}')".format(un,em,ps,cp1)
           cursor.execute(c)
           m.commit()
           return render(request, "welcome.html")
        else:

            return render(request, "passnotmatch.html")

        
    return render(request,'approver_signup.html')

def Approver_LoginPage(request):
    if request.method == "POST":
        try:
            # Connect to the MySQL database
            m = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Anand@123",
                database='registration'
            )
            cursor = m.cursor()

            # Get username and password from the request
            username = request.POST.get('Username', '')
            password = request.POST.get('Password', '')

            # Use parameterized query to prevent SQL injection
            query = "SELECT * FROM approver WHERE Username = %s AND Password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            # Check if the user exists
            if result:
                return render(request, "welcome.html")
            else:
                return render(request, "error.html")
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return render(request, "error.html", {"error_message": "Database connection error."})
        finally:
            # Close the database connection
            if m.is_connected():
                cursor.close()
                m.close()

    # Render the login page for GET request
    return render(request, 'approver_login.html')




def Admin_SignupPage(request):
    global un,em,ps,cp1
    if request.method=="POST":
        m=mysql.connector.connect(host="localhost",user="root",passwd="Anand@123",database='registration')
        cursor=m.cursor()
        un = request.POST.get('Username', '')  
        em = request.POST.get('Email', '')
        ps= request.POST.get('Password', '')
        cp1= request.POST.get('Confirm_Password', '')
        
        if ps==cp1:
           
           c="insert into admin Values('{}','{}','{}','{}')".format(un,em,ps,cp1)
           cursor.execute(c)
           m.commit()
           return render(request, "welcome.html")
        else:

            return render(request, "passnotmatch.html")

        

    return render(request,'admin_signup.html')

def Admin_LoginPage(request):
    if request.method == "POST":
        try:
            # Connect to the MySQL database
            m = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Anand@123",
                database='registration'
            )
            cursor = m.cursor()

            # Get username and password from the request
            username = request.POST.get('Username', '')
            password = request.POST.get('Password', '')

            # Use parameterized query to prevent SQL injection
            query = "SELECT * FROM admin WHERE Username = %s AND Password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            # Check if the user exists
            if result:
                return render(request, "welcome.html")
            else:
                return render(request, "error.html")
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return render(request, "error.html", {"error_message": "Database connection error."})
        finally:
            # Close the database connection
            if m.is_connected():
                cursor.close()
                m.close()

    # Render the login page for GET request
    return render(request, 'admin_login.html')


def Third_Page(request):
    return render(request,'thirdpage.html')

def authorizer(request):
    return render(request,'authorizer.html')

def fifthpage(request):
    return render(request,'fifthpage.html')