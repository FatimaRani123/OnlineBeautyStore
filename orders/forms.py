from django import forms

class CheckoutForm(forms.Form):
    customer_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    postal_code = forms.CharField(max_length=20)
