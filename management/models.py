from django.db import models

class management(models.Model):
    group = models.IntegerField()
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    # yesma add garesi :  python manage.py makemigrations management
    # ani: python manage.py migrate
    # check in /admin

    def __str__(self):
        return self.name
