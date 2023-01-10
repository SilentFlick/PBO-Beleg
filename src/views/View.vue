<template>
  <div
    v-if="post.length === 0"
    class="container d-flex justify-content-center w-100"
  >
    <div
      class="spinner-grow text-secondary"
      style="width: 3rem; height: 3rem; margin-top: 20px"
    ></div>
  </div>
  <Card
    v-else
    :postID="post.post_id"
    :username="post.name"
    :faculty="post.faculty"
    :content="post.content"
    :title="post.title"
    :created_at="post.created_at"
    :comments="comments.filter((comment) => comment.post_id === post.post_id)"
  />
</template>

<script>
import Card from "../components/Card.vue";
import { sendRequest } from "../api/sendRequest";
export default {
  name: "View",
  components: {
    Card,
  },
  data() {
    return {
      post: [],
      comments: [],
    };
  },
  watch: {
    $route: function () {
      this.getLoadedPost();
      this.getComments();
    },
  },
  methods: {
    getLoadedPost: async function () {
      return (this.post = await sendRequest(
        "GET",
        `post/${this.$route.path.split("/")[2]}`,
        null
      ).then((res) => {
        return res;
      }));
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
    this.getLoadedPost();
    this.getComments();
  },
};
</script>

<style></style>
