import {error} from "vue-resource/src/util";
import axios from 'axios'
import response from "vue-resource/src/http/response";

class Auth {
    constructor(token) {
        this.token = token
    }

}

class User {
    constructor(id, username, email, firstName='', lastName='') {
        this.id
        this.username = username
        this.first_name = firstName
        this.last_name = lastName
    }
}

export default {
    state: {
        auth: null,
        user: null
    },

    mutations: {
        setAuth (state, payload) {
            state.auth = payload
        },
        clearAuth(state) {
            state.auth = null
            localStorage.clear()
        },
        setUser (state, payload) {
            state.auth = payload
        },
        clearUser(state) {
            state.auth = null
            localStorage.clear()
        }
    },

    actions: {
        createAuth({commit}, payload) {
            commit('setAuth', payload)
        },

        logout({commit}, payload) {
            commit('setLoading', true)
            commit('clearError')

            commit('clearAuth')

            commit('setLoading', false)
        },
        clearUser({commit}) {
            commit('clearUser')
        },
        clearAuth({commit}) {
            commit('clearAuth')
        },




        registerUser({commit}, payload) {
            commit('setLoading', true)
            commit('clearError')

            axios.post('http://localhost:8000/api/auth/register/', payload)
                .then(response => {
                    commit('setAuth', new Auth(response.data.token))
                    console.log(response)
                    localStorage.setItem('auth', JSON.stringify(response.data))

                })
                .catch(error => {
                    commit('setError', error.message)
                    throw error
                })

            commit('setLoading', false)
        },

        loginUser({commit}, payload) {
            commit('setLoading', true)
            commit('clearError')

            axios.post('http://localhost:8000/api/auth/login/', payload)
                .then(response => {
                    commit('setAuth', new Auth(response.data.token))
                    console.log(response)
                    localStorage.setItem('auth', JSON.stringify(response.data))

                })
                .catch(error => {
                    commit('setError', error.message)
                    throw error
                })

            commit('setLoading', false)
        },

        autoLogin({commit}) {
            commit('setLoading', true)
            commit('clearError')
            if (JSON.parse(localStorage.getItem('auth'))) {
                const sessionUser = JSON.parse(localStorage.getItem('auth'))
                commit('setAuth', new Auth(sessionUser.token))
            }
            commit('setLoading', false)
        },
    },

    getters: {
        auth (state) {
            return state.auth
        },
        isAuthenticated (state) {
            if (state.auth) {
                return true
            }
            else {
                return false
            }
        }
    }
}