<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex
          xs12 sm8 md8>
        <v-card
            elevation="16"
            :loading="loading"
            class="d-flex flex-column main-card justify-space-around"

        >
          <v-img
              class="header__image"
              :src="todoList.cover"
              height="200px"
          ></v-img>


          <div class="card__header1">
            <h2 class="card__header__text">{{ todoList.name }}</h2>


            <v-menu
                left
                bottom
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                    icon
                    v-bind="attrs"
                    v-on="on"
                >
                  <v-icon>mdi-dots-vertical</v-icon>
                </v-btn>
              </template>

              <v-list>
                <v-list-item
                    @click="coverPicker = true"
                >
                  <v-list-item-title>
                    Add cover</v-list-item-title>
                </v-list-item>

                <v-list-item
                    @click="deleteDialog = true"
                >
                  <v-list-item-title>
                    Delete</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>

          </div>


          <!-- NEW TODO-->
          <div class="new__todo">
            <v-text-field
                v-model="newTodo"
                class="add__todo"
                label="Add new todo"
            >
            </v-text-field>
            <!--            <v-btn-->
            <!--                v-if="!datePicker"-->
            <!--              icon-->
            <!--              >-->
            <!--              <v-icon>-->
            <!--                mdi-calendar-->
            <!--              </v-icon>-->
            <!--            </v-btn>-->

            <v-menu
                ref="menu"
                v-model="menu"
                :close-on-content-click="false"
                :return-value.sync="date"
                transition="scale-transition"
                offset-y
                min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                    v-bind="attrs"
                    v-on="on"
                    v-if="!datePicker"
                    icon
                >
                  <v-icon
                  >
                    mdi-calendar
                  </v-icon>
                </v-btn>
              </template>
              <v-date-picker
                  v-model="date"
                  no-title
                  color="deep-purple"
                  scrollable
                  :min="todayDate"
              >
                <v-spacer></v-spacer>
                <v-btn
                    text
                    color="primary"
                    @click="menu = false"
                >
                  Cancel
                </v-btn>
                <v-btn
                    text
                    color="primary"
                    @click="saveDate(date)"
                >
                  OK
                </v-btn>
              </v-date-picker>
            </v-menu>

            <!--
            -->

            <v-btn
                icon
                @click="addTodo"
                @keyup.enter="addTodo"
            >
              <v-icon>
                mdi-plus
              </v-icon>
            </v-btn>
          </div>

          <div
              class="todo__item"
              v-if="todoList.tasks"
              v-for="todo in todoList.tasks"
          >
            <v-checkbox
                color="indigo"
                class="item__checkbox"
                hide-details
            ></v-checkbox>
            {{ todo.title }}
            <v-spacer></v-spacer>
            <v-btn
                icon

                @click="openDialog"
            >
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
            <v-btn
                @click="addToFavorite"
                icon
                color="indigo"

            >
              <v-icon>{{ star }}</v-icon>
            </v-btn>
          </div>
<!--          <div class="todo__item">-->
<!--            <v-checkbox-->
<!--                color="indigo"-->

<!--                hide-details-->
<!--            ></v-checkbox>-->
<!--            Lorem ipsum dolor sit.-->
<!--            <v-spacer></v-spacer>-->
<!--            <v-btn-->
<!--                @click="addToFavorite"-->
<!--                icon-->
<!--                color="indigo"-->

<!--            >-->
<!--              <v-icon>{{ star }}</v-icon>-->
<!--            </v-btn>-->
<!--          </div>-->
<!--          <div class="todo__item">-->
<!--            <v-checkbox-->
<!--                color="indigo"-->

<!--                hide-details-->
<!--            ></v-checkbox>-->
<!--            Lorem ipsum dolor sit amet.-->
<!--            <v-spacer></v-spacer>-->
<!--            <v-btn-->
<!--                @click="addToFavorite"-->
<!--                icon-->
<!--                color="indigo"-->

<!--            >-->
<!--              <v-icon>{{ star }}</v-icon>-->
<!--            </v-btn>-->
<!--          </div>-->
<!--          <div class="todo__item">-->
<!--            <v-checkbox-->
<!--                color="indigo"-->

<!--                hide-details-->
<!--            ></v-checkbox>-->
<!--            Lorem ipsum dolor sit amet, consectetur.-->
<!--            <v-spacer></v-spacer>-->
<!--            <v-btn-->
<!--                @click="addToFavorite"-->
<!--                icon-->
<!--                color="indigo"-->

<!--            >-->
<!--              <v-icon>{{ star }}</v-icon>-->
<!--            </v-btn>-->
<!--          </div>-->
<!--          <div class="todo__item">-->
<!--            <v-checkbox-->
<!--                color="indigo"-->

<!--                hide-details-->
<!--            ></v-checkbox>-->
<!--            Lorem ipsum dolor sit.-->
<!--            <v-spacer></v-spacer>-->
<!--            <v-btn-->
<!--                @click="addToFavorite"-->
<!--                icon-->
<!--                color="indigo"-->

<!--            >-->
<!--              <v-icon>{{ star }}</v-icon>-->
<!--            </v-btn>-->
<!--          </div>-->
<!--          <div class="todo__item">-->
<!--            <v-checkbox-->
<!--                color="indigo"-->

<!--                hide-details-->
<!--            ></v-checkbox>-->
<!--            1234-->
<!--            <v-spacer></v-spacer>-->
<!--            <v-btn-->
<!--                @click="addToFavorite"-->
<!--                icon-->
<!--                color="indigo"-->

<!--            >-->
<!--              <v-icon>{{ star }}</v-icon>-->
<!--            </v-btn>-->
<!--          </div>-->
<!--          <div class="todo__item">-->
<!--            <v-checkbox-->
<!--                color="indigo"-->

<!--                hide-details-->
<!--            ></v-checkbox>-->
<!--            Lorem ipsum dolor sit.-->
<!--            <v-spacer></v-spacer>-->
<!--            <v-btn-->
<!--                @click="addToFavorite"-->
<!--                icon-->
<!--                color="indigo"-->

<!--            >-->
<!--              <v-icon>{{ star }}</v-icon>-->
<!--            </v-btn>-->
<!--          </div>-->
<!--          <div class="todo__item">-->
<!--            <v-checkbox-->
<!--                color="indigo"-->

<!--                hide-details-->
<!--            ></v-checkbox>-->
<!--            Lorem ipsum dolor sit amet.-->
<!--            <v-spacer></v-spacer>-->
<!--            <v-btn-->
<!--                @click="addToFavorite"-->
<!--                icon-->
<!--                color="indigo"-->

<!--            >-->
<!--              <v-icon>{{ star }}</v-icon>-->
<!--            </v-btn>-->
<!--          </div>-->
<!--          <div class="todo__item">-->
<!--            <v-checkbox-->
<!--                color="indigo"-->

<!--                hide-details-->
<!--            ></v-checkbox>-->
<!--            Lorem ipsum dolor sit amet, consectetur.-->
<!--            <v-spacer></v-spacer>-->
<!--            <v-btn-->
<!--                @click="addToFavorite"-->
<!--                icon-->
<!--                color="indigo"-->

<!--            >-->
<!--              <v-icon>{{ star }}</v-icon>-->
<!--            </v-btn>-->
<!--          </div>-->
<!--          <div class="todo__item">-->
<!--            <v-checkbox-->
<!--                color="indigo"-->

<!--                hide-details-->
<!--            ></v-checkbox>-->
<!--            Lorem ipsum dolor sit.-->
<!--            <v-spacer></v-spacer>-->
<!--            <v-btn-->
<!--                @click="addToFavorite"-->
<!--                icon-->
<!--                color="indigo"-->

<!--            >-->
<!--              <v-icon>{{ star }}</v-icon>-->
<!--            </v-btn>-->
<!--          </div>-->
<!--          <div class="todo__item">-->
<!--            <v-checkbox-->
<!--                color="indigo"-->

<!--                hide-details-->
<!--            ></v-checkbox>-->
<!--            1234-->
<!--          </div>-->
<!--          <div class="todo__item">-->
<!--            <v-checkbox-->
<!--                color="indigo"-->

<!--                hide-details-->
<!--            ></v-checkbox>-->
<!--            Lorem ipsum dolor sit.-->
<!--            <v-spacer></v-spacer>-->
<!--            <v-btn-->
<!--                @click="addToFavorite"-->
<!--                icon-->
<!--                color="indigo"-->

<!--            >-->
<!--              <v-icon>{{ star }}</v-icon>-->
<!--            </v-btn>-->
<!--          </div>-->
<!--          <div class="todo__item">-->
<!--            <v-checkbox-->
<!--                color="indigo"-->

<!--                hide-details-->
<!--            ></v-checkbox>-->
<!--            Lorem ipsum dolor sit amet.-->
<!--          </div>-->
<!--          <div class="todo__item">-->
<!--            <v-checkbox-->
<!--                color="indigo"-->

<!--                hide-details-->
<!--            ></v-checkbox>-->
<!--            Lorem ipsum dolor sit amet, consectetur.-->
<!--          </div>-->
<!--          <div class="todo__item">-->
<!--            <v-checkbox-->
<!--                color="indigo"-->

<!--                hide-details-->
<!--            ></v-checkbox>-->
<!--            Lorem ipsum dolor sit.-->
<!--          </div>-->
        </v-card>
      </v-flex>
    </v-layout>
    <v-dialog
        v-model="dialog"
        persistent
        max-width="600px"
    >

      <v-card>
        <v-card-title>
          <span class="headline">User Profile</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col
                  cols="12"
                  sm="6"
                  md="4"
              >
                <v-text-field
                    label="Legal first name*"
                    required
                ></v-text-field>
              </v-col>
              <v-col
                  cols="12"
                  sm="6"
                  md="4"
              >
                <v-text-field
                    label="Legal middle name"
                    hint="example of helper text only on focus"
                ></v-text-field>
              </v-col>
              <v-col
                  cols="12"
                  sm="6"
                  md="4"
              >
                <v-text-field
                    label="Legal last name*"
                    hint="example of persistent helper text"
                    persistent-hint
                    required
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                    label="Email*"
                    required
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                    label="Password*"
                    type="password"
                    required
                ></v-text-field>
              </v-col>
              <v-col
                  cols="12"
                  sm="6"
              >
                <v-select
                    :items="['0-17', '18-29', '30-54', '54+']"
                    label="Age*"
                    required
                ></v-select>
              </v-col>
              <v-col
                  cols="12"
                  sm="6"
              >
                <v-autocomplete
                    :items="['Skiing', 'Ice hockey', 'Soccer', 'Basketball', 'Hockey', 'Reading', 'Writing', 'Coding', 'Basejump']"
                    label="Interests"
                    multiple
                ></v-autocomplete>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="blue darken-1"
              text
              @click="dialog = false"
          >
            Close
          </v-btn>
          <v-btn
              color="blue darken-1"
              text
              @click="dialog = false"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>


    <v-dialog
        v-model="coverPicker"
        persistent
        max-width="900px"
    >

      <v-card>
        <v-card-title>
          <span class="headline">Choose cover of todo list</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <vue-select-image
                :dataImages="covers"
                :is-multiple="false"
                @onselectimage="onSelectCover"
                :h="'250px'"
                :w="'300px'"
            >

            </vue-select-image>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="blue darken-1"
              text
              @click="coverPicker = false"
          >
            Close
          </v-btn>
          <v-btn
              color="blue darken-1"
              text
              @click="chooseCover"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>


    <v-dialog
        v-model="deleteDialog"
        persistent
        max-width="320px"
    >
      <v-card>
        <v-card-title class="headline">
          Delete this todo list?
        </v-card-title>
        <v-card-text>Are you sure you want to delete this list?</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="green darken-1"
              text
              @click="deleteDialog = false"
          >
            Go back
          </v-btn>
          <v-btn
              color="red"
              text
              @click="deleteToDo"
          >
            Delete
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </v-container>

</template>

<script>
import axios from 'axios'

export default {
  data: () => {
    return {
      drawer: false,
      favorite: false,
      starIcon: 'mdi-star',
      outlineStarIcon: 'mdi-star-outline',
      dialog: false,
      isListFavorite: false,
      heartIcon: 'mdi-heart',
      heartOutlinedIcon: 'mdi-heart-outline',

      datePicker: false,
      isDateUsing: false,
      date: new Date().toISOString().substr(0, 10),
      menu: false,
      todayDate: new Date().toISOString().substr(0, 10),
      dateRequired: false,

      newTodo: '',
      todoType: 9,

      deleteDialog: false,

      todoList: {
        id: 0,
        tasks: [],
        name: '',
        favorite: false,
        owner: null,
        cover: '',
      },

      initialSelected: [],
      coverPicker: false,
      selectedCover: null,

      covers: [
        {
          id: 1,
          src: require('@/assets/cover1.jpg'),
        },
        {
          id: 2,
          src: require('@/assets/cover2.jpg'),
        },
        {
          id: 3,
          src: require('@/assets/cover3.jpg'),
        },
        {
          id: 4,
          src: require('@/assets/cover4.jpg'),
        },
        {
          id: 5,
          src: require('@/assets/cover5.jpg'),
        },
        {
          id: 6,
          src: require('@/assets/cover6.jpg'),
        },
        {
          id: 7,
          src: require('@/assets/cover7.jpg'),
        },
        {
          id: 8,
          src: require('@/assets/cover8.jpg'),
        },
        {
          id: 9,
          src: require('@/assets/cover9.jpg'),
        },
        {
          id: 10,
          src: require('@/assets/cover10.jpg'),
        },
        {
          id: 11,
          src: require('@/assets/cover11.jpg'),
        },
        {
          id: 12,
          src: require('@/assets/cover12.jpg'),
        },

      ],

    }
  },
  computed: {
    star () {
      if (this.todoList.favorite) {
        return  this.starIcon
      }
      else {
        return this.outlineStarIcon
      }
    },

    heart () {
      if (this.isListFavorite) {
        return  this.heartIcon
      }
      else {
        return this.heartOutlinedIcon
      }
    },

    loading () {
      return this.$store.getters.loading
    }

  },
  methods: {
    deleteToDo () {
      this.$store.dispatch('setLoading', true)

      const config = {
        headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
      };

      axios.delete('http://localhost:8000/api/todo/simple-todo-list/' + this.$route.params['id'] +
          '/',
          config
      )
          .then(response => {
            this.todoList = null
            this.$router.push('/all-todo-lists')
          })

      this.$store.dispatch('setLoading', false)
    },

    chooseCover () {
      // TODO Add cover picker
      this.$store.dispatch('setLoading', true)
      this.coverPicker = false
      console.log(this.selectedCover.src)

      let coverSrc = this.selectedCover.src.replace('/img/', '').split('.')
      coverSrc = coverSrc[0] + "." + coverSrc[2]
      console.log(coverSrc)

      // const coverResult = this.covers.filter(cover => {
      //   if ()
      // })


      this.$store.dispatch('setCover', {
        cover: coverSrc,
        todoListId: this.todoList.id,
        coverId: this.selectedCover.id,
        todoType: this.todoType
      })
          .then(() => {
            const url = 'http://localhost:8000/api/todo/simple-todo-list/' +
                this.$route.params['id'] + '/'
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
                  this.todoList.cover = response.data.cover
                })
                .catch(error => {
                  this.$store.dispatch('setError', error.message)
                })
          })

      this.$store.dispatch('setLoading', false)
    },

    saveDate (date) {
      this.isDateUsing = true
      this.$refs.menu.save(date)
    },

    addTodo () {
      const url = 'http://127.0.0.1:8000/api/todo/todos/'
      const config = {
        headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
      };
      if (this.isDateUsing) {
        const date = this.date.toString() + "T00:00"

        axios.post(url, {
          title: this.newTodo,
          todo_list_id: this.$route.params['id'],
          todo_list_type: this.todoType,
          expired_time: date
        }, {
          headers: {Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}`}
        })
            .then(response => {
              this.date = new Date().toISOString().substr(0, 10),
                  this.newTodo = ''
              console.log(response.data)
              const url = 'http://localhost:8000/api/todo/simple-todo-list/' +
                  this.$route.params['id'] + '/'
              const config = {
                headers: {Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}`}
              };

              axios.get(url, config)
                  .then(response => {
                    this.todoList.id = response.data.id
                    this.todoList.name = response.data.name
                    this.todoList.owner = response.data.owner
                    this.todoList.favorite = response.data.favorite
                    this.todoList.tasks = response.data.tasks
                    this.todoList.cover = response.data.cover

                  })
                  .catch(error => {
                    this.$store.dispatch('setError', error.message)
                  })

            })
            .catch(error => {
              console.log(error)

            })

        const reloadUrl = 'http://localhost:8000/api/todo/simple-todo-list/' +
            this.$route.params['id'] + '/'
        const reloadConfig = {
          headers: {Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}`}
        };

        axios.get(reloadUrl, reloadConfig)
            .then(response => {
              this.todoList.id = response.data.id
              this.todoList.name = response.data.name
              this.todoList.owner = response.data.owner
              this.todoList.favorite = response.data.favorite
              this.todoList.tasks = response.data.tasks
              this.todoList.cover = response.data.cover


            })
            .catch(error => {
              this.$store.dispatch('setError', error.message)
            })
      }
      else {

        axios.post(url, {
          title: this.newTodo,
          todo_list_id: this.$route.params['id'],
          todo_list_type: this.todoType,
        }, {
          headers: {Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}`}
        })
            .then(response => {
              this.date = new Date().toISOString().substr(0, 10),
                  this.newTodo = ''
              console.log(response.data)
              const url = 'http://localhost:8000/api/todo/simple-todo-list/' +
                  this.$route.params['id'] + '/'
              const config = {
                headers: {Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}`}
              };

              axios.get(url, config)
                  .then(response => {
                    this.todoList.id = response.data.id
                    this.todoList.name = response.data.name
                    this.todoList.owner = response.data.owner
                    this.todoList.favorite = response.data.favorite
                    this.todoList.tasks = response.data.tasks
                    this.todoList.cover = response.data.cover

                  })
                  .catch(error => {
                    this.$store.dispatch('setError', error.message)
                  })

            })
            .catch(error => {
              console.log(error)

            })

        const reloadUrl = 'http://localhost:8000/api/todo/simple-todo-list/' +
            this.$route.params['id'] + '/'
        const reloadConfig = {
          headers: {Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}`}
        };

        axios.get(reloadUrl, reloadConfig)
            .then(response => {
              this.todoList.id = response.data.id
              this.todoList.name = response.data.name
              this.todoList.owner = response.data.owner
              this.todoList.favorite = response.data.favorite
              this.todoList.tasks = response.data.tasks
              this.todoList.cover = response.data.cover

            })
            .catch(error => {
              this.$store.dispatch('setError', error.message)
            })

      }

      this.isDateUsing = false

    },

    onSelectCover (data) {
      console.log(data.id)
      this.selectedCover = data
    },

    addToFavorite () {
      this.favorite = !this.favorite
    },
    openDialog() {
      this.dialog = true
    }
  },
  mounted() {
    console.log(this.$route.params)
    const url = 'http://localhost:8000/api/todo/simple-todo-list/' + this.$route.params['id'] + '/'
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
      this.todoList.cover = response.data.cover
    })
    .catch(error => {
      this.$store.dispatch('setError', error.message)
    })


    console.log("Tasks: " ,this.todoList.tasks)
  }

}
</script>

<style>
* {
  font-family: 'Open Sans', sans-serif;
}

.card__header__text {
  font-family: 'Andika New Basic', sans-serif;
}

.main-card {
  overflow: hidden;
  height: 100%;
  min-height: 100%;
  justify-content: space-between;
  padding-top: 5px;

}



.todo__item {
  border-radius: 5px;
  margin: 5px 10px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  padding: 3px 10px 10px 10px;
  background-color: #121212;

}
.todo__item:last-child {
  margin-bottom: 25px;
}

.item__checkbox {
  margin: 0;
  padding: 0;
}
p {
  margin: 0;
  padding: 0;
}

.card__header1 {
  margin: 25px 15px;
  display: flex;
  justify-content: space-between;
}

.header__image {
  margin: 0;
}

</style>