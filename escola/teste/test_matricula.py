from escola.models import Curso, Matricula, Estudante
from escola.serializers import CursoSerializer, MatriculaSerializer, EstudanteSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase, force_authenticate
from django.urls import reverse
from rest_framework import status


class MatriculaTestCase(APITestCase):
    def setUp(self):

        '''Criando um usuário para autenticação'''
        self.usuario = User.objects.create_superuser(username='Vampeta', password='vampirocomcapeta')
        self.client.force_authenticate(user=self.usuario)
        
        '''Criando Instância de Estudante'''
        self.estudante = Estudante.objects.create(nome = 'Ronaldinho Gaucho',
            email = 'eobruxonaotemjeito@gmail.com',
            cpf = '14925473018',
            data_nascimento = '1990-03-29',
            celular = '84 989731798'
        )
        '''Criando Instância de Curso'''
        self.curso = Curso.objects.create(
            codigo = 'TIWYWHITC',
            descricao = 'Musica do Worlds 2024, Faker pentacampeao, ave maria',
            nivel = 'A'
        )
        self.matricula = Matricula.objects.create(
            estudante =self.estudante,
            curso = self.curso,
            periodo='M'
            )
        
    def test_get_matriculas(self):
        '''Teste de GET para Matriculas'''
        response = self.client.get(reverse('matriculas-estudantes-list', args=[self.estudante.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 1)
        # self.assertEqual(response.data[0]['curso'], 'Musica do Worlds 2024 Faker pentacampeao ave maria')
        # self.assertEqual(response.data[0]['periodo'], 'Matutino')

    def test_post_matricula(self):
        '''Teste de POST para criar uma nova Matricula'''
        data = {
            'estudante': self.estudante.id,
            'curso': self.curso.id,
            'periodo': 'M'
            }
        response = self.client.post(reverse('Matriculas-list'), data, format='json')  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    
        self.assertEqual(Matricula.objects.count(), 2)  
        self.assertEqual(Matricula.objects.last().curso, self.curso)

    def test_put_matricula(self):
        '''Teste de PUT para atualizar uma Matricula existente'''
        matricula_id = self.matricula.id
        updated_data = {
            'estudante': self.estudante.id,
            'curso': self.curso.id,
            'periodo': 'V' 
            }
        response = self.client.put(reverse('Matriculas-detail', args=[matricula_id]), updated_data, format='json') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
        self.matricula.refresh_from_db() 
        self.assertEqual(self.matricula.periodo, 'V')

    def test_delete_matricula(self):
        '''Teste de DELETE para remover uma Matricula existente'''
        matricula_id = self.matricula.id
        response = self.client.delete(reverse('Matriculas-detail', args=[matricula_id]))  
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Matricula.objects.count(), 0)  