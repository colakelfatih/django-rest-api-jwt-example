from django.db import models

# Create your models here.
class ClassName(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        db_table = 'class'
        verbose_name = 'Sınıf'
        verbose_name_plural = 'Sınıflar'

    def __str__(self):
        return self.name



class Student(models.Model):
    student_name = models.CharField(max_length=120)
    student_age = models.IntegerField(null=True)
    student_class = models.ForeignKey(ClassName, on_delete=models.CASCADE, null=True)


    def __str__(self):
       return self.student_name

    class Meta:
        db_table = 'student'
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'
