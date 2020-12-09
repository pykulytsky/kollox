import Vue from 'vue'
import Vuex from 'vuex'
import links from "@/store/links";
import user from "@/store/user";
import common from "@/store/common";
import todo from '@/store/common'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    links,
    user,
    common,
    todo
  }
})
