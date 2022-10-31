from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django import forms
from mainapp.models import Comment


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'common-input mb-20 form-control',
                                                                        'placeholder': "Введите Ваше имя:"}), label='')
    email_address = forms.EmailField(max_length=150,
                                     widget=forms.TextInput(attrs={'class': 'common-input mb-20 form-control',
                                                                   'placeholder': "Введите Ваш email:"}), label='')
    subject = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'common-input mb-20 form-control',
                                                                            'placeholder': "Введите тему:"}), label='')


class MessageForm(forms.Form):
    message = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'class': 'common-textarea form-control',
                                                                            'cols': '30', 'rows': "10",
                                                                            'placeholder': "Введите сообщение:"}),
                              label='')


class FollowForm(forms.Form):
    email_address = forms.EmailField(max_length=150,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': "Ваш email:"}), label='')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user_name', 'email', 'comment', 'course', 'experience', 'photo')
        help_texts = {
            'photo': ('Загрузите свое фото'),
        }

    helper = FormHelper()

    helper.form_show_labels = False
    helper.layout = Layout(
        Field('user_name', css_class='common-input mt-30 mb-20 col-lg-11 form-control',
              placeholder="Введите Ваше имя:"),
        Field('email', css_class='common-input  mb-20 col-lg-11 form-control', placeholder="Введите Ваш email:"),
        Field('comment', css_class='common-textarea mb-20 col-lg-11 form-control', cols='30', rows="10",
              placeholder="Введите комментарий:"),
        Field('course', css_class='common-textarea mb-20 col-lg-11 form-control'),
        Field('experience', css_class='common-textarea mb-20 col-lg-11 form-control'),
        Field('photo', css_class='common-textarea col-lg-11 form-control'),
    )
