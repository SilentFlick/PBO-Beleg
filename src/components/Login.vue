<template>
  <div class="login">
    <div
      class="modal modal-centered fade"
      id="login"
      tabindex="-1"
      aria-labelledby="loginLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered modal-sm">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5">Login</h1>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <form>
              <!-- Email input -->
              <div class="form-group mb-3">
                <input
                  id="input-usernamer"
                  class="form-control"
                  placeholder="Bibliotheknummer"
                  v-model="loginValue.username"
                />
              </div>

              <!-- Password input -->
              <div class="form-group mb-3">
                <input
                  type="password"
                  class="form-control"
                  placeholder="Passwort"
                  v-model="loginValue.password"
                />
              </div>
              <p id="error" class="mb-3" style="display: none; color: red">
                Failed to authenticate. <br />Invalid credential
              </p>

              <!-- 2 column grid layout for inline styling -->
              <div class="row mb-3">
                <div class="col d-flex justify-content-begin">
                  <!-- Checkbox -->
                  <div class="form-check">
                    <input class="form-check-input" type="checkbox" />
                    <label class="form-check-label" for="form2Example31">
                      Remember me
                    </label>
                  </div>
                </div>
              </div>

              <!-- Submit button -->
              <div class="modal-footer">
                <button
                  type="button"
                  class="btn btn-secondary"
                  data-bs-dismiss="modal"
                >
                  Close
                </button>
                <button
                  @click="loginHandle"
                  type="button"
                  class="btn btn-primary"
                >
                  Login
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { sendRequest } from "../api/sendRequest";
export default {
  name: "Login",
  emits: ["loginData"],
  props: { msg: String },
  data() {
    return {
      loginValue: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    loginHandle() {
      sendRequest("POST", "login", JSON.stringify(this.loginValue)).then(
        (result) => {
        $("#login").modal("hide");
        let data = {
          isLogin: true,
          username: this.loginValue.username,
          pl_id: result.pl_id,
          hash: result.hash
        };
        this.$emit("loginData", data);

        }
      ).catch(error => {
        document.getElementById("error").style.display = "inline-block";
        this.$emit("loginData", data);
      });
    },
  },
};
</script>
