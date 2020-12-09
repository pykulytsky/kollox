import Vue from 'vue'
import VueRouter from 'vue-router'

import TodoList from "@/components/TodoList";
import Login from "@/components/Login";

Vue.use(VueRouter)

const routes = [
  {
    path: '/todo-list/:id',
    component: TodoList,
    name: 'todo-list'
  },
  {
    path: '/login',
    component: Login,
    name: 'login'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
