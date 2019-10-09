from django import forms
from myapp.models import Client

class ClientForm(forms.ModelForm):
    client_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
    address_street_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9A-Za-z ]+', 'title':'Enter Characters Only '}))
    suburb = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
    #postcode = forms.IntegerField(required=False)
    state = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
    contact_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
    # email_address = forms.CharField(required=True)
    # phone_number = forms.IntegerField(required=True)
    class Meta:
        model = Client
        fields = ['client_name','address_street_name','suburb','postcode','state','contact_name','email_address','phone_number']

    