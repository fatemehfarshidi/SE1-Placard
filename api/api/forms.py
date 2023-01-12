from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'type', 'price', 'description', 'contact_type',
                  'contact_info', 'image', 'slug', 'date_created', 'user', 'pk')
        read_only_fields = ('user', 'slug', 'date_created', 'pk')

    def clean_title(self):
        title = self.cleaned_data['title']
        if title == "":
            raise forms.ValidationError(
                'Please enter a title')
        return title

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError(
                'Please use a positive number')
        return price
    
    def clean_contact_info(self):
        contact_info = self.cleaned_data['contact_info']
        if contact_info == "":
            raise forms.ValidationError(
                'Please enter your contact information')
        return contact_info
    
    def clean_description(self):
        description = self.cleaned_data['description']
        if description == "":
            raise forms.ValidationError(
                'Please enter a description')
        return description
    
    


