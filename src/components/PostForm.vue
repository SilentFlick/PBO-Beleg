<template>
  <div class="container mt-2">
    <!--Form to create a new post-->
    <div v-if="data.isLogin" class="form-control post">
      <!--Faculty & Professor input-->
      <div class="d-flex justify-content-between">
        <label class="form-label w-50 me-2"
          >Faculty
          <select @change="onChange($event)" class="form-select" v-model="faculty" required>
            <option
              v-for="option in faculty_options"
              :key="option.id"
              :value="option.faculty"
            >
              {{ option.faculty }}
            </option>
          </select>
        </label>
        <label class="form-label w-50 ms-2"
          >To Professor<select class="form-select" v-model="professor" required>
            <option
              v-for="option in professor_options"
              :key="option.pl_id"
              :value="option.pl_id"
            >
              {{ option.name }}
            </option>
          </select></label
        >
      </div>
      <div>
        <!--Title input-->
        <input
          type="text"
          class="form-control w-100 mt-2 mb-2"
          placeholder="Title"
          v-model="title"
          required
        />
        <!--Content input-->
        <textarea
          class="form-control w-100 mx-auto mt-2 mb-2"
          rows="3"
          placeholder="Write a new Post..."
          v-model="content"
          required
        />
      </div>
      <!--Submit button-->
      <div class="d-flex justify-content-end" @click="postHandle">
        <button class="btn btn-primary w-25 mt-2 mb-2">Submit</button>
      </div>
    </div>
    <div v-else class="d-flex justify-content-center align-items-center mt-3">
      <div>Wanna write a Post?</div>
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
  </div>
  <div class="position-fixed top-0 start-50 translate-middle-x p-3" style="z-index: 11; margin-top: 60px">
    <div
      id="errorToast"
      class="toast hide"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
    >
      <div class="toast-body bg-danger text-white">
        Authetification failed. Please login again! If it is still not working, please contact the admin.
      </div>
    </div>
  </div>
  <div class="position-fixed top-0 start-50 translate-middle-x p-3" style="z-index: 11; margin-top: 60px">
    <div
      id="errorBlank"
      class="toast hide"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
    >
      <div class="toast-body bg-danger text-white">
        Please input every field!
      </div>
    </div>
  </div>
  <div class="position-fixed top-0 start-50 translate-middle-x p-3" style="z-index: 11; margin-top: 60px">
    <div
      id="success"
      class="toast hide"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
    >
      <div class="toast-body bg-success text-white">
        Post successfully!
      </div>
    </div>
  </div>
</template>

<script>
import { sendRequest } from "../api/sendRequest";
export default {
  name: "PostForm",
  inject: ["getLoginData"],
  data() {
    return {
      title: "",
      content: "",
      faculty: null,
      professor: null,
      faculty_options: [
        { id: 1, faculty: "Bauingenieurwesen" },
        { id: 2, faculty: "Design" },
        { id: 3, faculty: "Elektrotechnik" },
        { id: 4, faculty: "Geoinformation" },
        { id: 5, faculty: "Informatik/Mathematik" },
        { id: 6, faculty: "Landbau/Umwelt/Chemie" },
        { id: 7, faculty: "Maschinenbau" },
        { id: 8, faculty: "Wirtschaftsingenieurwesen" },
      ],
      professor_options: [],
      data: this.getLoginData,
    };
  },
  methods: {
    onChange: async function (event) {
      return (this.professor_options = await sendRequest(
        "POST",
        "profs",
        JSON.stringify({faculty: event.target.value})
      ).then((res) => {
        console.log(res);
        return res;
      }));
    },
    postHandle: function () {
      const data = {
        title: this.title,
        content: this.content,
        faculty: this.faculty,
        to_user: this.professor,
        from_user: this.data.pl_id || null,
        hash: this.data.hash,
      };
      if (
        this.title === "" ||
        this.content === "" ||
        this.faculty === "" ||
        this.to_user === ""
      ) {
        $("#errorBlank").toast("show");
        $("#errorBlank").toast({ delay: 1000 });
        return;
      }
      sendRequest("POST", "post", JSON.stringify(data)
      ).then(res => {
        $("#success").toast("show");
        $("#success").toast({ delay: 10000 });
      }
      ).catch(error => {
        $("#errorToast").toast("show");
        $("#errorToast").toast({ delay: 10000 });
      });
      this.title = "";
      this.content = "";
      this.faculty = "";
      this.to_user = "";
      // this.$router.push({
      //   path: `/`,
      // });
    },
  },

   // created() {
   //   this.getProfessors();
   // },
};
</script>

<style>
.container {
  width: 75%;
}

.post {
  width: 50% !important;
  margin: auto;
}
@media screen and (max-width: 900px) {
  .container {
    width: 100%;
  }
  .post {
    width: 100% !important;
  }
}
</style>
