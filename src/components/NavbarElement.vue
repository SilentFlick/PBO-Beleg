<!-- <script>
</script>
<template>
    <nav class="navbar navbar-expand-lg navbar-light fixed-top" style="background-color: #e3f2fd">
        <div class="container-fluid">
            <router-link class="navbar-brand" to="/">HTW Talk</router-link>
            <div class="collapse navbar-collapse" id="navbarContent">
                <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
                    <li class="nav-item">
                        <router-link class="nav-item nav-link" to="/">Home </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-item nav-link" to="/post">Post </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-item nav-link" to="/about">About </router-link>
                    </li>
                </ul>
                <form class="d-flex">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
            </div>
            <button class="navbar-toggler"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#navbarContent"
                    aria-expanded="false"
                    aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
        </div>
    </nav>
</template> -->

<template>
  <div class="container-fluid">
    <div class="row">
      <!-- Side NavBar -->
      <TopNavBar />
      <SideBarLeft />
      <main class="col-8"><router-view /> Cards of Content</main>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import TopNavBar from "./TopNavBar.vue";
import SideBarLeft from "./SideBarLeft.vue";

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
</style>
