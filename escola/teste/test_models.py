from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
     def setUp (self):
          self.estudante = Estudante.objects.create(
               nome = 'Teste de Modelo',
               email = 'testedemodelo@gmail.com',
               cpf = '68195899056',
               data_nascimento = '2023-02-02',
               celular = '86 99999-9999'
          )

     def test_verifica_atributos_de_estudante(self):
          """Teste que verifica os atributos do modelo de Estudante"""
          self.assertEqual(self.estudante.nome,'Teste de Modelo')
          self.assertEqual(self.estudante.email,'testedemodelo@gmail.com')
          self.assertEqual(self.estudante.cpf,'68195899056')
          self.assertEqual(self.estudante.data_nascimento,'2023-02-02')
          self.assertEqual(self.estudante.celular,'86 99999-9999')

class ModelCursoTestCase(TestCase):
     def setUp (self):
          self.curso = Curso.objects.create(
               codigo = '123456',
               descricao = 'Chromakopia',
               nivel = 'A',
          )
     def test_verifica_atributos_do_curso(self):
          """Teste que verifica os atributos do modelo de Curso"""
          self.assertEqual(self.curso.codigo,'123456')
          self.assertEqual(self.curso.descricao,'Chromakopia')
          self.assertEqual(self.curso.nivel,'A')

class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome='Raimundo Neto',
            email='raimundo@gmail.com',
            cpf='12345678901',
            data_nascimento='2000-01-01',
            celular='86 99999-9999'
        )
        self.curso = Curso.objects.create(
            codigo='654321',
            descricao='Teorica de Dobra',
            nivel='A',
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante,  
            curso=self.curso,          
            periodo='V',
        )

    def test_verifica_atributos_da_matricula(self):
        """Teste que verifica os atributos do modelo de Matricula"""
        self.assertEqual(self.matricula.estudante.nome, 'Raimundo Neto')
        self.assertEqual(self.matricula.curso.descricao, 'Teorica de Dobra')
        self.assertEqual(self.matricula.periodo, 'V')
