from django.db import models

# Create your models here.


class Plantao(models.Model):
    data_plantao = models.DateField(verbose_name='Dia')

    delegado_dia = models.CharField(max_length=100, verbose_name='Delegado')
    del_apoio_dia = models.CharField(max_length=100, blank=True,
                                     null=True, verbose_name='Del apoio')
    escriva1_dia = models.CharField(max_length=100,
                                    verbose_name='Escrivão')
    escriva2_dia = models.CharField(max_length=100, blank=True,
                                    null=True, verbose_name='Escriv 2')
    esc_ref_dia = models.CharField(max_length=100,
                                   verbose_name='Escriv ref')
    operacional_dia = models.CharField(max_length=100,
                                       verbose_name='Operac.')
    oper_ref_dia = models.CharField(max_length=100,
                                    verbose_name='Operac ref')

    delegado_noite = models.CharField(max_length=100,
                                      verbose_name='Delegado')
    del_apoio_noite = models.CharField(max_length=100, blank=True,
                                       null=True, verbose_name='Del apoio')
    escrivao_noite = models.CharField(max_length=100,
                                      verbose_name='Escrivão')
    esc_ref_noite = models.CharField(max_length=100,
                                     verbose_name='Escriv ref')
    operacional1_noite = models.CharField(max_length=100,
                                          verbose_name='Operac.')
    operacional2_noite = models.CharField(max_length=100,
                                          blank=True,
                                          null=True,
                                          verbose_name='Operac 2')
    oper_ref_noite = models.CharField(max_length=100,
                                      verbose_name='Operac ref')

    class Meta:
        verbose_name_plural = 'Plantões'

    def __str__(self):
        return self.data_plantao
