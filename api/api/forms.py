from django import forms
from .models import Post


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'type', 'price', 'description',
                  'contact_info', 'image', 'slug', 'date_created', 'user')
        read_only_fields = ('user', 'slug', 'date_created')

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'placeholder': '   نام محصول/ خدمت/ آگهی خود را وارد کنید   '})
        self.fields['contact_info'].widget.attrs.update(
            {'placeholder': '  شماره تماس/ ایدی تلگرام/ ایمیل    '})
        self.fields['price'].widget.attrs.update(
            {'placeholder': '   قیمت به تومان    '})
        self.fields['description'].widget.attrs.update({
            'id': 'description-input',
            'cols': "65",
            'rows': "5",
            'placeholder': ' جزئیات و نکات جالب توجه آگهی خود را کامل و دقیق بنویسید. نوشتن شمارهٔ تماس در متن آگهی مجاز نیست. حتماً به ساعات پاسخگویی خود اشاره کنید   ',
        })
