from django import forms
from . models import Task, UserProfile, Category



#Adding the main thing TASKS
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'complete', 'due_date']

        widgets = {

            'title': forms.TextInput(attrs={
                'class':' w-1/2 p-2 border border-red-500 rounded-lg bg-cyan shadow-sm    focus:outline-none focus:ring-2 focus:ring-purple-500',
                'placeholder': 'Enter task title'
            }),

           
            'description': forms.Textarea(attrs={
                'class':' w-1/2 p-2 border border-red-500 rounded-lg bg-cyan shadow-sm    focus:outline-none focus:ring-2 focus:ring-purple-500',
                'placeholder': 'Enter task description ~'
            }),

            'complete': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-red-600 border border-red-500',
                
            }),

            'due_date': forms.DateInput(attrs={
                'class': 'w-1/7 p-2 border border-red-500 rounded-lg bg-cyan shadow-sm',
                'placeholder': 'DD-MM-YYYY',
                'type': 'date'
                })
        }

    category = forms.ModelChoiceField(
        queryset = Category.objects.all(),
        empty_label = 'Select a Category',
        required=False,
        widget=forms.Select(attrs={
            'class': 'w-1/2 p-2 border border-red-500 rounded-lg bg-cyan shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500'
        })
     )
    

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['display_name', 'bio', 'profile_image']

        widgets = {

            'display_name': forms.TextInput(attrs={
                'class':' w-1/2 p-2 border border-red-500 rounded-lg bg-cyan shadow-sm    focus:outline-none focus:ring-2 focus:ring-purple-500',
                'placeholder': 'Enter profile name'
            }),

            'bio': forms.Textarea(attrs={
                'class':' w-1/2 p-2 border border-red-500 rounded-lg bg-cyan shadow-sm    focus:outline-none focus:ring-2 focus:ring-purple-500',
                'placeholder': 'Enter profile bio ~'
            }),
        }