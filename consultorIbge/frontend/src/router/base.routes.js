// Composables
import EmptyLayout from "@/layouts/default/EmptyLayout.vue"
import HomeView from "@/views/base/HomeView.vue"
import EstadoDetail from "@/views/base/EstadoDetail.vue"
import MunicipioDetail from "@/views/base/MunicipioDetail.vue"


export default [
  {
    path: "/",
    component: EmptyLayout,
    children: [
      {
        path: "",
        name: "base-home",
        component: HomeView,
      },
      {
        path: "estado/:id_ibge",
        name: "estado-detail",
        component: EstadoDetail,
      },
      {
        path: "municipio/:id_ibge",
        name: "municipio-detail",
        component: MunicipioDetail,
      },
    ],
  },
]
