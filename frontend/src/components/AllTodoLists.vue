<template>
<v-container>
  <v-row
  v-if="!loading && todoLists.length !== 0"
  >
  <div
      v-for="list in todoLists"
      :v-key = "list.id"
      class="col-md-4">
    <v-hover>
      <template v-slot:default="{ hover }">
        <v-card
            link
            :elevation="hover ? 10 : 3"
            :to="list.todo_list_type == 'project' ? '/project/' + list.data.id + '/?favorite=' +
            list.data.favorite :
            '/simple-todo-list/' +
            list.data.id + '/?favorite=' +
            list.data.favorite"
            class="mx-auto"
            max-width="344"
        >
          <v-img
              v-if="list.data.cover"
              :src="list.data.cover"
              height="200px"
          ></v-img>

          <v-card-title>
            {{ list.data.name }}
          </v-card-title>
          <v-card-actions>
            <v-spacer></v-spacer>
            <small> {{ list.data.total_completed_tasks }} of {{ list.data.total_tasks }}</small>
          </v-card-actions>

    <!--      <v-card-subtitle>-->
    <!--        {{ list.data.id }}-->
    <!--      </v-card-subtitle>-->

      <!--      <v-card-actions>-->
      <!--        <v-btn-->
      <!--            color="orange lighten-2"-->
      <!--            text-->
      <!--        >-->
      <!--          Explore-->
      <!--        </v-btn>-->

      <!--        <v-spacer></v-spacer>-->

      <!--&lt;!&ndash;        <v-btn&ndash;&gt;-->
      <!--&lt;!&ndash;            icon&ndash;&gt;-->
      <!--&lt;!&ndash;            @click="show = !show"&ndash;&gt;-->
      <!--&lt;!&ndash;        >&ndash;&gt;-->
      <!--&lt;!&ndash;          <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>&ndash;&gt;-->
      <!--&lt;!&ndash;        </v-btn>&ndash;&gt;-->
      <!--      </v-card-actions>-->

    <!--      <v-expand-transition>-->
    <!--        <div v-show="show">-->
    <!--          <v-divider></v-divider>-->

    <!--          <v-card-text>-->
    <!--            I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.-->
    <!--          </v-card-text>-->
    <!--        </div>-->
    <!--      </v-expand-transition>-->
        </v-card>
      </template>
    </v-hover>
  </div>
  </v-row>
  <div
      v-if="todoLists.length == 0"
      class="no__todo_png">
      <v-img
          class="no_todo"
          width="450px"
          height="450px"
        src="../assets/kisspng-computer-icons-action-item-share-icon-5b382cee0fab25.5919305715304081740642.png"
      >
      </v-img>
      <h3
      class="no_todo_text"
      >Here is no todo lists, try to add one by clicking the '+' button!</h3>
  </div>


  <v-btn
      class="float__btn grey darken-4"
      fixed
      @click="openDialog"
      dark
      fab
      bottom
      right
  >
    <v-icon>mdi-plus</v-icon>
  </v-btn>

  <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
  >

    <v-card>
      <v-card-title>
        <span class="headline">Create new todo list</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-radio-group
                v-model="todoListType"
                row
                @change="checkType"
            >
              <v-radio
                  label="Simple Todo list"
                  value="0"
              ></v-radio>
              <v-radio
                  label="Project"
                  value="1"
              ></v-radio>
            </v-radio-group>
<!--            <v-col-->
<!--                cols="12"-->
<!--                sm="6"-->
<!--                md="4"-->
<!--            >-->
<!--              <v-text-field-->
<!--                  label="Legal first name*"-->
<!--                  required-->
<!--              ></v-text-field>-->
<!--            </v-col>-->
<!--            <v-col-->
<!--                cols="12"-->
<!--                sm="6"-->
<!--                md="4"-->
<!--            >-->
<!--              <v-text-field-->
<!--                  label="Legal middle name"-->
<!--                  hint="example of helper text only on focus"-->
<!--              ></v-text-field>-->
<!--            </v-col>-->
<!--            <v-col-->
<!--                cols="12"-->
<!--                sm="6"-->
<!--                md="4"-->
<!--            >-->
<!--              <v-text-field-->
<!--                  label="Legal last name*"-->
<!--                  hint="example of persistent helper text"-->
<!--                  persistent-hint-->
<!--                  required-->
<!--              ></v-text-field>-->
<!--            </v-col>-->
            <v-col cols="12">
              <v-text-field
                  label="Name*"
                  v-model="newToDoListName"
                  required
              ></v-text-field>
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
            @click="onCreateSubmit"
        >
          Create
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</v-container>
</template>

<script>
import axios from 'axios'

export  default {
  title: 'All todo lists',
  data: () => {
    return {
      dialog: false,
      todoListType: 0,
      newToDoListName: ''
    }
  },
  computed: {
    todoLists () {
      return this.$store.getters.allLists
    },
    loading () {
      return this.$store.getters.loading
    },
    linkToList (list) {
      if (list.todo_list_type == 'simpletodolist') {
        return '/simple-todo-list/' + list.id + '/?favorite=' + list.id
      }
      else if  (list.todo_list_type == 'project'){
        return '/project/' + list.id + '/?favorite=' + list.id
      }
      else {
        this.$store.dispatch('setError', "Wrong way.")
      }
    }
  },

  methods: {
    checkType () {
      console.log("Type: ", this.todoListType)
    },

    openDialog() {
      this.dialog = true
    },

    onCreateSubmit () {
      if (this.todoListType == 0) {

        axios.post('http://localhost:8000/api/todo/simple-todo-lists/', {'name':
          this.newToDoListName}, {
        headers: {
          Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}`
        }})

      }
      else if (this.todoListType == 1) {
        axios.post('http://localhost:8000/api/todo/projects/', {'name': this.newToDoListName},
            {headers: {
              Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}`
              }})
      }

      this.$store.dispatch('loadAllTodoLists')
      this.dialog = false


    }
  },
  
  updated() {
    console.log(this.$route)

  },
  mounted() {
    this.$store.dispatch('loadAllTodoLists')

    if (this.$route.query['msg']) {
      this.$notify({
        group: 'main',
        type: 'info',
        title: 'Verify your email',
        text: 'Your email is not verified please do it'
      })
    }
  },
}

</script>

<style>
.float__btn {
  margin-bottom: 10px;
  margin-right: 10px;
}

.no__todo_png {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.no_todo_text {
  margin-top: 20px;
  color: #353535;
}
</style>
