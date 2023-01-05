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
        </div>
        <div v-if="isCommenting">
          <div v-if="isLogin" class="input-group mt-3">
            <textarea
              id="comment"
              type="text"
              class="form-control"
              placeholder="Write a comment..."
              aria-label="Write a comment..."
              aria-describedby="button-addon2"
              @keyup.enter="commentHandle()"
            ></textarea>
            <button
              class="btn btn-outline-secondary"
              type="button"
              id="button-addon2"
              @click="commentHandle()"
            >
              <i class="bi bi-send"></i>
            </button>
          </div>

          <div
            v-else
            class="d-flex justify-content-center align-items-center mt-3"
          >
            <div>Wanna write a comment?</div>
            <div>
              <a
                class="text-decoration-none"
                href="#login"
                data-bs-toggle="modal"
                data-bs-target="#login"
              >
                &nbsp; Login here!
              </a>
            </div>
          </div>
          <Comment
            v-for="comment in getComments.sort(
              (a, b) =>
                new Date(b.created_at).getTime() -
                new Date(a.created_at).getTime()
            )"
            :key="comment.comment_id"
            :comment="comment"
          />
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
import Comment from "./Comment.vue";
import { sendRequest } from "../api/sendRequest.js";
import getTimesAgo from "../utils/getTimesAgo.js";
import getRandomName from "../utils/getRandomName.js";
export default {
  name: "Card",
  components: { Comment },
  inject: ["loginStatus"],
  data() {
    return {
      comment: "",
      isExpanded: false,
      isCommenting: false,
      isLogin: this.loginStatus,
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
    commentHandle() {
      if ($("#comment").val() === "") {
        console.log("Comment is empty");
        return;
      }
      //get comment from input
      this.comment = $("#comment").val();

      //add comment string to comments array for rendering comment without refreshing page
      this.comments[0].comments = JSON.stringify([
        ...this.getComments,
        {
          comment: this.comment,
          from_user: null,
          created_at: new Date().toISOString().slice(0, 19).replace("T", " "),
        },
      ]);
      const comment = {
        post_id: this.postID,
        comment: this.comment,
      };
      sendRequest(
        "POST",
        "comments",
        JSON.stringify(comment),

        (res) => {
          console.log(res);
        }
      );
      $("#comment").val("");
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
