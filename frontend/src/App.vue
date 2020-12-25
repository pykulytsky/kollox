<template>
  <v-app>
    <v-navigation-drawer
        app
        class="grey darken-4"
        v-model="drawer"
        dark

    >
      <v-list>
        <v-list-item class="px-2" v-if="user">
          <v-list-item-avatar v-if="isUserHasAvatar">

            <v-img
                :src="user.avatar"></v-img>
          </v-list-item-avatar>
          <v-avatar
              v-else
              color="indigo">
            <v-icon dark>
              mdi-account-circle
            </v-icon>
          </v-avatar>
        </v-list-item>

        <v-list-item
            class="drawer__profile"
            v-if="user"
            to="/profile"
            link>
          <v-list-item-content>
            <v-list-item-title
                v-if="user.firstName && user.lastName"
                class="title">
              {{ user.firstName }} {{ user.lastName }}
            </v-list-item-title>


            <v-list-item-title
                v-else
                class="title">
              {{ user.username }}
            </v-list-item-title>
            <v-list-item-subtitle>{{ user.email }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>
      <v-list>

        <v-list-item
            class="drawer__item"
            @click="drawer = false"
            v-for="item in links"
            :key="item.name"
            link
            :to="item.url"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title
            >{{ item.name }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

    </v-navigation-drawer>

    <v-app-bar
        :loading="loading"
        app
        color="grey darken-4"
        dense
        dark
    >
      <v-app-bar-nav-icon
      @click="drawer = !drawer"
      ></v-app-bar-nav-icon>

      <v-toolbar-title class="card__header__text">KOLLOX</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn
          v-if="isDetailPageRoute"
          @click="isListFavorite = !isListFavorite"
          icon>
        <v-icon>{{heart}}</v-icon>
      </v-btn>
      <v-menu
          v-model="searchMenu"
          :close-on-content-click="false"
      >

      <template v-slot:activator="{on, attrs}">
          <v-btn
              v-bind="attrs"
              v-on="on"
              icon>
            <v-icon>mdi-magnify</v-icon>
          </v-btn>
      </template>
        <div class="search__dialog">
          <v-text-field
              @keydown.enter="search"
              v-model="searchParams"
              placeholder="Search..."
              class="search__input"
          ></v-text-field>
        </div>
      </v-menu>
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
              v-for="link in links"
              :key="link.name"
              @click="() => {}"
              :to="link.url"
          >
            <v-list-item-title>
              <v-icon left>{{ link.icon }}</v-icon>
              {{ link.name }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    <v-main>
      <router-view>

      </router-view>
    </v-main>
    <notifications group="main" position="bottom right"/>
    <notifications position="top center" group="loginError"/>
  </v-app>
</template>

<script>
import Navbar from "@/components/core/Navbar";

export default {
  name: 'App',

  components: {
    navBar: Navbar
  },

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

      searchParams: '',
      searchMenu: false
    }
  },
  computed: {
    user () {
      return this.$store.getters.user
    },
    star () {
      if (this.favorite) {
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

    error () {
      return this.$store.getters.error
    },
    links () {
      if (this.isUserAuthenticated) {
        return [
          {
            url: '/calendar',
            icon: 'mdi-calendar',
            name: 'Calendar'
          },
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
      }
      else {
        return [
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
        ]
      }
    },

    isUserHasAvatar () {
      try {
        return !!this.user.avatar
      }
      catch (error) {
        return false
      }
    },

    isUserAuthenticated () {
      return this.$store.getters.isAuthenticated
    },

    isDetailPageRoute () {
      return !!this.$route.params['id'];
    },
    loading () {
      return this.$store.getters.loading
    }
  },
  watch: {
    error () {
      if (this.error !== null) {
        if (this.$router.currentRoute.path == '/login') {
          if (this.error == "Request failed with status code 400") {
            this.$notify({
              group: 'loginError',
              type: 'error',
              title: "<p class='text-center'>Incorrect login credentials</p>"
            })
          }
        } else {
          this.$notify({
            group: 'main',
            type: 'error',
            title: this.error
          })
        }
      }
    }
  },
  methods: {
    search () {
      this.searchMenu = false
      this.$router.push('/search?s=' + this.searchParams)
      this.searchParams = ''
    },

    addToFavorite () {
      this.favorite = !this.favorite
    },
    openDialog() {
      this.dialog = true
    },
    closeError () {
      this.$store.dispatch('clearError')
    }
  },
  updated() {
  },

  beforeCreate() {
    try {
      this.$store.dispatch('loadUser')
      this.$store.dispatch('autoLogin')
    }
    catch (error) {
      this.$store.dispatch('setError', error.message)
      this.$router.push('/404')
    }
  }


};
</script>

<style>
@font-face {
  font-family: 'Proxima Nova Semibold';
  src: url('assets/fonts/ProximaNova-Semibold.eot');
  src: url('assets/fonts/ProximaNova-Semibold.eot?#iefix') format('embedded-opentype'),
  url('assets/fonts/ProximaNova-Semibold.woff') format('woff'),
  url('assets/fonts/ProximaNova-Semibold.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}

* {
  font-family: 'Proxima Nova Semibold', sans-serif;
}

.drawer__profile:hover {
  padding-left: 5px;
  transition: padding-left .4s ;
}

.drawer__item:hover {
  padding-left: 40px;
  transition: padding-left .4s ;
}

.notification-title {
  color: #121212;
  font-size: 14px;
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
.item__checkbox {
  margin: 0;
  padding: 0;
}
p {
  margin: 0;
  padding: 0;
}

.card__header1 {
  margin: 5px 15px;
  display: flex;
  justify-content: space-between;
}

.search__input {
  background-color: #121212 ;
  padding: 0px 15px;
  border-radius: 15px;
  max-height: 40px;
  overflow: hidden;
  border: 0;
}

.error__bar {
  padding: 0;
  display: flex;
  justify-content: space-between;
}
.err_btn {
  margin-left: 130px;
}
</style>
