<template>
  <!-- Top NavBar -->
  <header class="navbar">
    <nav class="d-flex justify-content-between align-items-center">
      <button class="btn" id="burgerMenu" @click="toggleSidebar">
        <i class="bi bi-list fa-lg"></i>
      </button>
      <a class="navbar-brand" style="color: white">HTW Talk</a>
      <form role="search">
        <Search />
      </form>
      <button
        v-if="!isLogin"
        id="login-btn"
        type="button"
        class="btn btn-primary"
        data-bs-toggle="modal"
        data-bs-target="#login"
      >
        Login
      </button>
      <button
        v-else
        id="logout-btn"
        type="button"
        class="btn btn-secondary"
        @click="logout"
      >
        Logout
      </button>
    </nav>
  </header>
</template>

<script>
import Search from "./Search.vue";

export default {
  name: "TopNavBar",
  components: {
    Search,
  },
  inject: ["loginStatus", "loginHandle"],
  data() {
    return {
      isLogin: this.loginStatus,
    };
  },
  methods: {
    toggleSidebar() {
      const sidebar = document.getElementById("sidebarDropdown");
      if (sidebar.style.display === "none") {
        sidebar.style.display = "block";
      } else {
        sidebar.style.display = "none";
      }
    },
    logout() {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i];
        const eqPos = cookie.indexOf("=");
        const name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
      }
      this.loginHandle();
    },
  },
  watch: {
    $route: function () {
      document.getElementById("sidebarDropdown").style.display = "none";
    },
    $window: function () {
      document.getElementById("sidebarDropdown").style.display = "none";
    },
  },
};
</script>

<style scoped>
header {
  margin: 0px;
  padding: 0px 30px;
  width: 100%;
  height: 100%;
  background-size: 100% 100%;
  background: rgb(41, 21, 56);
  background: linear-gradient(
    146deg,
    rgba(41, 21, 56, 1) 51%,
    rgba(172, 113, 49, 1) 73%
  );
}

nav {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

button {
  padding: 10px 10px;
}

.form-control {
  margin: 10px;
  width: 500px;
  height: 50px;
}

#burgerMenu {
  display: none;
}

@media screen and (max-width: 900px) {
  #burgerMenu {
    display: block;
    color: white;
    font-size: 30px;
  }
  .navbar-brand {
    display: none;
  }
}
</style>
