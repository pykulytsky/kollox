<template>
  <div class="project">
  <v-container fluid fill-height>
    <v-progress-circular
        :rotate="360"
        :size="70"
        :width="10"
        :value="percent"
        class="progress"
        color="accent-4"
    >
      {{ percent }}%
    </v-progress-circular>

    <v-layout align-center justify-center>
      <v-flex
          xs12 sm8 md8>
<!--        <v-card-->
<!--            elevation="16"-->
<!--            :loading="loading"-->
<!--            class="d-flex flex-column main-card justify-space-between"-->

<!--        >-->
        <v-card
            elevation="16"
            :loading="loading"
            class="d-flex flex-column main-card justify-space-around"

        >
          <transition name="fade">
          <v-img
              class="header__image"
              :src="todoList.cover"
              height="200px"

          >

          </v-img>
          </transition>
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
                  <v-list-item-icon>
                    <v-icon>
                      mdi-plus-box-multiple
                    </v-icon>
                  </v-list-item-icon>
                  <v-list-item-title>
                    Add cover</v-list-item-title>

                </v-list-item>


                <v-list-item
                    @click="loadUsersForShare"
                >
                  <v-list-item-icon>
                    <v-icon>

                      mdi-export-variant
                    </v-icon>
                  </v-list-item-icon>

                  <v-list-item-title>
                    Share list</v-list-item-title>

                </v-list-item>

                <v-list-item
                    @click="deleteDialog = true"
                >
                  <v-list-item-icon>
                    <v-icon>
                      mdi-delete-forever
                    </v-icon>
                  </v-list-item-icon>
                  <v-list-item-title>
                    Delete</v-list-item-title>
                </v-list-item>

              </v-list>
            </v-menu>
          </div>

          <v-btn
              icon
              v-if="addNewTodo == false"
              @click="addNewTodo = true"
          >
          <v-icon
            small
          >
            mdi-plus
          </v-icon>
          </v-btn>

<!--          NEW TODO-->
          <transition
            name="slide"
          >
            <div
                v-if="addNewTodo == true"
                class="new__todo">
              <v-text-field
                  @keydown.enter="addTodo"
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
                <div
                    v-click-outside="clearDate"
                    class="date__time">
                  <v-date-picker
                      v-model="date"
                      v-if="!chooseTime"
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
                  <v-time-picker
                      format="24hr"
                      v-model="time"
                      v-else
                  >
                    <v-spacer></v-spacer>
                    <v-btn
                        text
                        color="primary"
                        @click="closeDateTime"
                    >
                      Cancel
                    </v-btn>
                    <v-btn
                        text
                        color="primary"
                        @click="saveDateTime(time)"
                    >
                      OK
                    </v-btn>

                  </v-time-picker>
                </div>
              </v-menu>

              <v-btn
                  icon
                  :disabled="newTodo.length === 0"
                  @click="addTodo"
              >
                <v-icon
                >
                  mdi-check
                </v-icon>
              </v-btn>
            </div>
          </transition>

<!--          <v-hover>-->
<!--            <template v-slot:default="{ hover }">-->
          <transition-group
              v-if="todoList.tasks"
              name="list">
              <div
                  v-for="todo in todoList.tasks"
                  :key="todo.id"
                  class="todo__item"

              >
                <v-checkbox
                    ref="check"
                    color="indigo darken-3"
                    class="rounded-bl-circle"
                    v-model="todo.is_completed"
                    @click="completeTask(todo.id)"
                    hide-details
                ></v-checkbox>

                <p
                  :class="{'completed-task': todo.is_completed}"
                  @click="onPClick"
                >{{ todo.title }}</p>

                <small
                :class="{'date__info': true, 'red--text': todo.expired_time < todayDate, 'green--text':
                todo.expired_time > todayDate}"
                v-if="todo.expired_time"
                >
                  <v-icon
                  small
                >
                    mdi-calendar
                  </v-icon>
                  {{new Date(todo.expired_time).toDateString()}}
                </small>
                <v-spacer></v-spacer>
                <v-btn
                    icon
                    @click="showTodoDetail(todo.id)"
                >
                  <v-icon>mdi-dots-vertical</v-icon>
                  <p
                  ></p>
                </v-btn>
                <v-btn
                    @click="addToFavorite(todo.id)"
                    icon
                    color="indigo"

                >
                  <v-icon
                  v-if="todo.is_favorite"
                  >mdi-star</v-icon>

                  <v-icon
                  v-else
                  >mdi-star-outline</v-icon>
                </v-btn>
                <div
                    v-if="todo.detail"
                    class="todo__detail">
                  <p>Lorem ipsum dolor.</p>
                  <p>Lorem ipsum.</p>
                  <p>Lorem ipsum dolor sit.</p>
                </div>
              </div>
          </transition-group>

<!--            </template>-->
<!--          </v-hover>-->
          <div
              v-else
              class="badge__centered">
            <h3>Here is no todos, create now!</h3>
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
<!--        </v-card>-->
          </v-card>
      </v-flex>
    </v-layout>


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



<!--    delete list dialog-->
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


<!--    share project dialog-->
    <v-dialog
        width="500px"
        v-model="shareDialog"
    >
      <v-card
      >
        <v-card-title>
          Select user to share account
        </v-card-title>
        <v-autocomplete
            hide-no-data
            hide-selected
            v-model="selectedUser"
            class="ml-5 mr-5"
            :items="usersForShare"
        label="Enter usrename or name of user"
        >
        </v-autocomplete>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            @click="shareDialog = false"
          >Cancel</v-btn>
          <v-btn
            @click="shareList"
          >Share</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</div>
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

      deleteDialog: false,

      usersList: [],

      selectedUser: null,

      todoList: {
        id: 0,
        tasks: [],
        name: '',
        favorite: false,
        owner: null,
        cover: '',
        percentageCompleted: 0.0,
        sharedOwners: []
      },
      newTodo: '',
      todoType: 10,

      shareDialog: false,

      isNewTodoUsing: false,

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
      initialSelected: [],
      coverPicker: false,
      selectedCover: null,

      userListLoading: false,
      usersForShare: [],
      userForShareData: [],

      chooseTime: false,
      tempDate: null,
      time: '00:00',

      addNewTodo: false

    }
  },
  computed: {

    heart () {
      if (this.todoList.favorite) {
        return  this.heartIcon
      }
      else {
        return this.heartOutlinedIcon
      }
    },

    loading () {
      return this.$store.getters.loading
    },

    percent () {
      let totalTodoCount = this.todoList.tasks.length

      let totalCompletedTasks = 0
      // for (task in this.todoList.tasks) {
      //   if (task.is_completed) {
      //     totalCompletedTasks ++
      //   }
      // }

      if (this.todoList.tasks.length == 0) {
       return 0
      }
      else {
        this.todoList.tasks.forEach(task => {
          if (task.is_completed) {
            totalCompletedTasks++
          }
        })
        let percentCompleted = Math.round((totalCompletedTasks / totalTodoCount) * 100)
        return percentCompleted
      }
    }

  },
  methods: {
    closeDateTime () {
      this.menu = false
      this.chooseTime = false
    },

    onPClick () {
      this.$refs.check.click()

    },

    loadUsersForShare () {
      this.userListLoading = true

      axios.get('http://localhost:8000/api/auth/user/',
          {
            headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
          })
          .then(response => {
            response.data.forEach(user => {
              if (this.$store.getters.user.username !== user.username) {
                if (user.first_name && user.last_name && !(user in this.todoList.sharedOwners)) {
                  this.usersForShare.push(user.first_name + user.last_name)
                } else {
                  this.usersForShare.push(user.username)
                }
                this.userForShareData.push(user)
              }
            })
          })

      this.shareDialog = true
      this.userListLoading = false
    },
    star (todo_id) {
      if (this.todoList.tasks[0].is_favorite) {
        return  this.starIcon
      }
      else {
        return this.outlineStarIcon
      }
    },

    deleteToDo () {
      this.$store.dispatch('setLoading', true)

      const config = {
        headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
      };

      axios.delete('http://localhost:8000/api/todo/class=""/' + this.$route.params['id'] + '/',
          config
      )
      .then(response => {
        this.todoList = null
        this.$router.push('/all-todo-lists')
      })
      this.$store.dispatch('setLoading', false)

      this.$notify({
        title: "<p>You have successfully deleted the list</p>",
        type: 'success'
      })
    },

    onSelectCover (data) {
      this.selectedCover = data
    },

    completeTask (todo_id) {

      const url = 'http://127.0.0.1:8000/api/todo/todo/' + todo_id + '/'
      const config = {
        headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
      };
      const todo = this.todoList.tasks.filter(task => {
        return task ? task.id === todo_id: null
      })[0]

      // TODO Fix reloading

      // TODO Update request, to update not all list, actually specific todo item
      axios.patch(url, {
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
                    this.todoList.cover = response.data.cover
                    this.todoList.percentageCompleted = response.data.percentage_completed
                    this.todoList.percentageCompleted *= 100
                    this.todoList.sharedOwners = response.data.shared_owners
                    this.$store.dispatch('setLoading', false)


                    for (let i=0; i< this.todoList.tasks.length; i++) {
                      this.todoList.tasks[i] = Object.assign(this.todoList.tasks[i], {detail: false})
                    }
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

    saveDate (date) {
      this.isDateUsing = true
      this.chooseTime = true

    },

    saveDateTime(time) {
      this.$refs.menu.save(new Date(this.date + 'T' + time))
    },



    shareList () {
      this.$store.dispatch('setLoading', true)
      var userForShare = null
      this.userForShareData.forEach(user => {
        if (user.first_name && user.last_name) {
          if (user.first_name + user.last_name == this.selectedUser) {
            userForShare = user
          }
        }
        else {
          if (user.username == this.selectedUser) {
            userForShare = user
          }
        }
      })
      console.log(userForShare)

      axios.patch('http://localhost:8000/api/todo/project/' + this.$route.params['id'] + '/',
          {
            shared_owners: userForShare.pk
          },
          {
            headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
          }
      )
      .then(response => {
        this.$notify({
          group: 'main',
          type: 'info',
          title: 'You shared ' +this.todoList.name,
          text: 'You have just shared the list, we will notify ' + userForShare.username
        })
      })
      this.$store.dispatch('setLoading', false)

      this.shareDialog = false
      this.selectedUser = null
    },

    chooseCover () {
      // TODO Add cover picker
      this.$store.dispatch('setLoading', true)
      this.coverPicker = false

      let coverSrc = this.selectedCover.src.replace('/img/', '').split('.')
      coverSrc = coverSrc[0] + "." + coverSrc[2]

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
              this.todoList.cover = response.data.cover
              this.todoList.percentageCompleted = response.data.percentage_completed
              this.todoList.percentageCompleted *= 100
              this.todoList.sharedOwners = response.data.shared_owners

              for (let i=0; i< this.todoList.tasks.length; i++) {
                this.todoList.tasks[i] = Object.assign(this.todoList.tasks[i], {detail: false})
              }
            })
            .catch(error => {
              this.$store.dispatch('setError', error.message)
            })
      })

      this.$store.dispatch('setLoading', false)
    },

    clearDate () {
      this.isDateUsing = false
      this.date = null
      this.time = null

    },

    addToFavorite (todo_id) {
      const url = 'http://127.0.0.1:8000/api/todo/todo/' + todo_id + '/'
      const config = {
        headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
      };
      const todo = this.todoList.tasks.filter(task => {
        return task ? task.id === todo_id: null
      })[0]

      // TODO Update request, to update not all list, actually specific todo item

      axios.patch(url, {
        is_favorite: !todo.is_favorite
      },{
        headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
      })
      .then(response => {
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
              this.todoList.cover = response.data.cover
              this.todoList.tasks = response.data.tasks
              this.todoList.percentageCompleted = response.data.percentage_completed
              this.todoList.percentageCompleted *= 100
              this.todoList.sharedOwners = response.data.shared_owners

              for (let i=0; i< this.todoList.tasks.length; i++) {
                this.todoList.tasks[i] = Object.assign(this.todoList.tasks[i], {detail: false})
              }

            })
            .catch(error => {
              this.$store.dispatch('setError', error.message)
            })
      })
    },
    openDialog() {
      this.dialog = true
    },

    showTodoDetail (todoId) {
      let index = -1

      for (let i=0;i < this.todoList.tasks.length; i++) {
        if (this.todoList.tasks[i]['id'] == todoId) {
          index = i
        }
      }
      this.todoList.tasks[index].detail = true
    },

    addListToFavorite () {
      const url = 'http://localhost:8000/api/todo/project/' + this.todoList.id + '/'
      const config = {
        headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
      };

      axios.patch(url, {
        favorite: !this.todoList.favorite
      },
      config)
      .then(response => {
        // TODO notify
        this.todoList.favorite = !this.todoList.favorite
        this.$emit('updateHeart', this.heart)
      })
      .catch(error => {

      })

    },

    addTodo () {
      const url = 'http://127.0.0.1:8000/api/todo/todos/'
      const config = {
        headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}` }
      };
      if (this.isDateUsing) {

        axios.post(url, {
          title: this.newTodo,
          todo_list_id: this.$route.params['id'],
          todo_list_type: this.todoType,
          expired_time: this.date
        }, {
          headers: {Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}`}
        })
            .then(response => {
              this.date = new Date().toISOString().substr(0, 10),
                  this.newTodo = ''
              const url = 'http://localhost:8000/api/todo/project/' + this.$route.params['id'] + '/'
              const config = {
                headers: {Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}`}
              };

              this.addNewTodo = false

              axios.get(url, config)
                  .then(response => {
                    this.todoList.id = response.data.id
                    this.todoList.name = response.data.name
                    this.todoList.owner = response.data.owner
                    this.todoList.favorite = response.data.favorite
                    this.todoList.tasks = response.data.tasks
                    this.todoList.cover = response.data.cover
                    this.todoList.percentageCompleted = response.data.percentage_completed
                    this.todoList.percentageCompleted *= 100
                    this.todoList.sharedOwners = response.data.shared_owners

                    for (let i=0; i< this.todoList.tasks.length; i++) {
                      this.todoList.tasks[i] = Object.assign(this.todoList.tasks[i], {detail: false})
                    }

                  })
                  .catch(error => {
                    this.$store.dispatch('setError', error.message)
                  })

            })
            .catch(error => {
              console.log(error)

            })

        const reloadUrl = 'http://localhost:8000/api/todo/project/' + this.$route.params['id'] + '/'
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
              this.todoList.percentageCompleted = response.data.percentage_completed
              this.todoList.percentageCompleted *= 100
              this.todoList.sharedOwners = response.data.shared_owners

              for (let i=0; i< this.todoList.tasks.length; i++) {
                this.todoList.tasks[i] = Object.assign(this.todoList.tasks[i], {detail: false})
              }

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
              const url = 'http://localhost:8000/api/todo/project/' + this.$route.params['id'] + '/'
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
                    this.todoList.percentageCompleted = response.data.percentage_completed
                    this.todoList.percentageCompleted *= 100
                    this.todoList.sharedOwners = response.data.shared_owners

                    for (let i=0; i< this.todoList.tasks.length; i++) {
                      this.todoList.tasks[i] = Object.assign(this.todoList.tasks[i], {detail: false})
                    }
                  })
                  .catch(error => {
                    this.$store.dispatch('setError', error.message)
                  })

            })
            .catch(error => {
              console.log(error)

            })

        const reloadUrl = 'http://localhost:8000/api/todo/project/' + this.$route.params['id'] + '/'
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
              this.todoList.percentageCompleted = response.data.percentage_completed
              this.todoList.percentageCompleted *= 100
              this.todoList.sharedOwners = response.data.shared_owners

              for (let i=0; i< this.todoList.tasks.length; i++) {
                this.todoList.tasks[i] = Object.assign(this.todoList.tasks[i], {detail: false})
              }

            })
            .catch(error => {
              this.$store.dispatch('setError', error.message)
            })

      }

      this.isDateUsing = false

    }
  },

  mounted() {
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
          this.todoList.cover = response.data.cover
          this.todoList.percentageCompleted = response.data.percentage_completed
          this.todoList.percentageCompleted *= 100
          this.todoList.sharedOwners = response.data.shared_owners

          for (let i=0; i< this.todoList.tasks.length; i++) {
            this.todoList.tasks[i] = Object.assign(this.todoList.tasks[i], {detail: false})
          }
        })
        .catch(error => {
          this.$store.dispatch('setError', error.message)
        })


  }

}
</script>

<style>
* {
  font-family: 'Proxima Nova Semibold', sans-serif;
}

.card__header__text {
  font-family: 'Andika New Basic', sans-serif;
}

.main-card {
  overflow: hidden;
  height: 100%;
  min-height: 100%;
  justify-content: space-between;
  margin-top: 0;

}

.custom__checkbox {
  z-index: 0;
  position: absolute;
  opacity: 0;
}

.custom__checkbox+label {
  display: inline-flex;
  align-items: center;
  user-select: none;
}
.custom__checkbox+label::before {
  content: '';
  display: inline-block;
  width: 1em;
  height: 1em;
  flex-shrink: 0;
  flex-grow: 0;
  border: 1px solid #adb5bd;
  border-radius: 50%;
  margin-right: 0.5em;
  background-repeat: no-repeat;
  background-position: center center;
  background-size: 50% 50%;
}

.custom-checkbox:checked+label::before {
  border-color: #0b76ef;
  background-color: #0b76ef;
}

/* стили при наведении курсора на checkbox */
.custom-checkbox:not(:disabled):not(:checked)+label:hover::before {
  border-color: #b3d7ff;
}
/* стили для активного состояния чекбокса (при нажатии на него) */
.custom-checkbox:not(:disabled):active+label::before {
  background-color: #b3d7ff;
  border-color: #b3d7ff;
}
/* стили для чекбокса, находящегося в фокусе */
.custom-checkbox:focus+label::before {
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}
/* стили для чекбокса, находящегося в фокусе и не находящегося в состоянии checked */
.custom-checkbox:focus:not(:checked)+label::before {
  border-color: #80bdff;
}
/* стили для чекбокса, находящегося в состоянии disabled */
.custom-checkbox:disabled+label::before {
  background-color: #e9ecef;
}

.todo__item {
  border-radius: 5px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  padding: 0;
  background-color: #121212;
  max-height: 65px;
}

.todo__item:hover {
  padding-left: 5px;
  transition: padding-left .2s;
}

.todo__item:last-child {
  margin-bottom: 25px;
}

.item__checkbox {
  margin: 0;
  padding: 0;
  border-radius: 50%;

}
p {
  margin: 0;
  padding: 0;
}

.card__header1 {
  margin: 25px 15px;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}

.header__image {
  margin: 0;
}

.new__todo {
  display: flex;
  padding: 10px 30px;
  justify-content: space-between;
  align-items: center;
}
.add__todo {
  max-width: 85%;
  margin-right: 50px;
}
.date__info {
  margin-left: 10px;
}

.completed-task {
  text-decoration: line-through;
}

.progress {
  position: fixed;
  right: 5%;
  top: 10%;
  margin-right: 5px;
  margin-top: 5px;
}

.main {
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 1s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active до версии 2.1.8 */ {
  opacity: 0;
  transition: opacity .8s;
}

.slide-enter-active {
  transition: all .3s ease;
}
.slide-leave-active {
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-enter, .slide-leave-to
  /* .slide-fade-leave-active до версии 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}

.list-enter-active, .list-leave-active {
  transition: all 1s;
}
.list-enter, .list-leave-to /* .list-leave-active до версии 2.1.8 */ {
  opacity: 0;
  transform: translateY(30px);
}
</style>
