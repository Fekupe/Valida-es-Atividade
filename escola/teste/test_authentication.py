from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase, force_authenticate
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante, Curso, Matricula

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')

    def test_autenticacao_user_com_credenciais_corretas(self):
        usuario = authenticate(username='admin', password='admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)

    def test_autenticacao_usuario_com_credenciais_incorretas(self):
        usuario = authenticate(username='adimin', password='admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_autenticacao_senha_com_credenciais_incorretas(self):
        usuario = authenticate(username='admin', password='adimin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_get_request(self):
        self.client.force_authenticate(user=self.usuario)
        response = self.client.get(reverse('Estudantes-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_failed_request(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('Estudantes-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        ######################################################################
        '''Testes de Requisições GET, POST, PUT e DELETE'''

class EstudanteAPITests(APITestCase):
    def setUp(self):
        '''Criando um usuário para autenticação'''
        self.usuario = User.objects.create_superuser(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.usuario)

        '''Criando Instância de Estudante'''
        self.estudante = Estudante.objects.create(nome = 'Raimundo Neto',
            email = 'raimundonetolindodemamae@gmail.com',
            cpf = '98765432145',
            data_nascimento = '2002-06-06',
            celular = '84 988721697'
        )

    def test_get_estudante(self):
        response = self.client.get(reverse('Estudantes-detail', kwargs={'pk': self.estudante.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['nome'], 'Raimundo Neto')
        self.assertEqual(response.data['email'], 'raimundonetolindodemamae@gmail.com')
        self.assertEqual(response.data['cpf'], '98765432145')
        self.assertEqual(response.data['data_nascimento'], '2002-06-06')
        self.assertEqual(response.data['celular'], '84 988721697')
        
    def test_post_estudante(self):
        data = {'nome': 'Tossego',
                'email': 'tossegodoszoi@gmail.com',
                'cpf': '66956979497',
                'data_nascimento': '1999-02-06',
                'celular': '84988731798'
                }
        response = self.client.post(reverse('Estudantes-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Estudante.objects.count(), 2)

    def test_put_estudante(self):
        data = {
            'nome': 'Ludmila',
            'email': 'updatedemail@gmail.com',
            'cpf': '00575577053',
            'data_nascimento': '2002-06-06',
            'celular': '84999999999'
        }
        response = self.client.put(reverse('Estudantes-detail', kwargs={'pk': self.estudante.id}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.estudante.refresh_from_db()
        self.assertEqual(self.estudante.nome, 'Ludmila')
        self.assertEqual(self.estudante.email, 'updatedemail@gmail.com')
        self.assertEqual(self.estudante.celular, '84999999999')

    def test_delete_estudante(self):
        response = self.client.delete(reverse('Estudantes-detail', kwargs={'pk': self.estudante.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Estudante.objects.count(), 0)

    # def test_put_estudante(self):
    #     data = {'nome': 'Tossego Doszoi',
    #             'email': 'tossegodoszoi@gmail.com',
    #             'cpf': '74185296332',
    #             'data_nascimento': '1987-02-02',
    #             'celular': '84988731798'
    #             }
    #     response = self.client.put(reverse('Estudantes-detail', kwargs={'pk': self.estudante.id}), data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.estudante.refresh_from_db()
    #     self.assertEqual(self.estudante.nome, 'Tossego Doszoi')