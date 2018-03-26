from __future__ import unicode_literals
from time import gmtime, strftime
from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.utils.crypto import get_random_string
import sys, re
from flask import Flask, request, redirect, render_template, session, flash
import md5, os, binascii
import bcrypt
from django.core.urlresolvers import reverse

# TYLER MONDRAGON

app = Flask(__name__)
app.secret_key = 'unicorn'
rejectEmail = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# mysql = MySQLConnector(app, 'loginandreg')

def index():
    users = User.objects.get.all()
    # print str(users)
    sys.stdout.flush()  # to flush output
    return render_template('index.html', all_users=users)

#################################################################################################
def validate():
    if request.session == 'post':
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        password = request.form['password']
        email = request.form['email']
        # salt = binascii.b2a_hex(os.urandom(15))
        # session['salt'] = salt
        hashedPw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        # b92ffe1e926519608bab4cd327aed6e4
        if len(email) < 1 or len(password) < 1:
            flash("Email and/or Password cannot be empty!")
            return redirect('/')
        else:
            if not rejectEmail.match(email):
                flash("Email is not valid!")
                return redirect('/')
            flash("Email address: {} is accepted!".format(email))
            # PUT PASSWORD AND SALT TOGETHER IN DB
            data = {'email': email}

            # query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            query = User.objects.get(email = email)
            result = mysql.query_db(query, data)

            if len(result) != 0:
                # print "dddddddddddddddatabase - " + str(result[0])
                encrypted_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                # bb9bcd94992476c1d059c1dcdc8cfaa7
                # print (result[0]['psswrd'] + result[0]['salt']) + 'TTTTTTTTTTTTTTTTTTTTT'
                # 5d41402abc4b2a76b9719d911017c592103afc347a51dc497702b2d17871ed
                if result[0]['psswrd'] == encrypted_password:
                    flash("Password matched!")
                    return render_template('success.html')
                else:
                    flash("Password not matched!")
                    # print encrypted_password +'          TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT'
                    # bb9bcd94992476c1d059c1dcdc8cfaa7
                    # 5d41402abc4b2a76b9719d911017c592   ------- hello
                    # 36d3d28a1e6d85fea191c94cbca48a4f -- encripted password
                    return redirect('/')
            else:
                flash("Email not registered. Please sign up.")
                return redirect('/')

        sys.stdout.flush()  # to flush output
        return redirect('success.html', data)

#################################################################################################
def add():
    if request.session == 'post':
        session['name'] = request.form['nName']
        session['email'] = request.form['eEmail']
        session['cPassword'] = request.form['cPassword']
        session['conPassword'] = request.form['conPassword']
        # salter = binascii.b2a_hex(os.urandom(15))
        # session['salt'] = salter
        password = bcrypt.hashpw(session['cPassword'].encode(), bcrypt.gensalt())
        # hashedPw = md5.new(password + salter).hexdigest()

        if session['cPassword'] != session['conPassword']:
            flash("Password doesn't not match, Try again.")
            return redirect('/')

        query = User.objects.create(name=session['name'], email=session['email'])
        query.save()
        # "INSERT INTO users (name, email, psswrd, salt, created_at, updated_at) VALUES (:name, :email, :psswrd, :salt, NOW(), NOW())"
        # # We'll then create a dictionary of data from the POST data received.
        data = {
            'name': request.form['nName'],
            'email': request.form['eEmail'],
            'password': password
        }
        flash("Welcome  {}, Thank you for registering!".format(request.form['nName']))
        # mysql.query_db(query, data)

        sys.stdout.flush()  # to flush output
        return render_template("success.html")

#################################################################################################
def goingaway():
    session.clear()
    sys.stdout.flush()  # to flush output
    return redirect('/')

#################################################################################################
def update(request):
    errors = Blog.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/blog/edit/'+id)
    else:
        blog = Blog.objects.get(id = id)
        blog.name = request.POST['name']
        blog.email = request.POST['email']
        blog.save()
        return redirect('success.html')

sys.stdout.flush()  # to flush output
app.run(debug=True)