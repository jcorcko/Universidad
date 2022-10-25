from msilib.schema import Class
from django.test import TestCase
from Aplicaciones.Academico.models import Curso

# Create your tests here.

class CursoTestCase(TestCase):
    def setUp(self):
        Curso.objects.create(codigo="1234", nombre="MATEMÁTICA APLICADA I", creditos="8")
        Curso.objects.create(codigo="4325", nombre="MATEMÁTICA APLICADA II", creditos="8")

    def test_crear_curso(self):
        curso = Curso.objects.create_curso(
            codigo="3456",
            nombre="INFORMÁTICA I",
            creditos="12"
        )
        assert curso.codigo == "3456"