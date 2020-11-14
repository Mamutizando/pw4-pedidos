from django.db import models


class Cliente(models.Model):

    nome = models.CharField(max_length=254, verbose_name="Nome")
    endereco = models.CharField(max_length=254, verbose_name="Endereço")
    numero = models.CharField(max_length=10, verbose_name="Número")
    complemento = models.CharField(max_length=50, verbose_name="Complemento", blanck=True)
    bairro = models.CharField(max_length=50, verbose_name="Bairro")
    cidade = models.CharField(max_length=254, verbose_name="Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    telefone = models.CharField(max_length=19, verbose_name="Telefone fixo", blanck=True)
    celular = models.CharField(max_length=19, verbose_name="Celular", blanck=True)
    rg = models.CharField(max_length=15, verbose_name="RG")
    cpf = models.CharField(max_length=15, verbose_name="CPF")
    data_nascimento = models.DateField(verbose_name="Data de nascimento")
    email = models.EmailField(max_length=254, verbose_name="Email")

    class Meta:
        vebose_name = 'Cliente'
        vebose_name_plural = 'Clientes'

    def _str_(self):
        return self.nome