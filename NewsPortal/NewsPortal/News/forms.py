from django.forms import ModelForm, BooleanField
from .models import Post, User


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'categoryType', 'title', 'text']


class UserForm(ModelForm):
    check_box = BooleanField(label='Уверен?!')

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email']
