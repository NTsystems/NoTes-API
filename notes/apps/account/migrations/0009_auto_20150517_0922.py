# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management import call_command
from django.db import models, migrations

from rest_framework.authtoken.models import Token


def setup_accounts(apps, schema_editor):
    User = apps.get_model("account", "User")

    # create admin
    admin_password = "pbkdf2_sha256$20000$Ev9WcutfldWg$/QO+VT1boIENG+kdoIw3qn++QeipTKOx1yxUMzmUQVw="

    User.objects.create(e_mail="office@ntsystems.rs",
                        password=admin_password,
                        is_staff=True,
                        is_superuser=True)

    # create simple user
    swagger_password = "pbkdf2_sha256$20000$k6C2DXjal2YK$NWu2SW7QsrF8AspNos5GTqa803/a7XEp3LskZJ3BXiY="

    swagger = User.objects.create(e_mail="swagger@ntsystems.rs",
                                  password=swagger_password,
                                  is_staff=False,
                                  is_superuser=False)

    Token.objects.create(user_id=swagger.id, key="bbc7f7b5492468db6a4a54a00c1b504930371792")


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20150514_1011'),
        ('authtoken', '__first__')
    ]

    operations = [
        migrations.RunPython(setup_accounts)
    ]
