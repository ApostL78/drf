from django.db import models


class Person(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    def __str__(self):
        return self.title


class Role(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.name
