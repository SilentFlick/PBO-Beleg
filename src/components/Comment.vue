<template>
  <div class="card border-secondary mx-auto w-100">
    <div class="card-header">
      <div class="card-title">{{ getUsername }} - {{ getTimesAgo }}</div>
    </div>
    <div class="card-body text-secondary h-auto">
      <p class="card-text">
        {{ comment.comment }}
      </p>
    </div>
  </div>
</template>

<script>
import getTimesAgo from "../utils/getTimesAgo.js";
import getRandomName from "../utils/getRandomName.js";

export default {
  name: "Comment",
  props: {
    comment: Object,
  },
  computed: {
    getTimesAgo() {
      return getTimesAgo(this.comment.created_at);
    },
    getUsername() {
      if (this.comment.from_user === null) {
        return getRandomName();
      } else {
        return this.comment.from_user;
      }
    },
  },
};
</script>

<style></style>
