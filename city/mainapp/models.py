from django.db import models


class City(models.Model):
    name = models.CharField('Название города', max_length=50)
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        
    def __str__(self) -> str:
        return self.name
        

class People(models.Model):
    fio = models.CharField('ФИО жителя', max_length=150)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='peoples', 
                             verbose_name='Город проживания')
    
    class Meta:
        verbose_name = 'Житель'
        verbose_name_plural = 'Жители'
        
    def __str__(self) -> str:
        return self.fio