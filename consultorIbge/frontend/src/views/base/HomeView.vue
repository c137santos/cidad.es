<template>
  <div>
    <v-text-field label="Busque Estado ou Município" v-model="qtext"></v-text-field>
    
    <v-btn @click="buscar"> Buscar </v-btn>
  <div>
    Estado
    <div v-for="uf in estados" :key="uf"> 
      {{ uf.nome }} - {{ uf.sigla }}
      {{ uf.id_ibge }}
      {{ uf.metadado.regiao }}
     </div>
     Municípios
    <div v-for="mcp in municipios" :key="mcp"> 
      {{ mcp.nome }}
      {{mcp.uf_sigla }}
    </div>
  </div>
  </div>
</template>


<script>
import api from "@/api/buscas"

export default {
  data(){
    return{
      qtext: "",
      estados: [],
      municipios: []
    }
  },
  methods: {
    async buscar(){
      const resultadoDeEstados = await api.buscarEstado(this.qtext)
      this.estados = resultadoDeEstados.resultados
      const resultadoDeMunicipios = await api.buscarMunicipios(this.qtext)
      this.municipios = resultadoDeMunicipios.resultados
    }
  }
}
</script>
