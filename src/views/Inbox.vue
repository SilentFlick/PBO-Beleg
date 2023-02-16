<template>
  <div class="container">
    <div
      v-if="posts.length === 0"
      class="container d-flex justify-content-center w-100"
    >
      <div
        class="spinner-grow text-secondary"
        style="width: 3rem; height: 3rem; margin-top: 20px"
        v-if="flag"
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
          comments,
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
        :commentsData="comments"
      />
    </div>
  </div>
  <div
    class="position-fixed top-10 start-50 translate-middle-x p-3"
    style="z-index: 11"
  >
    <div
      id="success"
      class="toast hide"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
    >
      <div class="toast-body bg-info text-black">The inbox is empty.</div>
    </div>
  </div>
</template>
>

<script>
import Card from "@/components/Card.vue";
import { sendRequest } from "@/api/sendRequest.js";

export default {
  name: "Inbox",

  components: { Card },
  inject: ["getLoginData"],
  data() {
    return {
      posts: [],
      data: this.getLoginData,
      flag: true,
    };
  },

  methods: {
    getPosts: async function () {
      return (this.posts = await sendRequest(
        "POST",
        "posts",
        JSON.stringify({ pl_id: this.data.pl_id })
      ).catch((err) => {
        this.flag = false;
        $("#success").toast("show");
        $("#success").toast({ delay: 1000 });
      }));
    },
  },

  created() {
    this.getPosts();
  },
};
</script>
