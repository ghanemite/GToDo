from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify

import unidecode
from unidecode import unidecode

from .models import TodoList, ToDoItem


class CreateToDoListForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = ['list_name', ]

    def clean_list_name(self):
        return self.cleaned_data['list_name'].lower()

    def save(self):
        list_name = self.cleaned_data.get('list_name')
        qs = TodoList.objects.filter(list_name=list_name)
        is_obj = qs.exists()
        if is_obj:
            name_num = qs.count()
            a_slug = '{}-{}'.format(unidecode(list_name), (name_num+1))
            slug = slugify(a_slug)
        else:
            slug = slugify(unidecode(list_name))

        todo_list = TodoList.objects.create(
            list_name=list_name,
            slug=slug
        )
        return todo_list


class AddItemForm(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = ['title', 'description']

    def clean_title(self):
        new_title = self.cleaned_data['title']
        qs = ToDoItem.objects.filter(title=new_title)

        if qs.exists():
            raise ValidationError("Can't create 2 items with the same title")
        if len(new_title) < 6:
            raise ValidationError(
                "The Item title can not be less than 6 letters")
        return new_title

    def clean_description(self):
        new_d = self.cleaned_data['description']
        if new_d != '' and len(new_d) < 6:
            raise ValidationError(
                "The Item title can not be less than 6 letters")
        if len(new_d) > 0:
            return new_d

