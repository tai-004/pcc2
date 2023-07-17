from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save, post_delete

#doação de campanha de objetos
class DoacaoCampanhaObj(models.Model):
    CATEGORIA_CHOICES = [
        ["material de limpeza", "material de limpeza"],
        ["roupa", "roupa"],
        ["brinquedo", "brinquedo"],
        ["outros", "outros"]
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.CharField(max_length=100,choices=CATEGORIA_CHOICES,  null=True)
    outro = models.CharField(max_length=150, null=True, blank=True)
    descricao = models.TextField(max_length=100, null=True, blank=True)
    finalidade = models.TextField(max_length=500, null=True, blank=True)
    cidade = models.CharField(max_length=150, null=True)
    estado = models.CharField(max_length=150, null=True)
    rua = models.CharField(max_length=150, null=True)
    numero = models.CharField(max_length=10, null=True)
    bairro = models.CharField(max_length=150, null=True)
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    cont = models.IntegerField(default=0)
    
    class Meta:
         permissions = (("user", "user"), )
    def __str__(self):
        return self.titulo


#parte da notificação
class DoeUser(models.Model):
    DOE = ((1, 'Doacao'), )
    doacao = models.ForeignKey(DoacaoCampanhaObj, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dataEntrega = models.CharField(max_length=150, null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    doe = models.IntegerField(choices=DOE, blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='DoarUser')
    
    class Meta:
         permissions = (("user", "user"), )
    def __str__(self):
        return self.user.username


 
#produto na notificação de doação
class TabelarDoe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_doar')
    doacao = models.ForeignKey(DoacaoCampanhaObj,  null=True, on_delete=models.CASCADE, related_name='doe_indorma')
     
    def DoaTabela(sender, instance, *args, **kwargs):
        favori = instance
        doacao = favori.doacao
        sender = favori.user
        noti = DoeUser(doacao=doacao, sender=sender, user=doacao.user, doe=1)
        noti.save()
    def __str__(self):
        return self.user.username
post_save.connect(TabelarDoe.DoaTabela, sender=TabelarDoe)


#doação em dinheiro
class DoacaoCampanhaDinheiro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField(max_length=1000, null=True, blank=True)
    chavePix = models.TextField(max_length=500, null=True, blank=True)
    nomeChave = models.CharField(max_length=500, null=True)
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    class Meta:
         permissions = (("chave", "chave"),)
    def __str__(self):
        return self.titulo

    