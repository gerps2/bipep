from django.db import models
from django.contrib.auth import get_user_model


PERMISSOES = (
    (1, 'admin'),
    (2, 'paciente'),
    (3, 'equipe')
)