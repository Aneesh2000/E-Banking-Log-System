from django import forms
from . import models

class MoneyTransferForm (forms.ModelForm):
    class Meta:
        model = models.MoneyTransfer
        fields = [
            "enter_your_user_name",
            "enter_the_destination_account_number", 
            "enter_the_amount_to_be_transferred_in_INR"
        ]
