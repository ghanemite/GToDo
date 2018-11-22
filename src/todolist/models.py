from django.db import models
from django.core.urlresolvers import reverse

class TodoList(models.Model):
    list_name    = models.CharField(
                  max_length=50, help_text='Enter list name max 50 characters')
    slug      = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    date_created = models.DateField(auto_now_add = True)
    date_updated = models.DateField(auto_now = True)


    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.list_name


    def get_absolute_url(self):
        return reverse('list_details', kwargs={'slug': self.slug})


    def get_delete_url(self):
        return reverse('delete_list', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('add_item', kwargs={'slug': self.slug})


class ToDoItem(models.Model):
    parent          = models.ForeignKey(TodoList, related_name='items')
    title           = models.CharField(max_length=100, help_text='max 100 letters')
    description     = models.CharField(max_length=200, blank=True, null=True, help_text='max 200 letters')
    done            = models.BooleanField(default=False)
    date_created    = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ['-date_created']

    def __str_(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item_done', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('delete_item', kwargs={'pk': self.pk})

    def get_update_url(self):
        pass
        
    def get_redone_url(self):
        return reverse('item_redone', kwargs={'pk': self.pk})