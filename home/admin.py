from django.contrib import admin
from home.models import Image,ContactMessage,Role,Project,Post,Education,Experience,Skill,Tag,Category

# Register your models here.
admin.site.register(ContactMessage)
admin.site.register(Role)
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)