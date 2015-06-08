from __future__ import absolute_import

import hashlib 
import datetime
import random

from django.contrib.auth import get_user_model
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context, Template

from celery import shared_task
from notes.celeryconf import app


# templated email
@app.task(bind=True)
def activation_email_template(cls, user_id):
    user = get_user_model().objects.get(id=user_id)
    email = user.e_mail
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    activation_key = hashlib.sha1(salt+email).hexdigest()

    htmly = get_template('activation.html')

    context_kw = Context({'user': {'email': email, 'activation_key': activation_key}})
    
    email_subject = 'Account confirmation - NoTes'
    from_email = 'testntsystems@gmail.com'
    html_content = htmly.render(context_kw)
    msg = EmailMultiAlternatives(email_subject, html_content, 
                                 from_email, [email])
    msg.content_subtype = "html"
    print user
    msg.send()