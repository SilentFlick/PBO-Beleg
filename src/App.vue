<template>
    <div id="app">
        <section class="main-navbar-section">
            <div class="container">
                <navbar-element></navbar-element>
            </div>
        </section>
        <section class="main-content-section">
            <div class="container">
                <router-view/>
            </div>
        </section>
    </div>
</template>

<script>
 import NavbarElement from "@/components/NavbarElement.vue";

 export default {
     components: {
         NavbarElement
     }
 }
</script>

<style lang="scss">
 html {
     width: 100%;
     font-size: 18px;
     color: #333;
 }

 body {
     margin: 0;
     padding-top: 3%;
     height: 100%;
     height: 100vh;
     width: 100%;
     font-family: sans-serif;
 }

 #app {
     height: 100%;
     height: 100vh;
     width: 100%;
     line-height: 1.5;
 }

 .main-content-section {
     min-height: 100%;
 }

 .main-navbar-section {
     z-index:1;
     width:100%;
     height:50px;
     text-align:center;
     vertical-align:middle;
     line-height:50px;
     top:0px;
 }
</style>
