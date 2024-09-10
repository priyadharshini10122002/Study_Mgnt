from django import forms
from .models import Study

PHASE_CHOICES = [
    ('Phase I', 'Phase I'),
    ('Phase II', 'Phase II'),
    ('Phase III', 'Phase III'),
    ('Phase IV', 'Phase IV'),
]

SPONSER_CHOICES = [(sponsor, sponsor) for sponsor in Study.objects.values_list('Sponser_Name', flat=True).distinct()]

class StudyForm(forms.ModelForm):
    Phase = forms.ChoiceField(choices=PHASE_CHOICES)
    Sponser_Name = forms.ChoiceField(
        choices=SPONSER_CHOICES,
        required=True,
        label="Sponsor Name"
    )

    class Meta:
        model = Study
        fields = ['Name', 'Phase', 'Sponser_Name', 'Description']
