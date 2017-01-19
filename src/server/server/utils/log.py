from django.utils.log import AdminEmailHandler as DjangoAdminEmailHandler
from django.core import mail


class AdminEmailHandler(DjangoAdminEmailHandler):

    def send_mail(self, subject, message, *args, **kwargs):
        mail.mail_admins(subject, message, *args, connection=self.connection(), **kwargs)
