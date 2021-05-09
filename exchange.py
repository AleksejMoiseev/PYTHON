def send_information_email(self, user):
    """
    Send the activation email.
    """
    self.success_url = self.success_url_active_user
    context = dict()
    context['user'] = user

    subject = render_to_string(
        template_name='django_registration/mail/activation_user_subject.txt',
        context=context,
        request=self.request
    )
    subject = ''.join(subject.splitlines())
    message = render_to_string(
        template_name='django_registration/mail/activation_user.txt',
        context=context,
        request=self.request
    )
    signals.user_activated.send(sender=self.__class__, user=user, request=self.request)
    user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
