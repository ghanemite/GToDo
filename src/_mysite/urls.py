from django.conf.urls import include, url
from django.contrib import admin


from todolist.views import (HomePageView, CreateTodoListView, 
                            lists_list, list_details, DeleteTodoListView,
                            AddItemViewView, item_done, item_undone, DeleteItemView
                        )

urlpatterns = [
    # Examples:
    # url(r'^$', '_mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # list urls 
    url(r'^$', HomePageView.as_view(), name='index'),
    url(r'^list/$', lists_list, name='lists_list'),
    url(r'^list/create/$', CreateTodoListView.as_view(), name='create_todo_list'),
    url(r'^list/(?P<slug>[\w\-]+)/$', list_details, name='list_details'),
    url(r'^item/(?P<pk>\d+)/done/$', item_done, name='item_done'),
    url(r'^item/(?P<pk>\d+)/undone/$', item_undone, name='item_undone'),

    # url(r'^item/(?P<pk>\d+)/undone/$', , name='item_done'),
    url(r'^list/(?P<slug>[\w\-]+)/add-item/$', AddItemViewView.as_view(), name='add_item'),
    url(r'^list/(?P<slug>[\w\-]+)/delete/$', DeleteTodoListView.as_view() , name='delete_list'),
    url(r'^item/(?P<pk>\d+)/delete/$', DeleteItemView.as_view(), name='delete_item'),
    url(r'^admin/', include(admin.site.urls)),
]
