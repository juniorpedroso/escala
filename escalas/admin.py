from django.contrib import admin
from escalas.models import Plantao

# Register your models here.

class PlantaoDN(admin.ModelAdmin):
    list_display = (
        'data_plantao',

        'delegado_dia',
        'del_apoio_dia',
        'escriva1_dia',
        'escriva2_dia',
        'esc_ref_dia',
        'operacional_dia',
        'oper_ref_dia',

        'delegado_noite',
        'del_apoio_noite',
        'escrivao_noite',
        'esc_ref_noite',
        'operacional1_noite',
        'operacional2_noite',
        'oper_ref_noite',
    )


admin.site.register(Plantao, PlantaoDN)