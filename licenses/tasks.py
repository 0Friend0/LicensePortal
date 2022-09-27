from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .models import License, Client
from django.core.mail import EmailMessage
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta




@shared_task(name='email_sending')
def email():
    clients = Client.objects.all()
    for client in clients:
        licenses_list = License.objects.filter(client=client.id)
        licenses_expiry = []

 
        for license in licenses_list:
            # Expiration date within a week
            if license.expiration_date <= (datetime.today().date() + timedelta(days=7)):

                licenses_expiry.append([license, (license.expiration_date-datetime.today().date()).days])
                continue

            # Expiration date within a month and today is monday
            if license.expiration_date <= (datetime.today().date() + relativedelta(months=+1)) and date.today().weekday() == 6:
                licenses_expiry.append([license, (license.expiration_date-datetime.today().date()).days])
                continue

            if license.expiration_date == (datetime.today().date() + relativedelta(months=+4)):
                licenses_expiry.append([license, (license.expiration_date-datetime.today().date()).days])


        email_body = f"""Hi {client.name}. \n
        You have license that will expire soon. Please see below for more information.
        """
        for license in licenses_expiry:
            email_body += f"\n{license[0].name}    License id: {license[0].id}    Expiration date: {license[0].expiration_date}    Days left: {license[1]} Contact: {client.admin_poc}"

        email = EmailMessage('License Portal', email_body, to=[f"{client.admin_poc}"])
        email.send()
    return print("Mails sent!")

