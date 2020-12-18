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

        async setCover({commit, getters}, payload) {
            if (payload.todoType == 10) {
            await axios.patch('http://localhost:8000/api/todo/project/' + payload.todoListId + '/',
                {
                    cover_pick: payload.coverId
                },
                {
                    headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
                })
                .then(response => {
                    console.log("Success project")
                })
            }
            else if (payload.todoType == 9) {
                await axios.patch('http://localhost:8000/api/todo/simple-todo-list/' + payload.todoListId + '/',
                    {
                        cover_pick: payload.coverId
                    },
                    {
                        headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
                    })
                    .then(response => {
                        console.log("Success todolist")
                    })

            }
            else {
                commit('setError', 'Wrong todo list type')
            }

        },

        async loadProjects({commit, getters}, payload) {
            commit('setLoading', true)

            commit('clearError')

            const config = {
                headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
            };
            const url = 'http://localhost:8000/api/todo/projects/'

            await axios.get(url, config)
                .then(response => {
                    console.log("Success loading todos: ", response.data)
                    commit('setProjects', response.data)
                })
                .catch(error => {
                    commit('setError', error.message)
                })

            commit('setLoading', false)

        },

        async loadProject ({commit, getters}, payload) {
            const url = 'http://localhost:8000/api/todo/project/' + this.$route.params['id'] + '/'
            const config = {
                headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
            };

            await axios.get(url, config)
                .then( response => {
                    getters.todoList.id = response.data.id
                    this.todoList.name = response.data.name
                    this.todoList.owner = response.data.owner
                    this.todoList.favorite = response.data.favorite
                    this.todoList.tasks = response.data.tasks
                    this.todoList.percentageCompleted = response.data.percentage_completed
                    this.todoList.percentageCompleted *= 100
                    console.log("%: ", this.percentageCompleted)
                    console.log("response %: ", response.data.percentage_completed)
                })
                .catch(error => {
                    this.$store.dispatch('setError', error.message)
                })
        },
        async loadAllTodoLists ({commit}) {
            commit('setLoading', true)
            commit('clearError')

            const config = {
                headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
            };
            const url = 'http://localhost:8000/api/todo/all-todo-lists/'

            await axios.get(url, config)
                .then(response => {
                    console.log("Success loading todos: ", response.data)
                    commit('setAllLists', response.data)
                })
                .catch(error => {
                    commit('setError', error.message)
                })

            commit('setLoading', false)
        },

        async completeTask({commit, getters}, payload) {
            const url = 'http://127.0.0.1:8000/api/todo/todo/' + payload.todo_id + '/'
            const config = {
                headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
            };
            const todo = getters.todo.filter(task => {
                return task ? task.id === payload.todo_id: null
            })[0]

            // TODO Fix reloading

            console.log("Complete task: ",todo)
            // TODO Update request, to update not all list, actually specific todo item
            console.log("% before : ", this.todoList.percentageCompleted)
            await axios.patch(url, {
                is_completed: todo.is_completed
            },{
                headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
            })
                .then(response => {
                    this.$store.dispatch('setLoading', true)
                    setTimeout(() => {
                            const url = 'http://localhost:8000/api/todo/project/' + this.$route.params['id'] + '/'
                            const config = {
                                headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
                            };

                            axios.get(url, config)
                                .then( response => {
                                    this.todoList.id = response.data.id
                                    this.todoList.name = response.data.name
                                    this.todoList.owner = response.data.owner
                                    this.todoList.favorite = response.data.favorite
                                    this.todoList.tasks = response.data.tasks
                                    this.todoList.percentageCompleted = response.data.percentage_completed
                                    this.todoList.percentageCompleted *= 100
                                    console.log("% after: ", this.todoList.percentageCompleted)
                                    this.$store.dispatch('setLoading', false)
                                })
                                .catch(error => {
                                    this.$store.dispatch('setError', error.message)
                                    this.$store.dispatch('setLoading', false)
                                })
                        },
                        1000
                    )

                })
        },
    },
    getters: {
        allLists (state) {
            return state.allLists
        },
        projects (state) {
            return state.projects
        }
    }
}