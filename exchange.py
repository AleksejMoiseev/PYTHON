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


class RepresentationToBannerForm(forms.Form):
    actions = forms.CharField(required=False, label='Click URL')
    tracking_urls = forms.CharField(required=False, label='Tracking')
    native = forms.CharField(required=False)
    vast_tracking_urls = forms.CharField(required=False)
    video = forms.CharField(required=False)
    img = forms.CharField(required=False)

    # TODO: Non-core fields
    markup = forms.CharField(required=False)
    slides = forms.CharField(required=False)
    attributes = forms.CharField(required=False)
    width = forms.CharField(required=False)
    height = forms.CharField(required=False)
    btext = forms.CharField(required=False, label='Text of banner')
    title = forms.CharField(required=False)
    current_ctr = forms.DecimalField(decimal_places=4, max_digits=20, required=False)
    btype = forms.IntegerField(required=False)
    iab_category = forms.CharField(required=False)
    moderation = forms.BooleanField(required=False)
    throttling_enabled = forms.BooleanField(required=False, label='Frequency cap')
    throttling_period = forms.IntegerField(required=False, label='Period(sec)')
    throttling_maxnumber = forms.IntegerField(required=False, label='Max impressions')
    third_party_cpm = forms.DecimalField(max_digits=20, decimal_places=4, required=False)

    def clean_native(self):
        native = self.cleaned_data['native']
        if native:
            native = literal_eval(native)
            row_value = native[0]
            value = ''
            for k, v in row_value.items():
                if k == 'icons__width' \
                        or k == 'icons__height' \
                        or k == 'images__width' \
                        or k == 'images__height' \
                        or k == 'brandname':
                    continue
                if k == 'icons__img':
                    k = 'Icon IMG'
                    v = f'<a target=_blank href="/media/{v}">Link</a>'
                if k == 'images__img':
                    k = 'Main IMG'
                    v = f'<a target=_blank href="/media/{v}">Link</a>'
                value += f'{k}: {v}<br>'
            return value
        return native

    def clean_vast_tracking_urls(self):
        value = self.cleaned_data['vast_tracking_urls']
        result = ''
        if value:
            value = literal_eval(value)
            for i in value:
                result += f'{i["event"]}: {i["url"]}<br>'
            return result
        return value

    def clean_video(self):
        video = self.cleaned_data['video']
        if video:
            video = literal_eval(video)
            return '<a target=_blank href="/media/{}">Link</a>'.format(video[0]["file"])
        return video

    def clean_actions(self):
        actions = self.cleaned_data['actions']
        if actions:
            actions = literal_eval(actions)
            return actions[0]['value'] if len(actions) else 'None'
        return actions

    def clean_tracking_urls(self):
        tracking_urls = self.cleaned_data['tracking_urls']
        if tracking_urls:
            tracking_urls = literal_eval(tracking_urls)
            return tracking_urls[0]['url'] if len(tracking_urls) else 'None'
        return tracking_urls

    def clean_img(self):
        img = self.cleaned_data['img']
        if img:
            return '<a target=_blank href="/media/{}">Link</a>'.format(img)
        return img



class RepresentationToGroupModelForm(RepresentationToBaseModelForm):
    _exclude_fields = ('id', 'created', 'gdailybudget', 'throttling_period', 'device', 'os',)
    gdailybudget = forms.CharField(required=False)
    throttling_period = forms.IntegerField(required=False)
    bid = forms.IntegerField(required=False)

    class Meta:
        model = Group
        fields = '__all__'
        exclude = ['gdailybudget', 'throttling_period', 'device', 'os', 'bid']

    def clean_bid(self):
        bid = self.cleaned_data['bid']
        print('BID', bid, type(bid))
        if bid:
            return ('$' + str(round(float(bid) / 100, 2))) if bid else 'None'
        return bid

    def clean_gdailybudget(self):
        gdailybudget = self.cleaned_data['gdailybudget']
        if gdailybudget:
            return ('$' + str(round(float(gdailybudget) / 100, 2))) if gdailybudget else 'None'

    def clean_throttling_period(self):
        throttling_period = self.cleaned_data['throttling_period']
        if throttling_period:
            return (str(int(throttling_period) / 86400) + ' day') if throttling_period else 'None'

    def clean_ssps(self):
        ssps = self.cleaned_data['ssps']
        if ssps:
            ssps = literal_eval(ssps)
            return ', '.join([''.join(v['ssp']) for v in ssps]) if ssps else 'None'
        return ssps

    def clean(self):
        return super().clean()

class RepresentationToBannerModelForm(RepresentationToBaseModelForm):
    _exclude_fields = ('group', 'id', 'created', )
    actions = forms.CharField(required=False, label='Click URL')
    tracking_urls = forms.CharField(required=False, label='Tracking')
    native = forms.CharField(required=False)
    vast_tracking_urls = forms.CharField(required=False)
    video = forms.CharField(required=False)

    class Meta:
        model = Banner
        fields = '__all__'
        exclude = ['group']
        labels = {
            'btext': _('Text of banner'),
            'throttling_enabled': _('Frequency cap'),
            'throttling_period': _('Period(sec)'),
            'throttling_maxnumber': _('Max impressions'),
        }

    def clean_native(self):
        native = self.cleaned_data['native']
        if native:
            native = literal_eval(native)
            row_value = native[0]
            value = ''
            for k, v in row_value.items():
                if k == 'icons__width' \
                        or k == 'icons__height' \
                        or k == 'images__width' \
                        or k == 'images__height' \
                        or k == 'brandname':
                    continue
                if k == 'icons__img':
                    k = 'Icon IMG'
                    v = f'<a target=_blank href="/media/{v}">Link</a>'
                if k == 'images__img':
                    k = 'Main IMG'
                    v = f'<a target=_blank href="/media/{v}">Link</a>'
                value += f'{k}: {v}<br>'
            return value
        return native

    def clean_vast_tracking_urls(self):
        value = self.cleaned_data['vast_tracking_urls']
        result = ''
        if value:
            value = literal_eval(value)
            for i in value:
                result += f'{i["event"]}: {i["url"]}<br>'
            return result
        return value

    def clean_video(self):
        video = self.cleaned_data['video']
        if video:
            video = literal_eval(video)
            return '<a target=_blank href="/media/{}">Link</a>'.format(video[0]["file"])
        return video

    def clean_actions(self):
        actions = self.cleaned_data['actions']
        if actions:
            actions = literal_eval(actions)
            return actions[0]['value'] if len(actions) else 'None'
        return actions

    def clean_tracking_urls(self):
        tracking_urls = self.cleaned_data['tracking_urls']
        if tracking_urls:
            tracking_urls = literal_eval(tracking_urls)
            return tracking_urls[0]['url'] if len(tracking_urls) else 'None'
        return tracking_urls

    def clean_img(self):
        img = self.cleaned_data['img']
        if img:
            return '<a target=_blank href="/media/{}">Link</a>'.format(img)
        return img

class RepresentationToBaseModelForm(forms.ModelForm):
    _exclude_fields = ('id', )
    bid = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.display_fields:
            self.fields[field].required = False

    @property
    def exclude_fields(self):
        return self._exclude_fields

    @property
    def display_fields(self):
        return [field.name for field in self.Meta.model._meta.fields if field.name not in self.exclude_fields]

