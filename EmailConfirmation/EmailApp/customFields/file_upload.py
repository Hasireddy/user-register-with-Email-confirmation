from django.db.models import FileField

from django.forms import ValidationError

from django.forms import forms

ALLOWED_CONTENT_TYPES = ["application/pdf"]
MAX_FILE_SIZE = 10*1024*1024  #10MB


class LicenseFileField(FileField):

    def clean(self, *args, **kwargs):
        data = super().clean(*args, **kwargs)
        file_object = data.file
        
        if file_object.size > MAX_FILE_SIZE:
            raise ValidationError(f"File size exceeds the maximum limit of {MAX_FILE_SIZE}")

        if file_object.content_type not in ALLOWED_CONTENT_TYPES:
            raise forms.ValidationError("Only .pdf file is allowed")

        return data