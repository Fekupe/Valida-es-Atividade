import datetime
from rest_framework import serializers
from escola.models import Estudante,Curso, Matricula
from datetime import date
from django.core.validators import MinLengthValidator

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','cpf','data_nascimento','celular']

    def validate_cpf(self, cpf: str) -> str: 
        if len(cpf) !=11:
            raise serializers.ValidationError('O CPF deve ter 11 dígitos')
        
        #Extrair os dígitos
        digits = [int(d) for d in cpf]

        #Calcular primeiro dígito de validação
        weights = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        soma1 = sum(d * w for d , w in zip(digits[:9], weights))
        resto1 = soma1 % 11
        first_check_digit = 0 if resto1 in [0,1] else 11 - resto1

        #Calcular o segundo dígito de validação
        weights2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        soma2 = sum(d * w for d, w in zip(digits[:10], weights2))
        resto2 = soma2 % 11
        second_check_digit = 0 if resto2 in [0,1] else 11 - resto2

        #Validação
        if digits [-2] == first_check_digit and digits [-1] == second_check_digit:
            return cpf
        else:
            raise serializers.ValidationError('CPF Inválido')
        
        
    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError('O nome deve conter apenas letras')
        return nome
    
    def validate_celular(self, celular):
        if len(celular) !=11:
            raise serializers.ValidationError('O Celular deve ter 11 dígitos com DDD')
        return celular 

    def validate_email(self, email):
        if '@' not in email:
            raise serializers.ValidationError('Insira um Email Válido')
        return email
    
    def validate_data_nascimento(self, data_nascimento):
        if data_nascimento > datetime.date.today():
            raise serializers.ValidationError('Informe uma data de nascimento válida')
        return data_nascimento 

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    def get_periodo(self,obj):
        return obj.get_periodo_display()

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'celular']
        
        
        