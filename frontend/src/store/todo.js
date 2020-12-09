

export default {
    state: {
        todos: []
    },
    mutations: {
        setTodos (state, payload) {
            state.todos = payload
        },
        addTodo (state, payload) {
            state.todos.push(payload)
        }
    },

    actions: {
        setTodo ({commit}, payload) {
            commit('setLoading', true)
            commit('clearError')
            commit('setTodo', payload)
            commit('setLoading', false)

        },
        addTodo ({commit}, payload) {
            commit('setLoading', true)
            commit('clearError')
            commit('addTodo', payload)
            commit('setLoading', true)
        },
        loadTodos ({commit}, payload) {
            commit('setLoading', true)
            commit('clearError')


            commit('setLoading', false)
        }
    }
}