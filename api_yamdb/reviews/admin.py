from django.contrib import admin

from .models import Comment, Review, Genre, Title, Category, GenreTitle


class CommentAdmin(admin.ModelAdmin):
    """Управление комментариями к отзывам."""

    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'review',
    )
    search_fields = ('text',)
    list_filter = ('pub_date',)


class ReviewAdmin(admin.ModelAdmin):
    """Управление отзывами пользователей."""

    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'score',
        'title',
    )
    list_editable = ('title',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class TitleAdmin(admin.ModelAdmin):
    """Управление произведениями"""

    list_display = (
        'name',
        'year',
        'description',
        'category',
    )
    list_editable = ('category',)
    search_fields = ('name',)
    list_filter = ('year',)


class CategoryAdmin(admin.ModelAdmin):
    """Управление категориями"""

    list_display = ('name', 'slug')
    search_fields = ('name',)


class GenreAdmin(admin.ModelAdmin):
    """Управление списком жанров."""

    list_display = ('name', 'slug')
    search_fields = ('name',)


class GenreTitleAdmin(admin.ModelAdmin):
    """Управление жанрами произведений."""

    list_display = ('pk', 'title', 'genre')
    search_fields = ('title__name',)
    list_editable = ('title', 'genre')
    list_filter = ('title',)


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(GenreTitle, GenreTitleAdmin)
