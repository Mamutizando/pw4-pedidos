from django.db import models


class Categoria(models.Model):

    nome = models.CharField(max_length=30, verbose_name="Nome")
    
    class Meta:
        vebose_name = "Categoria"
        vebose_name_plural = "Categorias"

    def _str_(self):
        return self.nome

class Produto(models.Model):

    LITROS = "LT"
    GRAMAS = "GR"
    KILOS = "KG"
    UNIDADE = "UND"
    PECA = "PC"
    UNIDADES = [
        (LITROS, "Litros"),
        (GRAMAS, "Gramas"),
        (KILOS, "Kilos"),
        (UNIDADE, "Unidade"),
        (PECA, "Peça"),
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome") 
    valor = models.DecimalField(max_length=10, decimal_places=2, verbose_name="Valor")
    categoria = models.ForeignKey(
        "produtos.Categoria",
        verbose_name="Categoria",
        on_delete = models.CASCADE
    )
    nome = models.CharField(max_length=3, choices=UNIDADES) 

    class Meta:
        vebose_name = "Produto"
        vebose_name_plural = "Produtos"

    def _str_(self):
        return self.nome