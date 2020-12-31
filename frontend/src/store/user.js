import {error} from "vue-resource/src/util";
import axios from 'axios'
import response from "vue-resource/src/http/response";

class Auth {
    constructor(token) {
        this.token = token
    }

}

class User {
    constructor(id, username, email, firstName, lastName, emailVerified ,avatar ) {
        this.id = id
        this.username = username
        this.email = email
        this.firstName = firstName
        this.lastName = lastName
        this.emailVerified = emailVerified
        this.avatar = avatar
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
        async clearAuth(state) {
            state.auth = null
            await localStorage.clear()
        },
        setUser (state, payload) {
            state.user = payload
        },
        async clearUser(state) {
            state.user = null
            await localStorage.clear()
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

        async logInViaGoogle({commit, getters}, payload) {
            // TODO DONT WORKK FUCKING PYTHUHON
            await axios.post('http://localhost:8000/api/auth/google/',
                {
                    access_token: payload
                })
                .then(response => {

                })
                .catch(error => {

                })
        },

        async loadUser({commit}) {
            commit('setLoading', true)
            commit('clearError')

            if (JSON.parse(localStorage.getItem('auth'))) {
                await axios.get(`http://localhost:8000/api/auth/user/${JSON.parse(localStorage.getItem('auth'))['pk']}`, {
                    headers: {Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}`}
                })
                    .then(response => {
                        commit('setUser', new User(
                            response.data['id'],
                            response.data['username'],
                            response.data['email'],
                            response.data['first_name'],
                            response.data['last_name'],
                            response.data['email_verified'],
                            response.data['avatar'],
                        ))
                    })
                    .catch(error => {
                        console.log(error)
                        commit('setError', error.message)
                        throw error
                    })
            }
            else {
                commit('setUser', null)
            }
            commit('setLoading', false)
        },


        async registerUser({commit}, payload) {
            commit('setLoading', true)
            commit('clearError')

            await axios.post('http://localhost:8000/api/auth/register/', payload)
                .then(response => {
                    console.log(response.status)
                    if (response.status == 201) {
                        commit('setAuth', new Auth(response.data.token))
                        console.log("Response: ",response)
                        console.log("success")
                        localStorage.setItem('auth', JSON.stringify(response.data))
                        commit('setLoading', false)
                    }
                    else {
                        console.log("Error Response: ",response)
                        commit('setError', "Wrong register credentials")
                        commit('setLoading', false)
                        throw error("Wrong REGISTRATION credentials")
                    }
                })
                .catch(error => {
                    commit('setError', error.message)
                    commit('setLoading', false)
                    throw error
                })

            commit('setLoading', false)
        },

        async loginUser({commit}, payload) {
            commit('setLoading', true)
            commit('clearError')

            await axios.post('http://localhost:8000/api/auth/login/', payload)
                .then(response => {
                    if (response.status == 200) {
                        commit('setAuth', new Auth(response.data.token))
                        console.log("Response: ",response)
                        console.log("success")
                        localStorage.setItem('auth', JSON.stringify(response.data))
                        commit('setLoading', false)
                    }
                    else {
                        console.log("Error Response: ",response)
                        commit('setError', "Wrong login credentials")
                        commit('setLoading', false)
                        throw error("Wrong login credentials")
                    }

                })
                .catch(error => {
                    console.log("Error: ", error)
                    commit('setError', error.message)
                    commit('setLoading', false)
                    throw error
                })

            commit('setLoading', false)
        },

        async autoLogin({commit}) {
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
        user (state) {
          return state.user
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