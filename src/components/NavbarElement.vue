<template>
  <div class="container-fluid">
    <div class="row">
      <!-- Side NavBar -->
      <TopNavBar />
      <SideBarLeft />
      <main class="col-lg-10"><router-view /></main>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import TopNavBar from "@/components/TopNavBar.vue";
import SideBarLeft from "@/components/SideBarLeft.vue";

export default {
  name: "HomeView",
  components: {
    TopNavBar,
    SideBarLeft,
  },
};
</script>

<style scoped>
row {
  margin: 0;
  padding: 0;
  width: 100%;
}

body {
  position: relative;
  height: auto;
  min-height: 100vh;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  overflow: hidden;
  margin: 0;
}
</style>
