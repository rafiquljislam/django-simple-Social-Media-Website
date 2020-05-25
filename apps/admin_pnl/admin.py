from django.contrib import admin
from apps.posts.models import Post
from django.utils.html import format_html

class MyAdminSite(admin.AdminSite):
    admin.AdminSite.site_header = "Welcome Rafiq"
    admin.AdminSite.site_title = "rafiq"
    admin.AdminSite.index_title = "Rafiq Blog"
    
class PostAdmin(admin.ModelAdmin):    
    list_display = ('id','title','date','imageeeee')
    list_display_links = ('title',)
    list_filter = ('title',)
    list_select_related = False
    list_per_page = 30
    list_max_show_all = 200
    list_editable = ()
    search_fields = ('title','date','content')
    date_hierarchy = None
    save_as = False
    save_as_continue = True
    save_on_top = False
    preserve_filters = True
    inlines = []

    # Custom templates (designed to be over-ridden in subclasses)
    add_form_template = None
    change_form_template = None
    change_list_template = None
    delete_confirmation_template = None
    delete_selected_confirmation_template = None
    object_history_template = None
    popup_response_template = None

    # Actions
    actions = []
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True






admin.site.register(Post,PostAdmin)
