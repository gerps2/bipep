from django.contrib import admin
from .models import Usuario
from .models import Hospitais
from .models import Permissoes
from .models import Consultas
from .models import Medico
from .models import Exames
from .models import Areasequipe
from .models import Paciente
from .models import Etnia


admin.site.register(Usuario)
admin.site.register(Hospitais)
admin.site.register(Permissoes)
admin.site.register(Consultas)
admin.site.register(Medico)
admin.site.register(Exames)
admin.site.register(Areasequipe)
admin.site.register(Etnia)
admin.site.register(Paciente)