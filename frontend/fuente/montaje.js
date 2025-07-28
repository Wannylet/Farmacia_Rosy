import { createApp } from "vue";
import virtual from "./virtual.vue";
import router from "./routers/router";

createApp(virtual).use(router).mount("#montaje");
