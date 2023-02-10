<template>
  <div>
    <v-text-field label="Busque Estado ou Município" v-model="qtext"></v-text-field>
    
    <v-btn @click="buscar"> Buscar </v-btn>
  <div>
  <v-card class="mx-auto" max-width="344" >
    <v-card-text v-for="uf in estados" :key="uf">
    <div>Unidade Federativa do {{ uf.metadado.regiao }}</div>
      <p class="text-h4 text--primary">{{ uf.nome }} - {{ uf.sigla }} </p>
      <v-btn @click="abrirEstado(uf.id_ibge)"> Mais detalhes </v-btn>
    </v-card-text>
  </v-card>

  <v-card class="mx-auto" max-width="344" >
    <v-card-text v-for="mcp in municipios" :key="mcp">
    <div>Município de {{mcp.uf.nome}}</div>
      <p class="text-h4 text--primary">{{ mcp.nome }} - {{ mcp.uf_sigla}} </p>
      <v-btn @click="abrirMunicipio(mcp.id_ibge)"> Mais detalhes </v-btn>
    </v-card-text>
  </v-card>
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
