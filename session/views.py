from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from session.models import Users
from session.models import Administrator

def login(request):
    message = '''<html>
                    <head>
                        <style>
                            body {
                                margin: 0;
                                padding: 0;
                            }

                            .container {
                                position: relative;
                                width: 100%;
                            }

                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <form name="submit_form" id="submit_form" action="/career/doLogin/" method="post">
                                <table border="1" style="width: 400px; margin-left: auto; margin-right: auto; margin-top: 30px;" cellpadding="8" cellspacin="8">
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Username
                                        </td>
                                        <td>
                                            <input type="text" name="username" value="" placeholder="Please enter username." style="width: 100%; height: 30px;" />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Password
                                        </td>
                                        <td>
                                            <input type="password" name="password" value="" placeholder="Please enter password." style="width: 100%; height: 30px;" />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            &nbsp;
                                        </td>
                                        <td>
                                            <input type="button" value="Cancel" />
                                            <input type="submit" value="Submit" />
                                        </td>
                                    </tr>
                                </table>
                            </form>
                        </div>
                    </body>
                </html>'''

    return HttpResponse (message)

@csrf_exempt
def doLogin(request):
    if request.method == "POST":
        _username = request.POST.get("username", "")
        _password = request.POST.get("password", "")

        # print _username
        # print _password

        row = Administrator.objects.filter(username=_username, password=_password)
        admin = None

        if not row:
            return HttpResponseRedirect('/career/login/')
        else:
            admin = row[0]

        print (admin.username)
        print (admin.password)

        request.session['username'] = admin.username

    return HttpResponseRedirect('/career/')
    # return HttpResponse ('xxxxx')

def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/career/login/')
    # return HttpResponseRedirect('/career/')


# Create your views here.
#from models import Users
def index(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('/career/login/')
    else:
        print (request.session['username'])
        message = '''<html>
                    <head>
                        <style>
                            body {
                                margin: 0;
                                padding: 0;
                            }

                            .container {
                                position: relative;
                                width: 100%;
                            }

                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <div style="text-align: center;">
                                Hi '''+request.session['username']+''' | <a href="/career/logout">Logout</a>
                            </div>
                            <form name="submit_form" id="submit_form" action="/career/showdata/" method="post">
                                <table border="1" style="width: 400px; margin-left: auto; margin-right: auto; margin-top: 30px;" cellpadding="8" cellspacin="8">
                                    <tr>
                                    	<td style="width: 30%; text-align: center;">
                                    		First Name
                                    	</td>
                                    	<td>
                                    		<input type="text" name="firstName" value="" placeholder="Please enter firstname." style="width: 100%; height: 30px;" />
                                    	</td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Last Name
                                        </td>
                                        <td>
                                            <input type="text" name="lastName" value="" placeholder="Please enter lastname." style="width: 100%; height: 30px;" />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Middle Name
                                        </td>
                                        <td>
                                            <input type="text" name="midName" value="" placeholder="Please enter middle name." style="width: 100%; height: 30px;" />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Gender
                                        </td>
                                        <td>
                                            <input type="radio" name="gender" value="m" checked /> Male
                                            <br />
                                            <input type="radio" name="gender" value="f" /> Female
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Date of birth
                                        </td>
                                        <td>
                                            <input type="text" name="dateOfBirth" value="" placeholder="Please enter date of birth." style="width: 100%; height: 30px;" />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            &nbsp;
                                        </td>
                                        <td>
                                            <input type="button" value="Cancel" />
                                            <input type="submit" value="Submit" />
                                        </td>
                                    </tr>
                                </table>
                            </form>
                        </div>
                    </body>
                </html>'''

        return HttpResponse (message)

@csrf_exempt
def showdata (request):
    if request.method == "POST":
        firstName = request.POST.get("firstName", "")
        lastName = request.POST.get("lastName", "")
        midName = request.POST.get("midName", "")
        gender = request.POST.get("gender", "")
        dateOfBirth = request.POST.get("dateOfBirth", "")
        print (firstName)
        print (lastName)
        print (midName)
        print (gender)
        print (dateOfBirth)

        # with connection.cursor() as cursor:
            # cursor.execute("INSERT INTO person (firstname, lastname, middlename, gender, dateofB) VALUES (%s, %s, %s, %s, %s)", (firstName, lastName, midName, gender, dateOfBirth))

        user = Users.objects.create(firstname=firstName, lastname=lastName, middlename=midName, gender=gender, dateofB=dateOfBirth)
        user.save()
        # cursor.execute("DELETE FROM login_users where id= %s", user_id)

        # row = cursor.fetchone()


    return HttpResponseRedirect('/career/select/')

def select (request):

    user = ''
    for row in Users.objects.raw('SELECT * FROM person'):
        print(row.id)
        print(row.firstname)
        print(row.lastname)
        print(row.middlename)
        print(row.gender)
        print(row.dateofB)
        user += '''
                <tr>
                    <td>'''+str(row.id)+'''</td>
                    <td>'''+row.firstname+'''</td>
                    <td>'''+row.lastname+'''</td>
                    <td>'''+row.middlename+'''</td>
                    <td>'''+row.gender+'''</td>
                    <td>'''+row.dateofB+'''</td>
                    <td><a href="/career/update/?id='''+str(row.id)+'''">Update</a></td>
                    <td><a href="/career/delete/?id='''+str(row.id)+'''">Delete</a></td>
                </tr>
                '''

    # print user

    message = """<html>
                    <head>
                        <style>
                            body {
                                margin: 0;
                                padding: 0;
                            }

                            .container {
                                position: relative;
                                width: 100%;
                            }

                        </style>
                    </head>
                    <body>
                        <div style="text-align: center;">
                            Hi """+request.session['username']+""" | <a href="/career/logout">Logout</a>
                        </div>
                        <div class="container">
                            <table border="1" width="800" style="margin-left: auto; margin-right: auto; margin-top: 30px;">
                                """+user+"""
                            </table>
                        </div>
                    </body>
                </html>"""

    # message = 'xxxx'

    return HttpResponse(message)

def update(request):
    _id = request.GET.get('id','')

    row = Users.objects.filter(id=_id)
    person = row[0]
    maleSelected = ''
    if person.gender == 'm':
        maleSelected = 'checked'

    femaleSelected = ''
    if person.gender == 'f':
        femaleSelected = 'checked'

    message = '''<html>
                    <head>
                        <style>
                            body {
                                margin: 0;
                                padding: 0;
                            }

                            .container {
                                position: relative;
                                width: 100%;
                            }

                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <div style="text-align: center;">
                                Hi '''+request.session['username']+''' | <a href="/career/logout">Logout</a>
                            </div>
                            <form name="submit_form" id="submit_form" action="/career/doUpdate/" method="post">
                                <input type="hidden" name="id" value="'''+str(person.id)+'''" />
                                <table border="1" style="width: 400px; margin-left: auto; margin-right: auto; margin-top: 30px;" cellpadding="8" cellspacin="8">
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            First Name
                                        </td>
                                        <td>
                                            <input type="text" name="firstName" value="'''+person.firstname+'''" placeholder="Please enter firstname." style="width: 100%; height: 30px;" />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Last Name
                                        </td>
                                        <td>
                                            <input type="text" name="lastName" value="'''+person.lastname+'''" placeholder="Please enter lastname." style="width: 100%; height: 30px;" />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Middle Name
                                        </td>
                                        <td>
                                            <input type="text" name="midName" value="'''+person.middlename+'''" placeholder="Please enter middle name." style="width: 100%; height: 30px;" />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Gender
                                        </td>
                                        <td>
                                            <input type="radio" name="gender" value="m" '''+maleSelected+''' /> Male
                                            <br />
                                            <input type="radio" name="gender" value="f" '''+femaleSelected+''' /> Female
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Date of birth
                                        </td>
                                        <td>
                                            <input type="text" name="dateOfBirth" value="'''+person.dateofB+'''" placeholder="Please enter date of birth." style="width: 100%; height: 30px;" />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            &nbsp;
                                        </td>
                                        <td>
                                            <input type="button" value="Cancel" />
                                            <input type="submit" value="Submit" />
                                        </td>
                                    </tr>
                                </table>
                            </form>
                        </div>
                    </body>
                </html>'''

    return HttpResponse (message)

@csrf_exempt
def doUpdate (request):
    if request.method == "POST":
        _id = request.POST.get("id", "")
        firstName = request.POST.get("firstName", "")
        lastName = request.POST.get("lastName", "")
        midName = request.POST.get("midName", "")
        gender = request.POST.get("gender", "")
        dateOfBirth = request.POST.get("dateOfBirth", "")
        print (firstName)
        print (lastName)
        print (midName)
        print (gender)
        print (dateOfBirth)

        Users.objects.filter(id=_id).update(firstname=firstName, lastname=lastName, middlename=midName, gender=gender, dateofB=dateOfBirth)

    return HttpResponseRedirect('/career/select/')

def delete(request):
    _id = request.GET.get('id','')
    with connection.cursor() as cursor:
         cursor.execute("DELETE FROM person where id= %s", _id)

    return HttpResponseRedirect('/career/select/')
