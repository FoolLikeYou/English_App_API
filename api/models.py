from django.db import models


class Category(models.Model):
    name = models.CharField( max_length = 100)
    icon = models.ImageField(upload_to='icons')

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Theme(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='icons')

    def __str__(self):
        return self.name


class Word(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, related_name='words', verbose_name=u"theme", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    translation = models.CharField(max_length=255)
    transcription = models.CharField(max_length=255)
    example = models.CharField(max_length=255)
    sound = models.FileField(upload_to='sounds')

    def __str__(self):
        return self.name




