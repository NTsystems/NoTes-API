from __future__ import absolute_import
from celery import shared_task
from notes.celeryconf import app
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
import hashlib 
import datetime
import random

@app.task(bind=True)
def user_send_activation_email(cls, user_id):
    user = get_user_model().objects.get(id=user_id)
    email = user.e_mail
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    activation_key = hashlib.sha1(salt+email).hexdigest()
    # Send email with activation key
    email_subject = 'Account confirmation - NoTes'
    email_body = "Hey %s, thanks for signing up. To activate your account, click this link within 48hours \
                  http://192.168.85.5:8000/swagger/#!/users/confirm/%s" % (email, activation_key)
    print email
    print get_user_model().objects.all()
    send_mail(email_subject, email_body,'testntsystems@gmail', [email], fail_silently=False)