<template>
<v-text-field label="Busque Estado ou Município" v-model="qtext"></v-text-field>

<v-btn @click="buscar"> Buscar </v-btn>

</template>


<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"
import api from "@/api/buscas"

export default {
  computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
  },
  data(){
    return{
      qtext: "",
      estados: []
    }
  },
  methods: {
    async buscar(){
      const resultado = await api.buscarEstado(this.qtext)
    }
  }
}
</script>

<style scoped>

</style>