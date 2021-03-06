from django.db import models

class Item(models.Model):

    pedido = models.ForeignKey(
        "pedidos.Pedido",
        verbose_name="Pedido",
        on_delete = models.CASCADE
    )
    produto = models.ForeignKey(
        "produtos.Produto",
        verbose_name="Produto",
        on_delete = models.CASCADE
    )
    quantidade = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Quantidade") 
    valor_base = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Base") 
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Subtotal") 
    
    class Meta:
        vebose_name = "Item"
        vebose_name_plural = "Itens"

    def _str_(self):
        return "#" + str(self.pedido.id) + " " + self.produto.nome

class Pedido(models.Model):

    CRIADO = "CRD"
    FECHADO = "FCD"
    ENVIADO = "EVD"
    STATUSES = [
        (CRIADO, "Criado"),
        (FECHADO, "Fechado"),
        (ENVIADO, "Enviado")
    ]

    cliente = models.ForeignKey(
        "clientes.Cliente",
        verbose_name="Cliente",
        on_delete = models.CASCADE
    )
    data = models.DateField(verbose_name="Data") 
    criado = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total") 
    status = models.CharField(max_length=5, choices=STATUSES, default=CRIADO, verbose_name="Status") 
    itens = models.ManyToManyField("produtos.Produto", verbose_name="Itens", through=Item)

    class Meta:
        vebose_name = "Pedido"
        vebose_name_plural = "Pedidos"

    def _str_(self):
        return "#" + str(self.id) + " " + self.cliente.nome