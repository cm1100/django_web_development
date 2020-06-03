from django.contrib import admin
from .models import Tutorial,Tutorial_Series,Tutorial_Category
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.


class TutorialAsmin(admin.ModelAdmin):
    '''fields = ["tutorial_title",
              "tutorial_published",
              "tutorial_content"]'''

    fieldsets = [
        ("Title/date",{"fields":["tutorial_title","tutorial_published"]}),

        ("URL", {"fields": ["tutorial_slug"]}),
        ("Series", {"fields": ["tutorial_series"]}),


        ("Content",{"fields":["tutorial_content"]})

    ]

    formfield_overrides = {
        models.TextField:{'widget':TinyMCE()}
    }


admin.site.register(Tutorial_Series)
admin.site.register(Tutorial_Category)
admin.site.register(Tutorial,TutorialAsmin)


