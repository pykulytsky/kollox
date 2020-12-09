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
        }
    },

    getters: {
        user (state) {
            return state.user
        }
    }
}