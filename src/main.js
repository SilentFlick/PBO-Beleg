import { createApp } from "vue";
import App from "./App.vue";
import router from "@/router";

import * as bootstrap from "bootstrap";
import "@/scss/styles.scss";

createApp(App).use(router).mount("#app");
