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
              <div class="form-outline mb-3">
                <input
                  type="email"
                  class="form-control"
                  placeholder="Bibliotheknummer"
                />
              </div>

              <!-- Password input -->
              <div class="form-outline mb-3">
                <input
                  type="password"
                  class="form-control"
                  placeholder="Passwort"
                />
              </div>

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
                <button type="button" class="btn btn-primary">Login</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  props: { msg: String },
};
</script>
