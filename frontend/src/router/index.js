import Vue from 'vue'
import VueRouter from 'vue-router'

import TodoList from "@/components/TodoList";
import AllTodoLists from "@/components/AllTodoLists";
import Login from "@/components/Login";
import Logout from "@/components/Logout";
import Register from "@/components/Register";
import Profile from "@/components/Profile";

import store from '../store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/todo-list/:id',
    component: TodoList,
    name: 'todo-list',
    beforeEnter(to, from, next) {
      if (JSON.parse(localStorage.getItem('auth'))['token']) {
        store.dispatch('loadUser')
        next()
      }
      else {
        next('/login')
      }
    }
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
  },
  {
    path: '/logout',
    component: Logout,
    name: 'logout',
    beforeEnter (to, from, next) {
      store.dispatch('clearUser')
      store.dispatch('clearAuth')
      next('/login')
    }
  },
  {
    path: '/all-todo-lists',
    component: AllTodoLists,
    beforeEnter(to, from, next) {
      if (JSON.parse(localStorage.getItem('auth'))['token']) {
        store.dispatch('loadUser')
        next()
      }
      else {
        next('/login')
      }
    }

  },

  {
    path: "/profile/:id",
    component: Profile,
    beforeEnter(to, from, next) {
      if (JSON.parse(localStorage.getItem('auth'))['token']) {
        store.dispatch('loadUser')
        next()
      }
      else {
        next('/login')
      }
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
