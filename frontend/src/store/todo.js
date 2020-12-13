import axios from 'axios'
import response from "vue-resource/src/http/response";

export default {
    state: {
        todos: [],
        allLists: [],
        projects: [],
        simpleToDoLists: []
    },
    mutations: {
        setTodos (state, payload) {
            state.todos = payload
        },
        addTodo (state, payload) {
            state.todos.push(payload)
        },
        setAllLists (state, payload) {
            state.allLists = payload
        },
        setProjects (state, payload) {
            state.projects = payload
        },
        setSimpleToDoLists (state, payload) {
            state.simpleToDoLists = payload
        },

        addProject (state, payload) {
            state.projects.push(payload)
        },
        addSimpleToDoLists (state, payload) {
            state.simpleToDoLists.push(payload)
        },

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
        loadAllTodoLists ({commit}) {
            commit('setLoading', true)
            commit('clearError')

            const config = {
                headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
            };
            const url = 'http://localhost:8000/api/todo/all-todo-lists/'

            axios.get(url, config)
                .then(response => {
                    console.log("Success loading todos: ", response.data)
                    commit('setAllLists', response.data)
                })
                .catch(error => {
                    commit('setError', error.message)
                })

            commit('setLoading', false)
        }
    },
    getters: {
        allLists (state) {
            return state.allLists
        }
    }
}