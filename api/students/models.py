from django.db import models

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256)
    date_of_birth = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "students"
