from django.db import models
from django.shortcuts import resolve_url as r
from eventex.core.managers import KindQuerySet, PeriodManager


class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    website = models.URLField('website', blank=True)
    description = models.TextField('descrição', blank=True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'

    KINDS = (
        (EMAIL, 'E-mail'),
        (PHONE, 'Telefone'),
    )
    speaker = models.ForeignKey('Speaker', verbose_name='palestrante')
    kind = models.CharField(max_length=1, choices=KINDS)
    value = models.CharField(max_length=255)

    objects = KindQuerySet.as_manager()

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.value


class Activity(models.Model):
    title = models.CharField('Título', max_length=200)
    start = models.TimeField('Início', blank=True, null=True)
    description = models.TextField('Descrição', blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='palestrante', blank=True)

    objects = PeriodManager()

    class Meta:
        abstract = True
        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'

    def __str__(self):
        return self.title


class Talk(Activity):
    pass


class Course(Activity):
    slots = models.IntegerField()

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
