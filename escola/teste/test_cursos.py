from escola.models import Curso
from escola.serializers import CursoSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase, force_authenticate
from django.urls import reverse
from rest_framework import status

class CursoTestCase(APITestCase):
    def setUp(self):
        '''Criando um usuário para autenticação'''
        self.usuario = User.objects.create_superuser(username='rogerio', password='galegodoscds')
        self.client.force_authenticate(user=self.usuario)

        '''Criando Instância de Curso'''
        self.curso = Curso.objects.create(
            codigo = 'TSTTFT12',
            descricao = 'Testando aqui pra ver se vai',
            nivel = 'I'
        )

    def test_get_curso(self):
        response = self.client.get(reverse('Cursos-detail', kwargs={'pk': self.curso.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['codigo'], 'TSTTFT12')
        self.assertEqual(response.data['descricao'], 'Testando aqui pra ver se vai')
        self.assertEqual(response.data['nivel'], 'I')


    def test_post_curso(self):
        data = {'codigo': 'deuscalec',
                'descricao': 'Aprendendo a Caetar com um dos melhores ADCs de todos os tempos',
                'nivel': 'A'
                }
        response = self.client.post(reverse('Cursos-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Curso.objects.count(), 2)

    def test_put_curso(self):
        data = {'codigo': 'MicãoPos',
                'descricao': 'Aprendendo aonde você NÃO deve estar em cada fight',
                'nivel': 'A'
                }
        response = self.client.put(reverse('Cursos-detail', kwargs={'pk': self.curso.id}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.curso.refresh_from_db()
        self.assertEqual(self.curso.codigo, 'MicãoPos')
        self.assertEqual(self.curso.descricao, 'Aprendendo aonde você NÃO deve estar em cada fight')
        self.assertEqual(self.curso.nivel, 'A')

    def test_delete_curso(self):
        response = self.client.delete(reverse('Cursos-detail', kwargs={'pk': self.curso.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Curso.objects.count(), 0)

