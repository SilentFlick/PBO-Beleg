<template>
  <div>
    <section class="main-navbar-section">
      <NavbarElement />
    </section>
    <section class="main-content-section">
      <div class="container"></div>
    </section>
    <Login @isLogin="loginHandle" />
  </div>
</template>

<script>
import NavbarElement from "@/components/NavbarElement.vue";
import Login from "@/components/Login.vue";
import { computed } from "@vue/runtime-core";

export default {
  name: "App",
  components: {
    NavbarElement,
    Login,
  },
  data() {
    return {
      isLogin:
        document.cookie.indexOf("username") !== -1 &&
        document.cookie.valueOf("username").split("=")[1].length !== 0,
    };
  },
  methods: {
    loginHandle() {
      this.isLogin =
        document.cookie.valueOf("username").split("=")[1].length !== 0;
    },
  },
  provide() {
    return {
      loginStatus: computed(() => this.isLogin),
      loginHandle: this.loginHandle,
    };
  },
};
</script>

<style lang="scss">
html {
  width: 100%;
  font-size: 18px;
  color: #333;
}

body {
  margin: 0;
  height: 100%;
  width: 100%;
  font-family: sans-serif;
}

#app {
  height: 100%;
  width: 100%;
  line-height: 1.5;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.main-content-section {
  min-height: 100%;
}

.main-navbar-section {
  z-index: 1;
  width: 100%;
}
</style>
