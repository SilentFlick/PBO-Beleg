<template>
  <div
    class="d-flex flex-shrink-0 p-3 align-items-center sidebar-left"
    id="sidebarLine"
  >
    <ul class="nav nav-pills container-fluid" id="sidebarLeft">
      <li>
        <router-link
          tag="li"
          active-class="active text-white bg-dark"
          class="nav-item nav-link text-dark"
          to="/"
        >
          <!-- Icon from https://icons.getbootstrap.com/ -->
          <i class="bi bi-house"></i>
          Main
        </router-link>
      </li>
      <li>
        <router-link
          active-class="active text-white bg-dark"
          class="nav-item nav-link text-dark"
          to="/post"
        >
          <i class="bi bi-plus-square"></i>
          Post
        </router-link>
      </li>
      <li>
        <router-link
          active-class="active text-white bg-dark"
          class="nav-item nav-link text-dark d-flex justify-content-between"
          to="/faq"
        >
          <i class="bi bi-question-square"></i>
          FAQ
        </router-link>
      </li>
    </ul>
    <hr />
  </div>
</template>
<style scoped>
.sidebar-left {
  height: 100vh;
  width: auto;
  border-right: solid 2px black;
  flex-direction: column;
}

.nav a {
  font-weight: lighter;
}

#sidebarLeft {
  display: inline-flex;
  flex-direction: column;
}

i {
  margin: 0 10px 0 0;
}

@media screen and (max-width: 900px) {
  .sidebar-left {
    border-right: none;
    height: 30%;
    width: auto;
    padding: 0px;
  }

  #sidebarLeft {
    display: inline-flex;
    flex-direction: row;
  }
}

@media screen and (max-width: 600px) {
  .sidebar-left {
    border-right: none;
    height: 30%;
    width: auto;
    padding: 0px;
  }

  #sidebarLeft {
    display: inline-flex;
    flex-direction: row;
  }
}
</style>
