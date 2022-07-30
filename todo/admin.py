from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):      #Отображает дату и время создания записи
    readonly_fields = ('created',) #created - модель из класса Todo

admin.site.register(Todo, TodoAdmin)

#python3 manage.py makemigrations | python3 manage.py migrate