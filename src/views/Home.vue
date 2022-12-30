<template>
  <div class="container-fluid">
    <h1>Home</h1>
    <Card
      v-if="posts.length > 0"
      v-for="{
        post_id,
        from_user,
        to_user,
        faculty,
        content,
        title,
        name,
        created_at,
      } in posts"
      :key="post_id"
      :username="name"
      :faculty="faculty"
      :content="content"
      :title="title"
      :created_at="created_at"
    />
  </div>
</template>

<script>
import Card from "../components/Card.vue";
import { sendRequest } from "../api/sendRequest.js";

export default {
  name: "Home",

  components: { Card },

  data() {
    return {
      posts: [],
    };
  },

  methods: {
    getPosts: async function () {
      return (this.posts = await sendRequest("GET", "posts", null).then(
        (res) => {
          return res;
        }
      ));
    },
  },

  created() {
    this.getPosts();
  },
};
</script>
