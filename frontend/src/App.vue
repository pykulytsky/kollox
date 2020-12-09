<template>
  <v-app>
    <v-navigation-drawer
        app
        class="deep-purple accent-4"
        v-model="drawer"
        dark

    >
      <v-list>
        <v-list-item
            v-for="item in links"
            :key="item.name"
            link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.name }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <template v-slot:append>
        <div class="pa-2">
          <v-btn block>
            Logout
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>

    <v-app-bar
        app
        color="deep-purple accent-4"
        dense
        dark
    >
      <v-app-bar-nav-icon
      @click="drawer = !drawer"
      ></v-app-bar-nav-icon>

      <v-toolbar-title class="card__header__text">Page title</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn
          @click="isListFavorite = !isListFavorite"
          icon>
        <v-icon>{{heart}}</v-icon>
      </v-btn>
      <v-menu
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

          <v-text-field
              placeholder="Search..."
              @click="() => {}"
          class="search__input"
          ></v-text-field>

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
      heartOutlinedIcon: 'mdi-heart-outline'
    }
  },
  computed: {
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

    links () {
      return this.$store.getters.links
    }
  },
  methods: {
    addToFavorite () {
      this.favorite = !this.favorite
    },
    openDialog() {
      this.dialog = true
    }
  }

};
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


</style>
