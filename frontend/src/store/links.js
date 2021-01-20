export default {
    state: {
        links: [
            {
                url: '/all-todo-lists',
                icon: 'mdi-check-all',
                name: 'All todo lists'
            },
            {
                url: '/projects',
                icon: 'mdi-briefcase-check',
                name: 'Projects'
            },
            {
                url: '/todos',
                icon: 'mdi-check-bold',
                name: 'Todos'
            },
            {
                url: '/important',
                icon: 'mdi-exclamation-thick',
                name: 'Important todos'
            },
            {
                url: '/new-todo',
                icon: 'mdi-comment-check',
                name: 'Add new todo'
            },
            {
                url: '/login',
                icon: 'mdi-account-arrow-left',
                name: 'Login'
            },
            {
                url: '/register',
                icon: 'mdi-shield-account',
                name: 'Register'
            },
            {
                url: '/logout',
                icon: 'mdi-account-arrow-right',
                name: 'Logout'
            },
            {
                url: '/search',
                icon: 'mdi-magnify',
                name: 'Search'
            }

        ],
        linksNotAuthenticated: [
        {
            url: '/login',
            icon: 'mdi-account-arrow-left',
            name: 'Login'
        },
        {
            url: '/register',
            icon: 'mdi-shield-account',
            name: 'Register'
        },


        ],

        linksAuthenticated: [
            {
                url: '/all-todo-lists',
                icon: 'mdi-check-all',
                name: 'All todo lists'
            },
            {
                url: '/projects',
                icon: 'mdi-briefcase-check',
                name: 'Projects'
            },
            {
                url: '/todos',
                icon: 'mdi-check-bold',
                name: 'Todos'
            },
            {
                url: '/important',
                icon: 'mdi-exclamation-thick',
                name: 'Important todos'
            },
            {
                url: '/new-todo',
                icon: 'mdi-comment-check',
                name: 'Add new todo'
            },
            {
                url: '/logout',
                icon: 'mdi-account-arrow-right',
                name: 'Logout'
            },
            {
                url: '/search',
                icon: 'mdi-magnify',
                name: 'Search'
            }

        ]
    },

    getters: {
        links (state) {
            if (state.auth) {
                return state.linksAuthenticated
            }
            else {
                return state.linksNotAuthenticated
            }
        }
    }
}