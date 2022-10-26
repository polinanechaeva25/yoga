from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'common-input mb-20 form-control',
                                                                        'placeholder': "Введите Ваше имя:"}), label='')
    email_address = forms.EmailField(max_length=150, widget=forms.TextInput(attrs={'class': 'common-input mb-20 form-control',
                                                                                   'placeholder': "Введите Ваш email:"}), label='')
    subject = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'common-input mb-20 form-control',
                                                                         'placeholder': "Введите тему:"}), label='')


class MessageForm(forms.Form):
    message = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'class': 'common-textarea form-control',
                                                                            'cols': '30', 'rows': "10",
                                                                            'placeholder': "Введите сообщение:"}), label='')
