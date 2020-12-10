import {error} from "vue-resource/src/util";


class User {
    constructor(token) {
        this.token = token
    }

}

export default {
    state: {
        user: null
    },

    mutations: {
        setUser (state, payload) {
            state.user = new User(payload.token)
        },
        clearUser(state) {
            state.user = null
        }
    },

    actions: {
        createUser({commit}, payload) {
            commit('setUser', payload)
        },

        logout({commit}, payload) {
            commit('setLoading', true)
            commit('clearError')

            commit('clearUser')

            commit('setLoading', false)
        },

        registerUser({commit}, payload) {

            commit('setUser', {token: payload.token})


        },
        loginUser({commit}, payload) {
            commit('setLoading', true)
            this.$http.post('http://localhost:8000/api/auth/login/',
                {username: payload.username,
                    email: payload.email,
                    password: payload.password
                })
                .then(response => {
                    return response.json()
                })
                .then(token => {
                    commit('setUser', {id: 1, token: token})
                    commit('setLoading', false)
                    console.log(token)
                })
                .catch(error => {
                    commit('setError', error.message)
                    commit('setLoading', false)
                    throw error
                })
        },

    },

    getters: {
        user (state) {
            return state.user
        },
        isAuthenticated (state) {
            if (state.user) {
                return  true
            }
            else {
                return  false
            }
        }
    }
}