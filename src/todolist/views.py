from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ValidationError

from .models import TodoList, ToDoItem 

from .forms import CreateToDoListForm, AddItemForm

class HomePageView(View):

    template_name = 'todolist/homepage.html'
    model = TodoList

    def get(self, request, *args, **kwargs):
        todolists = TodoList.objects.all().count()

        context = {
            'todolists':todolists,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass


class CreateTodoListView(View):
    
    model = TodoList
    template_name = 'todolist/create_list_form.html'
    form_class = CreateToDoListForm

    def get(self, request):
        
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('lists_list')
        else:
            return render(request, self.template_name, {'form':bound_form})
        
def lists_list(request):
    lists = TodoList.objects.all()
    context = {
        'lists':lists
    }
    return render(request, 'todolist/lists_list.html', context)

def list_details(request, slug):
    todo_list = get_object_or_404(TodoList, slug=slug)
    context = {
        'list':todo_list,
    }

    return render(request, 'todolist/list_details.html', context)

class DeleteTodoListView(View):
    
    model = TodoList
    template_name = 'todolist/delete_list_form.html'

    def get_object(self, slug):
        my_list = get_object_or_404(TodoList, slug=slug)
        return my_list

    def get(self, request, slug, *args, **kwargs):
        my_list = self.get_object(slug=slug)
        return render(request, self.template_name, {'list':my_list})

    def post(self, request, slug, *args, **kwargs):
        my_list = self.get_object(slug=slug)
        my_list.delete()
        return redirect('lists_list')


class AddItemViewView(View):
    
    model = TodoList
    template_name = 'todolist/add_item_form.html'
    form_class = AddItemForm

    def get_object(self, slug):
        my_list = get_object_or_404(self.model, slug=slug)
        return my_list

    def get(self, request, slug, *args, **kwargs):
        my_list = self.get_object(slug=slug)
        form = self.form_class()
        return render(request, self.template_name, {'list':my_list,'form':form})

    def post(self, request, slug, *args, **kwargs):
        my_list = self.get_object(slug=slug)
        form = self.form_class(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.parent = my_list
            item.save()
            return redirect(my_list)
        else:
            return render(request, self.template_name, {'list':my_list,'form':form})
  

def item_done(request, pk):
    item = get_object_or_404(ToDoItem, pk=pk)
    item.done = True
    item.save()
    my_list = item.parent
    return redirect(my_list)

def item_redone(request, pk):
    item = get_object_or_404(ToDoItem, pk=pk)
    item.done = False
    item.save()
    my_list = item.parent
    return redirect(my_list)


class DeleteItemView(View):
    
    model = ToDoItem
    template_name = 'todolist/delete_item.html'

    def get_object(self, pk):
        item = get_object_or_404(self.model, pk=pk)
        return item

    def get(self, request, pk, *args, **kwargs):
        item = self.get_object(pk=pk)
        return render(request, self.template_name, {'tem':item})

    def post(self, request, pk, *args, **kwargs):
        item = self.get_object(pk=pk)
        my_list = item.parent
        item.delete()
        return redirect(my_list)
