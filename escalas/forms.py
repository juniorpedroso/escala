from django import forms
from .models import Plantao


class PlantaoForm(forms.ModelForm):
    class Meta:
        model = Plantao
        fields = [
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
        ]

        labels = {
            'DateField': 'Dia.......',
            'CharField': 'Delegado..',
            'CharField': 'Del apoio.',
            'CharField': 'Escrivão..',
            'CharField': 'Escriv 2..',
            'CharField': 'Escriv ref',
            'CharField': 'Operac....',
            'CharField': 'Operac ref',

            'CharField': 'Delegado..',
            'CharField': 'Del apoio.',
            'CharField': 'Escrivão..',
            'CharField': 'Escriv ref',
            'CharField': 'Operac....',
            'CharField': 'Operac 2..',
            'CharField': 'Operac ref',

        }
