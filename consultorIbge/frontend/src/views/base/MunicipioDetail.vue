<template>
  <div>
    <div class="text-center titulo">
      <h1>Informações sobre Município de {{ nome }}</h1>
    </div>
    <v-card class="mx-auto text-center cardzinhos" max-width="500" >
      <v-card-text >
        <p class="text-h4 text--primary">{{ nome }} - {{ sigla }} </p>
        <p>Sigla: {{ sigla }} </p>
        <p>Região: {{ regiao }} </p>
        <p>PIB: {{ pib }} </p>
        <p>IDH: {{ idh }}</p>
        <p>Extensão Territorial: {{ extensaoTerritorial }} </p>
        <p>População Estimada: {{ populacaoEstimada }} </p>
        <p>Densidade demográfica: {{ densidade_demografica }}</p>
      </v-card-text>
    </v-card>
    <p class="rodapezim"> Acesse nossa API por meio de /api/municipio/{{id_ibge}}/detail/</p>
  </div>
</template>

<script>
import api from "@/api/buscas"

export default {
  data() {
    return {
      nome: "",
      sigla: "",
      regiao:"",
      pib: "",
      idh: "",
      extensaoTerritorial:"",
      populacaoEstimada:"",
      municipios:"",
      densidade_demografica:""
    }
  },
  mounted() {
    api.buscaDetailMunicipio(this.id_ibge).then((response)=>{
      this.nome = response.nome
      this.sigla = response.sigla
      this.regiao = response.metadado.regiao
      this.pib = response.metadado.pib
      this.idh = response.metadado.idh
      this.extensaoTerritorial = response.metadado.extensao_territorial
      this.populacaoEstimada = response.metadado.populacao_estimada
      this.densidade_demografica = response.metadado.densidade_demografica
      this.municipios = response.total_municipios
    })
  },
computed : {
  id_ibge(){
    return this.$route.params.id_ibge
  }
  }    
}
</script>

<style>
p{
  font-size: 25px;
  margin: 2%;
}

.cardzinhos{
  margin: 2%;
}

.titulo{
  margin: 5%;

}

.rodapezim{
  font-size: 20px;
  position: absolute;
  margin-bottom: 0 ;
}

</style>