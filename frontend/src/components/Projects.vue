<template>
  <v-container>
    <v-row
        v-if="!loading"
    >
      <div
          v-for="list in todoLists"
          :v-key = "n"
          class="col-md-4">
        <v-card
            class="mx-auto"
            max-width="344"
        >
          <v-img
              src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
              height="200px"
          ></v-img>

          <v-card-title>
            {{ list.data.name }}
          </v-card-title>

          <v-card-subtitle>
            1,000 miles of wonder
          </v-card-subtitle>

          <v-card-actions>
            <v-btn
                color="orange lighten-2"
                text
            >
              Explore
            </v-btn>

            <v-spacer></v-spacer>

            <v-btn
                icon
                @click="show = !show"
            >
              <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
            </v-btn>
          </v-card-actions>

          <v-expand-transition>
            <div v-show="show">
              <v-divider></v-divider>

              <v-card-text>
                I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
              </v-card-text>
            </div>
          </v-expand-transition>
        </v-card>
      </div>
    </v-row>
    <v-progress-circular
        v-else
        indeterminate
        color="primary"
    ></v-progress-circular>
    <v-btn
        class="float__btn deep-purple accent-4"
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
              >
                <v-radio
                    label="Simple Todo list"
                    value="simpleList"
                ></v-radio>
                <v-radio
                    label="Project"
                    value="project"
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
  data: () => {
    return {
      dialog: false,
      todoListType: 'simpleList',
      newToDoListName: ''
    }
  },
  computed: {
    todoLists () {
      return this.$store.getters.allLists
    },
    loading () {
      return this.$store.getters.loading
    }
  },

  methods: {
    openDialog() {
      this.dialog = true
    },

    onCreateSubmit() {
      axios.post('http://localhost:8000/api/todo/projects/', {'name': this.newToDoListName},
          {
            headers: {
              Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}`
            }
          })

      this.$store.dispatch('loadAllTodoLists')
      this.dialog = false

    },
  }
  mounted() {
    this.$store.dispatch('loadAllTodoLists')

  }
}

</script>

<style>
.float__btn {
  margin-bottom: 10px;
  margin-right: 10px;
}
</style>