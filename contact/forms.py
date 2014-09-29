from django import forms

class ContactForm(forms.Form):
  subject = forms.CharField(max_length=20)
  email = forms.EmailField(required=False, label='You e-mail address')
  message = forms.CharField()

  def clean_message(self):
    message = self.cleaned_data['message']
    num_words = len(message.split())
    if num_words < 4:
      raise forms.ValidationError("Not enough words")
    return message
