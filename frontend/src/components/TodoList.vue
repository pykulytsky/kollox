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
              src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
              height="200px"
          ></v-img>
          <div class="card__header1">
            <h2 class="card__header__text">{{ todoList.name }}</h2>
            <v-btn
                icon
                v-on="on"
            >
              <v-icon>mdi-dots-vertical</v-icon>
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

      todoList: {
        id: 0,
        tasks: [],
        name: '',
        favorite: false,
        owner: null
      }
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