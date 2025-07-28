import { createRouter, createWebHistory } from "vue-router";
import IniciarSesion from "../vistas/iniciar-sesion.vue";
import Inicio from "../vistas/inicio.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/iniciar-sesion",
      name: "iniciar-sesion",
      component: IniciarSesion,
    },
    {
      path: "/inicio",
      name: "inicio",
      component: Inicio,
    },
  ],
});

export default router;
