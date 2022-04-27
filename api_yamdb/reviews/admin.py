from django.contrib import admin

from .models import Comment, Review


class CommentAdmin(admin.ModelAdmin):
    """Управления комментариями к отзывам."""

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


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
