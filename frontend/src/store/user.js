import response from "vue-resource/src/http/response";

class User {
    constructor(id, token) {
        this.id = id
        this.token = token
    }

}

export default {
    state: {
        user: null
    },

    mutations: {
        setUser (state, payload) {
            state.user = new User(payload.id, payload.token)
        }
    },

    actions: {
        createUser({commit}, payload) {
            commit('setUser', payload)
        },

        registerUser({commit}, payload) {
            commit('setLoading', true)
            this.$http.post('http://localhost:8000/api/auth/register',
                {username: payload.username,
                    email: payload.email,
                    password: payload.password
            })
                .then(response => {
                    return response.json()
                })
                .then(token => {
                    commit('setUser', {id: 1, token: token})
                    console.log(token)
                })
                .catch(error => {
                    commit('setError', error.message)
                    throw error
            })
        }
    },

    getters: {
        user (state) {
            return state.user
        }
    }
}