<template>
  <div>
<div> {{ nome }}</div>
      nome: {{ nome }}
      sigla: {{ sigla }}
      regiao: {{ regiao }}
      pib: {{ pib }}
      idh: {{ idh }}
      extensaoTerritorial: {{ extensaoTerritorial }}
      populacaoEstimada: {{ populacaoEstimada }}
      densidade_demografica: {{ densidade_demografica }}
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
