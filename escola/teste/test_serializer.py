from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer
from django.urls import reverse

class EstudanteSerializerTest(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Raimundo Neto',
            email = 'raimundonetolindodemamae@gmail.com',
            cpf = '98765432145',
            data_nascimento = '2002-06-06',
            celular = '84 988721697'
        )
        self.serializer = EstudanteSerializer(instance=self.estudante)

    def test_serialization(self):
        expect_data = {
            'id' : self.estudante.id,
            'nome': 'Raimundo Neto',
            'email': 'raimundonetolindodemamae@gmail.com',
            'cpf' : '98765432145',
            'data_nascimento' : '2002-06-06',
            'celular' : '84 988721697'
        }
        self.assertEqual(self.serializer.data, expect_data)


# class EstudanteAPITest(APITestCase):
#     def setUp(self):
#         self.create_url = reverse('Estudantes-list')
#         self.estudante = Estudante.objects.create(
#             nome = 'Raimundo Neto',
#             email = 'raimundonetolindodemamae@gmail.com',
#             cpf = '98765432145',
#             data_nascimento = '2002-06-06',
#             celular = '84 988721697'
#         )

#     def test_get_estudante(self):
#         create_response = self.client.post(self.create_url, self.estudante, format='json')
#         self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

#         student_id= create_response.data['id']

#         detail_url = reverse('Estudantes-detail', kwargs={'pk': student_id})
#         get_response = self.client.get(detail_url)

#         # response = self.client.get(f'http://localhost:8000/estudantes/<20>/{self.estudante.id}/')  
        
#         self.assertEqual(get_response.status_code, status.HTTP_200_OK)

#         expect_data = {
#             'id' : student_id,
#             'nome': 'Raimundo Neto',
#             'email': 'raimundonetolindodemamae@gmail.com',
#             'cpf' : '98765432145',
#             'data_nascimento' : '2002-06-06',
#             'celular' : '84 988721697'
#         }
#         self.assertEqual(get_response.data, expect_data)

    #     def test_list_estudantes(self):
    #         self.client.post(self.create_url, self.student_data, format='json')
        
    #     # Get the list of students
    #         list_url = reverse('Estudantes-list')
    #         response = self.client.get(list_url)
        
    #         self.assertEqual(response.status_code, status.HTTP_200_OK)
    #         self.assertEqual(len(response.data), 1)  # Verify that there is one student in the list
    #         self.assertEqual(response.data[0]['nome'], 'Raimundo Neto')  # Verify the student's name

    # # Optional: Test invalid data
    # def test_create_invalid_estudante(self):
    #     invalid_data = {
    #         'nome': '',  # Invalid empty name
    #         'email': 'invalid-email',  # Invalid email format
    #         'cpf': '123',  # Invalid CPF
    #         'data_nascimento': '2002-13-45',  # Invalid date
    #         'celular': '123'  # Invalid phone number
    #     }
        
    #     response = self.client.post(self.create_url, invalid_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)