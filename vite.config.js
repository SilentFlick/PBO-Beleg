import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path";
// https://vitejs.dev/config/
export default defineConfig({
  root: path.resolve(__dirname, "./"),

  server: {
    port: 8080,
    hot: true,
  },
  plugins: [vue()],
});
