import Vue from 'vue'
import VueRouter from 'vue-router'

import TodoList from "@/components/TodoList";
import AllTodoLists from "@/components/AllTodoLists";
import Login from "@/components/Login";
import Logout from "@/components/Logout";
import Register from "@/components/Register";
import Profile from "@/components/Profile";

import store from '../store'
import Projects from "@/components/Projects";
import Project from "@/components/Project";
import ImportantTodos from "@/components/ImportantTodos";
import ErrorPage from "@/components/ErrorPage.vue";

import Search from '@/components/Search'
import Calendar from "@/components/Calendar";
import Home from "@/components/Home";

Vue.use(VueRouter)

const routes = [
  {
    path: '/simple-todo-list/:id',
    component: TodoList,
    name: 'simple-todo-list',
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
    path: '/project/:id',
    component: Project,
    name: 'project',
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
    path: '/all-todo-lists/',
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
    path: '/projects/',
    component: Projects,
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
    path: "/profile",
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
  },

  {
    path: '/important',
    component: ImportantTodos,
    beforeEnter(to, from, next) {
      if (JSON.parse(localStorage.getItem('auth'))['token']) {
        store.dispatch('loadUser')
        next()
      } else {
        next('/login')
      }
    }
  },
  {
    path: '/search',
    component: Search,
    name: 'search'
  },

  {
    path: '/calendar',
    component: Calendar,
    name: 'calendar'
  },

  {
    path: '*',
    component: ErrorPage,
    name: '404'
  },


  {
    path: '/home',
    component: Home,
    name: 'home',
    beforeEnter(to, from, next) {
      if (JSON.parse(localStorage.getItem('auth'))['token']) {
        store.dispatch('loadUser')
        next()
      } else {
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
