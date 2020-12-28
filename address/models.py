from django.db import models


# Create your models here.
class FileUpload(models.Model):
    file = models.FileField(upload_to='uploaded_files')

    def __str__(self):
        return self.file.name
