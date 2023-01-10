<template>
  <div>
    <input
      class="form-control"
      type="search"
      placeholder="Search"
      aria-label="Search"
      v-model="query"
      @input="search"
    />
    <div class="dropdown">
      <ul v-if="results.length > 0">
        <li
          v-for="result in results"
          @click="clickHandle"
          :key="result.post_id"
          :value="result.post_id"
        >
          <p>
            <strong>{{ result.title }}</strong> <br />{{
              result.content.slice(0, 100)
            }}
          </p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: "",
      results: [],
      autocompleteData: [],
      loadedPost: [],
    };
  },
  methods: {
    search() {
      const data = JSON.parse(localStorage.getItem("autocompleteData"));
      if (this.query === "") {
        return (this.results = []);
      }
      this.results = data.filter(
        (item) =>
          item.title
            .toLocaleLowerCase()
            .includes(this.query.toLocaleLowerCase()) ||
          item.content
            .toLocaleLowerCase()
            .includes(this.query.toLocaleLowerCase())
      );
    },
    async clickHandle(event) {
      const post_id = event.currentTarget.value;
      console.log(event.target.value);
      this.$router.push({
        path: `/view/${post_id}`,
      });

      this.results = [];
      this.query = "";
    },
  },
  created() {
    const data = JSON.parse(localStorage.getItem("autocompleteData"));
    if (this.query === "") {
      return (this.results = []);
    }
    this.results = data.filter(
      (item) =>
        item.title.includes(this.query) || item.content.includes(this.query)
    );
  },
};
</script>

<style scoped>
.form-control {
  margin: 10px;
  width: 500px;
  height: 50px;
}
.form-control:focus {
  margin: 10px;
  width: 500px;
  height: 50px;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
}

p {
  word-wrap: break-word;
  width: 450px;
}
.dropdown {
  transform: translate(10px, -10px);
  position: absolute;
  background: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 4px;
  overflow: hidden;
  width: 500px;
  z-index: 1;
}

.dropdown ul {
  list-style: none;
  margin: 0;
  padding: 0;
  max-height: 18em;
  overflow-y: scroll;
}

.dropdown li {
  padding: 0.5em 1em;
  display: block;
}

.dropdown li:hover {
  background: #eee;
}
</style>
