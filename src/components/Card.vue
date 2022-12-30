<template>
  <div class="card">
    <div class="card-header">
      <div class="row">
        <div
          class="col-9"
          style="padding-right: 20px; border-right: 1px solid #ccc"
        >
          {{ getUsername() }}
        </div>
        <div class="col-3">{{ faculty }}</div>
      </div>
    </div>
    <div class="card-body">
      <h5 class="card-title fw-bolder">{{ title }}</h5>
      <p class="card-content">
        {{ fullContent() }}
        <span v-if="isExpanded === false && content.length > 100">
          ...
          <span class="underline-text" @click="expandHandle">
            See more</span
          ></span
        >

        <span
          v-if="isExpanded === true"
          class="underline-text"
          @click="collapseHandle"
        >
          See less</span
        >
      </p>
      <div class="text-end">{{ getTimesAgo() }}</div>

      <hr />
      <footer class=""></footer>
    </div>
  </div>
</template>

<script>
import getTimesAgo from "../utils/getTimesAgo.js";
import getRandomName from "../utils/getRandomName.js";
export default {
  name: "Card",
  data() {
    return {
      isExpanded: false,
    };
  },
  methods: {
    fullContent() {
      if (
        (this.content && this.content.length < 100) ||
        this.isExpanded === true
      ) {
        return this.content;
      } else {
        return this.content.slice(0, 100);
      }
    },
    expandHandle() {
      this.isExpanded = true;
    },
    collapseHandle() {
      this.isExpanded = false;
    },
    getTimesAgo() {
      return getTimesAgo(this.created_at);
    },
    getUsername() {
      if (this.username === null) {
        return getRandomName();
      } else {
        return this.username;
      }
    },
  },
  props: {
    postID: Number,
    username: String | null,
    faculty: String,
    title: String,
    content: String,
    created_at: String,
  },
};
</script>

<style scoped>
.card {
  width: 50%;
  margin: 10px auto;
  min-height: 150px;
}

.underline-text:hover {
  text-decoration: underline;
  font-weight: bold;
}
</style>
