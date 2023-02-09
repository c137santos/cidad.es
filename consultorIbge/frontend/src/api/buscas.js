import api from "./config.js"
import apiHelpers from "./helpers.js"

export default {
  buscarEstado: (q) => {
    return new Promise((resolve, reject) => {
      api
        .get("api/search/", {params:{"q":q}})
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  buscarMunicipios: (q) => {
    return new Promise((resolve, reject) => {
      api
        .get("api/search/municipio/", {params:{"q":q}})
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
}
}
