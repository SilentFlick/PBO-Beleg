<script setup></script>

<template>
  <!-- Top NavBar -->
  <header class="navbar sticky-top">
    <nav class="container-fluid flex-wrap">
      <a class="navbar-brand">HTW Shits Talk</a>
      <form class="" role="search">
        <input
          class="form-control"
          type="search"
          placeholder="Search"
          aria-label="Search"
        />
      </form>

      <button
        type="button"
        class="btn btn-info"
        data-bs-toggle="modal"
        data-bs-target="#login"
      >
        Login
      </button>
    </nav>
  </header>
</template>

<script>
import Login from "@/components/Login.vue";
export default {
  components: { Login },
};
</script>

<style scoped>
header {
  margin: 0;
  padding: 0 30px;
  width: 100%;
  background-color: #f99b1c;
}
nav {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
button {
  padding: 10px 30px;
}
.form-control {
  margin: 10px;
  width: 500px;
  height: 50px;
}
</style>
