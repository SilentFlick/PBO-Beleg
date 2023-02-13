import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import FAQ from "@/views/FAQ.vue";
import Post from "@/views/Post.vue";
import View from "@/views/View.vue";
import Inbox from "@/views/Inbox.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/faq",
    name: "FAQ",
    component: FAQ,
  },
  {
    path: "/post",
    name: "Post",
    component: Post,
  },
  {
    path: "/view/:postID",
    name: "View",
    component: View,
  },
  {
    path: "/inbox",
    name: "Inbox",
    component: Inbox,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
