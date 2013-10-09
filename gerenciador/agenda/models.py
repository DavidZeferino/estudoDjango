# -*- coding: utf-8 -*-

from django.db import models

class ItemAgenda(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    
    class Meta:
        db_table = "tbl_itens_da_agenda"
    class PessoaFisica(models.Model):
        cpf = models.CharField(max_length=11, primary_key=True) 


# Create your models here.
