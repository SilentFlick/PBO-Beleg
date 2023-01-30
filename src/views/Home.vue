<template>
  <div class="container">
    <div
      v-if="posts.length === 0"
      class="container d-flex justify-content-center w-100"
    >
      <div
        class="spinner-grow text-secondary"
        style="width: 3rem; height: 3rem; margin-top: 20px"
      ></div>
    </div>
    <div v-else class="w-100">
      <Card
        v-for="{
          post_id,
          from_user,
          to_user,
          faculty,
          content,
          title,
          name,
          created_at,
        } in posts.sort(
          (a, b) =>
            new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
        )"
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
          const autocompleteData = JSON.stringify(
            res.map((r) => {
              return { content: r.content, title: r.title, post_id: r.post_id };
            })
          );
          localStorage.setItem("autocompleteData", autocompleteData);
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
