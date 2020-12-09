# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estatistica(models.Model):
    dt = models.DateField(blank=True, null=True)
    idlegenda = models.ForeignKey('Legenda', models.DO_NOTHING, db_column='idLegenda', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estatistica'


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


class Legenda(models.Model):
    idlegenda = models.IntegerField(db_column='idLegenda', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'legenda'


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


class Paciente(models.Model):
    idpaciente = models.CharField(db_column='idPaciente', primary_key=True, max_length=250)  # Field name made lowercase.
    idusuario = models.IntegerField(db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.
    dtnascimento = models.DateField(db_column='dtNascimento', blank=True, null=True)  # Field name made lowercase.
    idetnia = models.IntegerField(db_column='idEtnia', blank=True, null=True)  # Field name made lowercase.
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
    idhospital = models.ForeignKey(Hospitais, models.DO_NOTHING, db_column='idHospital', blank=True, null=True)  # Field name made lowercase.
    idpermissao = models.ForeignKey(Permissoes, models.DO_NOTHING, db_column='idPermissao', blank=True, null=True)  # Field name made lowercase.
    iduser = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='idUser', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
