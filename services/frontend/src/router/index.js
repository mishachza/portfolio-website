import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import MiniAppBarbershop from '../views/MiniAppBarbershop.vue';

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
  },
  {
    path: '/examples/mini-app-barbershop',
    name: 'MiniAppBarbershop',
    component: MiniAppBarbershop,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;