from django import forms
from .models import ContactForm
from .models import Review

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label = 'Correo')
    customer_name = forms.CharField(max_length = 64, label = 'Nombre')
    message = forms.CharField(label = 'Mensaje')

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['flan', 'rating', 'comment']
        widgets = {
            'flan': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }