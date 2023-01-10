import { createApp } from "vue";
import App from "./App.vue";
import router from "@/router";
import VueCookies from "vue-cookies";

import * as bootstrap from "bootstrap";
import "@/scss/styles.scss";

createApp(App).use(router).use(VueCookies).mount("#app");
