<template>
  <div>
  <navbar-element></navbar-element>
  </div>
  <div>
  <router-view/>
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

<style lang="scss"></style>
