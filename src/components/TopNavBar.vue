<template>
    <!-- Top NavBar -->
    <header class="navbar navbar-expand topbar mb-4 shadow">
        <nav class="d-flex justify-content-between align-items-center">
            <button class="btn" id="burgerMenu" @click="toggleSidebar">
                <i class="bi bi-list"></i>
            </button>
            <a class="navbar-brand" style="color: white">HTW Shits Talk</a>
            <form class="" role="search">
                <input
                    class="form-control"
                    type="search"
                    placeholder="Search"
                    aria-label="Search"
                />
            </form>

            <button
                id="login-btn"
                type="button"
                class="btn btn-primary"
                data-bs-toggle="modal"
                data-bs-target="#login"
                v-if="!isLogin"
            >
                Login
            </button>
            <button
                type="button"
                class="btn btn-secondary"
                @click="logout"
                v-else
            >
                Logout
            </button>
        </nav>
    </header>
</template>

<script>
 import FAQ from "../views/FAQ.vue";
 export default {
     components: { FAQ },
     name: "TopNavBar",
     inject: ['loginStatus', 'loginHandle'],
     data() {
         return{
             isLogin: this.loginStatus
         }
     },
     methods:{
         toggleSidebar(){
             var sidebar = document.getElementById("sidebarLeft");
             if(sidebar.style.display === "inline-flex") {
                 sidebar.style.display = "none";
             } else {
                 sidebar.style.display = "inline-flex";
             }
         },
         logout(){
             document.cookie ="username=" + ";SameSite=Strict;Secure";
             this.loginHandle();
         }
     }
 };
</script>

<style scoped>
 header {
     margin: 0px;
     padding: 0px 30px;
     width: 100%;
     height: 100%;
     background-size: 100% 100%;
     background: rgb(41,21,56);
     background: linear-gradient(146deg, rgba(41,21,56,1) 51%, rgba(172,113,49,1) 73%);
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

 #burgerMenu {
     display: none;
 }

 @media screen and (max-width: 600px) {
     #burgerMenu {
         background-color: none;
         display: block;
     }
 }

 @media screen and (max-width: 900px) {
     #burgerMenu {
         background-color: none;
         display: block;
     }
 }
</style>
