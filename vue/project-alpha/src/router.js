// router.js
import { createRouter, createWebHashHistory } from 'vue-router';
import Build from './components/Build.vue';

const routes = [
  {
    path: '/build',
    component: Build
  }
  // Add more routes as needed
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

export default router;
