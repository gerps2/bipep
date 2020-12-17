from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import Bit1BooleanField


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
        
        
    def __str__(self):
        return self.nome


class Mensagens(models.Model):
    idmensagem = models.AutoField(db_column='idMensagem', primary_key=True)  # Field name made lowercase.
    conteudomensagem = models.CharField(db_column='conteudoMensagem', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    horamensagem = models.DateTimeField(db_column='horaMensagem', blank=True, null=True)  # Field name made lowercase.
    idpermissao = models.IntegerField(db_column='idPermissao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mensagens'
        
    def __str__(self):
        return self.idmensagem


class Permissoes(models.Model):
    idpermissao = models.AutoField(db_column='idPermissao', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissoes'
        
    def __str__(self):
        return self.nome

class Usuario(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    nome = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    telefone = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    idhospital = models.ForeignKey(Hospitais, models.DO_NOTHING, db_column='idHospital', blank=True, null=True)  # Field name made lowercase.
    idpermissao = models.ForeignKey(Permissoes, models.DO_NOTHING, db_column='idPermissao', blank=True, null=True)  # Field name made lowercase.
    iduser = models.ForeignKey(User, models.DO_NOTHING, db_column='idUser', blank=True, null=True)  # Field name made lowercase.
    isequipe = Bit1BooleanField(db_column='isEquipe', blank=True)  # Field name made lowercase. This field type is a guess.
    areaequipe = models.IntegerField(db_column='areaEquipe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
        
    def __str__(self):
        return self.nome
        
    
class Etnia(models.Model):
    idetnia = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etnia'
        
    def __str__(self):
        return self.nome


class Paciente(models.Model):
    idpaciente = models.CharField(db_column='idPaciente', primary_key=True, max_length=250)  # Field name made lowercase.
    idusuario = models.IntegerField(db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.
    dtnascimento = models.DateField(db_column='dtNascimento', blank=True, null=True)  # Field name made lowercase.
    idetnia = models.ForeignKey(Etnia, models.DO_NOTHING, db_column='idEtnia', blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(max_length=250, blank=True, null=True)
    telefone = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    dttce = models.DateField(db_column='dtTCE', blank=True, null=True)  # Field name made lowercase.
    dtinternaco = models.DateField(db_column='dtInternaco', blank=True, null=True)  # Field name made lowercase.
    dtalta = models.DateField(db_column='dtAlta', blank=True, null=True)  # Field name made lowercase.
    dtobito = models.DateField(db_column='dtObito', blank=True, null=True)  # Field name made lowercase.
    sexo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'

    def __str__(self):
        return self.idpaciente

class Legenda(models.Model):
    idlegenda = models.IntegerField(db_column='idLegenda', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'legenda'
    def __str__(self):
        return self.nome
        
        
class Estatistica(models.Model):
    id = models.IntegerField(primary_key=True)
    dt = models.DateField(blank=True, null=True)
    idlegenda = models.ForeignKey('Legenda', models.DO_NOTHING, db_column='idlegenda', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estatistica'

class Areasequipe(models.Model):
    idarea = models.AutoField(db_column='idArea', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areasequipe'
        
    def __str__(self):
        return self.nome
    
