// router.js
import { createRouter, createWebHistory } from 'vue-router';
import Build from './views/Build.vue';
import About from './views/About.vue';

const routes = [
  {
    path: '/build',
    name: 'build',
    component: Build
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },

];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
