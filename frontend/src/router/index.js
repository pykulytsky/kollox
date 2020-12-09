import Vue from 'vue'
import VueRouter from 'vue-router'

import TodoList from "@/components/TodoList";
import Login from "@/components/Login";
import Register from "@/components/Register";

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
  },
  {
    path:'/register',
    component: Register,
    name: 'register'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
