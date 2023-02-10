<template>
  <div>
    <v-card class="mx-auto " max-width="344" >
      <v-card-text >
      <div>Município de {{ nome }}</div>
        <p class="text-h4 text--primary">{{ nome }} - {{ sigla }} </p>
        <p>sigla: {{ sigla }} </p>
        <p>regiao: {{ regiao }} </p>
        <p>pib: {{ pib }} </p>
        <p>idh: {{ idh }}</p>
        <p>extensaoTerritorial: {{ extensaoTerritorial }} </p>
        <p>populacaoEstimada: {{ populacaoEstimada }} </p>
        <p>densidade_demografica: {{ densidade_demografica }}</p>
      </v-card-text>
    </v-card>
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
