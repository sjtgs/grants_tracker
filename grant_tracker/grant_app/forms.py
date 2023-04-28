from django import forms
from .fields import GroupedModelChoiceField
from .models import Category, Priority, Grant_Management


class CategoryForm(forms.ModelForm):
    category = GroupedModelChoiceField(
        queryset=Category.objects.exclude(parent=None), choices_groupby="parent"
    )


class PriorityForm(forms.ModelForm):
    category = GroupedModelChoiceField(
        queryset=Priority.objects.exclude(parent=None), choices_groupby="parent"
    )

    class Meta:
        model = Grant_Management
        fields = (
            "item",
            "category",
            "priority",
            "timeline",
            "data_of_submission",
            "Foundation",
            "Amount_Requested",
            "Amount_Received",
            "Awarded_Date",
            "Payment_Date",
            "Purpose",
            "POC_NAME",
            "Email",
            "Phone",
            "Year_Awarded",
        )
