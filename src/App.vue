<template>
  <div>
    <section class="main-navbar-section">
      <NavbarElement></NavbarElement>
    </section>
    <section class="main-content-section">
      <div class="container"></div>
    </section>
  </div>
</template>

<script>
import NavbarElement from "@/components/NavbarElement.vue";

export default {
  components: {
    NavbarElement,
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
}

.main-content-section {
  min-height: 100%;
}

.main-navbar-section {
  z-index: 1;
  width: 100%;
}
</style>
