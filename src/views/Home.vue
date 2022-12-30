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
      :postID="post_id"
      :username="name"
      :faculty="faculty"
      :content="content"
      :title="title"
      :created_at="created_at"
      :comments="comments.filter((comment) => comment.post_id === post_id)"
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
      comments: [],
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
    getComments: async function () {
      return (this.comments = await sendRequest("GET", "comments", null).then(
        (res) => {
          return res;
        }
      ));
    },
  },

  created() {
    this.getPosts();
    this.getComments();
  },
};
</script>
