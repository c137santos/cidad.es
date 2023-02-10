<template>
  <div>
    <v-text-field label="Busque Estado ou Município" v-model="qtext"></v-text-field>
    
    <v-btn @click="buscar"> Buscar </v-btn>
  <div>
    Estado
    <div v-for="uf in estados" :key="uf"> 
      <div @click="abrirEstado(uf.id_ibge)">
        {{ uf.id_ibge }}
        {{ uf.nome }} - {{ uf.sigla }}
        {{ uf.metadado.regiao }}
      </div>
     </div>
     Municípios
    <div v-for="mcp in municipios" :key="mcp">
      <div @click="abrirMunicipio(mcp.id_ibge)">
        {{ mcp.nome }}
        {{mcp.uf_sigla }}    
      </div>
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
    abrirEstado(id_ibge){
      this.$router.push({name: "estado-detail", params:{"id_ibge":id_ibge}})
    },
    abrirMunicipio(id_ibge){
      this.$router.push({name: "municipio-detail", params:{"id_ibge":id_ibge}})
    },
    async buscar(){
      const resultadoDeEstados = await api.buscarEstado(this.qtext)
      this.estados = resultadoDeEstados.resultados
      const resultadoDeMunicipios = await api.buscarMunicipios(this.qtext)
      this.municipios = resultadoDeMunicipios.resultados
    }
  }
}
</script>
