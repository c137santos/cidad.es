from django.db import models

# Melhorar região para que tenha opções

class Metadado(models.Model):
    regiao = models.CharField(max_length=25, blank=True)
    pib = models.FloatField()
    idh = models.FloatField()
    extensao_territorial = models.FloatField()
    densidade_demografica = models.FloatField()
    populacao_estimada = models.IntegerField(default=0)

    def to_dict_json(self):
        return {
            'id': self.id,
            'regiao': self.regiao,
            'pib': self.pib,
            'idh': self.idh,
            'extensao_territorial': self.extensao_territorial,
            'densidade_demografica': self.densidade_demografica,
            'populacao_estimada': self.populacao_estimada,
        }

    def __str__(self):
        return str(self.id)


class UF(models.Model):
    id_ibge = models.IntegerField(primary_key=True)
    metadado = models.ForeignKey(Metadado, on_delete=models.PROTECT)
    nome = models.TextField()
    sigla = models.TextField()

    def to_dict_json(self):
        return {
            'metadado': self.metadado.to_dict_json(),
            'nome': self.nome,
            'sigla': self.sigla,            
            'id_ibge': self.id_ibge,            
        }

    def __str__(self):
        return str(self.nome)


class Municipio(models.Model):
    id_ibge = models.IntegerField(primary_key=True)
    metadado = models.ForeignKey(Metadado, on_delete=models.PROTECT)
    nome = models.TextField()
    uf = models.ForeignKey(UF, on_delete=models.CASCADE)
    uf_sigla = models.TextField()

    def to_dict_json(self):
        return {
            'metadado': self.metadado.to_dict_json(), 
            'nome': self.nome,
            'uf': self.uf.to_dict_json(),
            'uf_sigla': self.uf_sigla,
            'id_ibge': self.id_ibge,  
        }

    def __str__(self):
        return str(self.nome)