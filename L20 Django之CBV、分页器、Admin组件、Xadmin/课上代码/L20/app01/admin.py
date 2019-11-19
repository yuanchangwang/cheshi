from django.contrib import admin
from app01 import models

# Register your models here.


# @admin.register(models.Book)  # 方式二 注册
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'publish', "show_authors"]  # 定制展示的列
    list_display_links = ('price',)  # 定制跳转的列
    list_filter = ('publish', 'authors')  # 定制过滤列
    search_fields = ('title', 'price')  # 定制模糊搜索列
    # list_editable = ('title',)  # 定制可以直接编辑的列
    actions = ['patch_init']  # 定制批量处理方法

    def show_authors(self, obj):
        return " | ".join([i.name for i in obj.authors.all()])

    def patch_init(self, request, queryset):
        queryset.update(price=100)

    patch_init.short_description = "批量初始化"  # 设置操作名称


admin.site.register(models.Book, BookAdmin)  # 方式一 常用的方法
admin.site.register(models.Publish)
admin.site.register(models.Author)
admin.site.register(models.AuthorDetail)
