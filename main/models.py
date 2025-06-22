from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    tizer = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Biz haqimizda"
        verbose_name_plural = "Biz haqimizda maqolalar"

    def __str__(self) -> str:
        return self.title

class News(models.Model):
    image = models.ImageField(upload_to='images/%Y.%m.%d/news/')
    title = models.CharField(max_length=256)
    date = models.DateField()
    text = models.TextField()
    big_text = RichTextField()
    slug = models.SlugField()

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

    def __str__(self) -> str:
        return self.title

class Plans(models.Model):
    image = models.ImageField(upload_to='images/%Y.%m.%d/plans/')
    title = models.CharField(max_length=256)
    text = models.TextField()
    data = models.DateField()

    class Meta:
        verbose_name = "Kelgusi tadbir"
        verbose_name_plural = "Kelgusi tadbirlar"

    def __str__(self) -> str:
        return self.title


class TeamMember(models.Model):
    image = models.ImageField(upload_to="images/%Y.%m.%d/team/")
    name = models.CharField(max_length=256)
    profession = models.CharField(max_length=256)
    text = models.TextField()

    class Meta:
        verbose_name = "Jamoa azosi"
        verbose_name_plural = "Jasmoa azolari"

    def __str__(self) -> str:
        return self.name


class Gallary(models.Model):
    image = models.ImageField(upload_to='images/%Y.%m.%d/gallary/')

    class Meta:
        verbose_name = "Galareya surati"
        verbose_name_plural = "Galareya suratlari"

    def __str__(self) -> str:
        return str(self.pk)


class Partner(models.Model):
    image = models.ImageField(upload_to='images/%Y.%m.%d/partner/')

    class Meta:
        verbose_name = "Hamkor"
        verbose_name_plural = "Hamkorlar"

    def __str__(self) -> str:
        return f"{self.pk}inchi hamkor"


class Map(models.Model):
    embeded_url = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Xarita"
        verbose_name_plural = "Xaritalar"

    def __str__(self) -> str:
        return f"{self.pk}inchi hamkor"

class Murojaat(models.Model):
    ism = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    matn = models.TextField()
