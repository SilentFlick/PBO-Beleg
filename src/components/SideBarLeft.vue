<template>
  <div
    class="d-flex flex-column flex-shrink-0 p-3 bg-dark col-2 align-items-center sidebar-left"
  >
    <ul
      class="nav nav-pills flex-column position-fixed float-left"
      style="width: 150px"
    >
      <li class="nav-item">
        <a href="/" class="nav-link text-white active" aria-current="page">
          Home
        </a>
      </li>
      <li>
        <a href="/post" class="nav-link text-white link-dark">
          Create a Post
        </a>
      </li>
      <li>
        <a href="#" class="nav-link text-white link-dark"> Selection </a>
      </li>
      <li>
        <a href="#" class="nav-link text-white link-dark"> Q&A </a>
      </li>
      <li>
        <a href="/about" class="nav-link text-white link-dark">
          Help/Support
        </a>
      </li>
    </ul>
    <hr />
  </div>
</template>
<style scoped>
.sidebar-left {
  height: 100vh;
}
</style>
