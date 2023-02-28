<template>
  <div>
    <div class="text-center titulo">
      <h1> Cidad.es: </h1>
      <h2>API de informações geográficas brasileiras simples e organizadas</h2>
    </div>
    <div class="centralizadora">
      <v-text-field class="campoDeBusca" label="Busque Estado ou Município" v-model="qtext"></v-text-field>
      <v-btn @click="buscar"> Buscar </v-btn>
    </div>

    <div>

    <v-card class="mx-auto cardzinhos" max-width="344">
      <v-card-text v-for="uf in estados" :key="uf" >
      <div>Unidade Federativa do {{ uf.metadado.regiao }}</div>
        <p class="text-h4 text--primary">{{ uf.nome }} - {{ uf.sigla }} </p>
        <v-btn @click="abrirEstado(uf.id_ibge)"> Mais detalhes </v-btn>
      </v-card-text>
    </v-card>

    <v-card class="mx-auto cardzinhos" max-width="344" >
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
      if (this.qtext.length == 0 || this.qtext == null) {
        return
      }
      const resultadoDeEstados = await api.buscarEstado(this.qtext)
      this.estados = resultadoDeEstados.resultados
      const resultadoDeMunicipios = await api.buscarMunicipios(this.qtext)
      this.municipios = resultadoDeMunicipios.resultados
    }
  }
}
</script>

<style scoped>

.campoDeBusca{
    width: 50%;
    display: flex;
    flex-direction: column;
    text-align: center;
}
.centralizadora {
  display: flex;
  margin-top: 5%;
  flex-direction: column;
  align-items: center;
}

.cardzinhos{
  margin: 2%;
}
.titulo{
  margin-top: 3%;
}
</style>