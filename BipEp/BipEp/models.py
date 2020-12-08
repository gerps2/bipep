from django.db import models
from django.contrib.auth import get_user_model

class Consultas(models.Model):
    idconsulta = models.AutoField(db_column='idConsulta', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    local = models.ForeignKey('Hospitais', models.DO_NOTHING, db_column='local', blank=True, null=True)
    medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='medico', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consultas'


class Exames(models.Model):
    idexame = models.AutoField(db_column='idExame', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    local = models.ForeignKey('Hospitais', models.DO_NOTHING, db_column='local', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exames'


class Hospitais(models.Model):
    idhospital = models.AutoField(db_column='idHospital', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hospitais'


class Medico(models.Model):
    idmedico = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medico'


class Mensagens(models.Model):
    idmensagem = models.AutoField(db_column='idMensagem', primary_key=True)  # Field name made lowercase.
    conteudomensagem = models.CharField(db_column='conteudoMensagem', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    horamensagem = models.DateTimeField(db_column='horaMensagem', blank=True, null=True)  # Field name made lowercase.
    idpermissao = models.IntegerField(db_column='idPermissao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mensagens'


class Permissoes(models.Model):
    idpermissao = models.AutoField(db_column='idPermissao', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissoes'


class Usuario(models.Model):
    nome = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    senha = models.CharField(max_length=1000, blank=True, null=True)
    telefone = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    UltimoLogin = models.DateTimeField(auto_now=True) 
    idhospital = models.ForeignKey(Hospitais, models.DO_NOTHING, db_column='idHospital', blank=True, null=True)  # Field name made lowercase.
    idpermissao = models.ForeignKey(Permissoes, models.DO_NOTHING, db_column='idPermissao', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'usuario'
