<template>
  <div
    class="d-flex align-items-center sidebar-container sticky-top"
    id="sidebar-container"
  >
    <ul class="nav nav-pills container-fluid" id="sidebarList">
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
          class="nav-item nav-link text-dark d-flex"
          to="/faq"
        >
          <i class="bi bi-question-square"></i>
          FAQ
        </router-link>
      </li>
    </ul>
    <ul class="nav nav-pills container-fluid" id="sidebarDropdown">
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
          class="nav-item nav-link text-dark d-flex"
          to="/faq"
        >
          <i class="bi bi-question-square"></i>
          FAQ
        </router-link>
      </li>
    </ul>
  </div>
</template>
<style scoped>
.sidebar-container {
  height: 100vh;
  width: auto;
  border-right: solid 2px black;
  flex-direction: column;
}

.nav a {
  font-weight: lighter;
}

#sidebarList {
  display: block;
  flex-direction: column;
}

#sidebarDropdown {
  display: none;
}

@media screen and (max-width: 900px) {
  .sidebar-container {
    height: auto;
    width: 75%;
    border: none;
    z-index: 1;
    position: absolute;
    background: white;
    transform: translateY(67px);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
  }
  #sidebarList {
    display: none;
  }

  #sidebarDropdown {
    padding: 5px;
    margin: 0px;
    display: none;
    flex-direction: column;
  }
}
</style>
