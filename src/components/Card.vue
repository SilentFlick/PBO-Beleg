<template>
  <div class="card">
    <div class="card-header">
      <div class="row">
        <div
          class="col-9"
          style="padding-right: 20px; border-right: 1px solid #ccc"
        >
          {{ getUsername }}
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
          <span class="underline-text" @click="seeMoreHandle">
            See more</span
          ></span
        >

        <span
          v-if="isExpanded === true"
          class="underline-text"
          @click="seeLessHandle"
        >
          See less</span
        >
      </p>
      <div class="text-end">{{ getTimesAgo }}</div>

      <footer class="card-footer">
        <div
          class="btn-group row w-100 m-auto"
          role="group"
          aria-label="Basic example"
        >
          <button type="button" class="btn btn-outline-secondary col-6">
            Like
          </button>
          <button
            @click="commentToggle"
            type="button"
            class="btn btn-outline-secondary col-6"
            data-bs-toggle="collapse"
            aria-expanded="false"
          >
            Comment
          </button>
          <div v-if="isCommenting">
            <Comment
              v-for="comment in getComments"
              :key="comment.comment_id"
              :comment="comment"
            />
            <input
              type="text"
              class="form-control mt-2"
              placeholder="Write a comment..."
            />
          </div>
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
import Comment from "./Comment.vue";
import getTimesAgo from "../utils/getTimesAgo.js";
import getRandomName from "../utils/getRandomName.js";
export default {
  name: "Card",
  components: { Comment },
  data() {
    return {
      isExpanded: false,
      isCommenting: false,
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
    seeMoreHandle() {
      this.isExpanded = true;
    },
    seeLessHandle() {
      this.isExpanded = false;
    },
    commentToggle() {
      this.isCommenting = !this.isCommenting;
    },
  },

  computed: {
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
    getComments() {
      return this.comments.length > 0
        ? JSON.parse(this.comments[0].comments)
        : [];
    },
  },

  props: {
    postID: Number,
    username: String | null,
    faculty: String,
    title: String,
    content: String,
    created_at: String,
    comments: Array,
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
