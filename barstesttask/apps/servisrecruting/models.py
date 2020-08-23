from django.db import models


class Planet(models.Model):
    planet_name = models.CharField('Название Планеты', max_length = 50)
    siths_in_mtm = models.ManyToManyField('Sith', blank=False, related_name='planets')
    recruts_in_mtm = models.ManyToManyField('Recrut', blank=False, related_name='recruts')

    def __str__(self):
        return self.planet_name
    
    class Meta:
        verbose_name = 'Планета'
        verbose_name_plural = 'Планеты'   

class Sith(models.Model):
    #planet = models.ForeignKey(Planet, on_delete = models.CASCADE)
    sith_name = models.CharField('Имя Ситха', max_length = 50)
    sith_planet = models.CharField('Планета обучения', max_length = 50)
    shadow_hand = 0
    
    def __str__(self):
        return self.sith_name

    def sith_shadow_hand(self, shadow_hand):
        #if Sith 
        if shadow_hand > 3:
            return True


    class Meta:
        verbose_name = 'Ситх'
        verbose_name_plural = 'Ситхи'



class Test_of_shadow_hand(models.Model):
    test_of_shadow_hand_id = models.CharField('Уникальный код Ордена', max_length = 250)
    test_of_shadow_hand_list = models.TextField('Список вопроов', max_length = 200000)
    #вывести 3 вопроса всместо листа?

    def __str__(self):
        return self.test_of_shadow_hand_id

    class Meta:
        verbose_name = 'Испытание Руки Тени'
        verbose_name_plural = 'Испытания Руки Тени'

class Recrut(models.Model):
    recrut_name = models.CharField('Имя Рекрута', max_length = 50)
    recrut_planet = models.CharField('Планета обитания', max_length = 50)
    recrut_age = models.CharField('Возраст', max_length = 50)
    recrut_email = models.EmailField('Email', max_length = 254)
   # recrut = models.ForeignKey(Planet, on_delete = models.CASCADE)
   # recrut_shadow_hand = 0

    def __str__(self):
        return self.recrut_name

    class Meta:
        verbose_name = 'Рекрут'
        verbose_name_plural = 'Рекруты'
   


#Полный список ситхов с указанием их Рук-Теней
#a.comment_set.all()