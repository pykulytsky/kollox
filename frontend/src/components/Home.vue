<template>
  <div class="wrapper">

    <div class="header__section base-section">
      <h2>Hello, {{ user.username }}</h2>
    </div>

    <div class="content__section base-section">

      <div class="favorites_section base-section">
        <h2>Favorites lists</h2>
        <div class="lists_grid">
          <home-small-card></home-small-card>
          <home-small-card></home-small-card>
          <home-small-card></home-small-card>
          <home-small-card></home-small-card>

          <p
            class="add_new"
          >+ Add new</p>
        </div>
      </div>

      <div class="content_body base-section">
        <div class="my__day__header">
          <h2>My day</h2>
          <p>{{ today }}</p>
        </div>
      </div>

    </div>
    

    <div class="last__section base-section">
      <div class="last__list__section base-section">

        <h2 class="text--center">Last lists</h2>
        
        <v-row>
          <v-col
            v-for="n in 12"
            :key="n"
            cols="3"
            md="6"
            sm="12"
          >
            <home-small-card></home-small-card>
          </v-col>
        </v-row>

      </div>

      <div class="last__todo__section base-section">
        <div class="calendar__header">
          <h2>Calendar</h2>
          <v-btn
            icon
            to="/calendar"
          >
            <v-icon
              x-small
            >
              mdi-chevron-right
            </v-icon>
          </v-btn>
        </div>
        <calendar class="small__calendar"></calendar>
      </div>
    </div>
  </div>
</template>

<script>
import HomeSmallCard from '@/components/core/HomeSmallCard.vue'
import CalendarComponent from './core/CalendarComponent.vue'

export default {
  title: 'home',

  components: {
    homeSmallCard: HomeSmallCard,
    calendar: CalendarComponent
  },

  data: () => {
    return {
      today: new Date(Date.now()).toDateString()
    }
  },

  computed: {
    user () {
      return this.$store.getters.user
    }

  },
}
</script>

<style>

.header__section {
  justify-content: center;
}

.base-section {
  display: flex;
}

.wrapper {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;

}

.content_body  {
  display: flex;
  flex-direction: column;
  min-width: 60%;
  max-width: 60%;

  padding: 10px;
}

.content_body h2 {
  align-self: center;
  margin-bottom: 8px;
}

.last__section {
  flex-direction: row;
  justify-content: space-around;
}

.content__section {
  flex-direction: row;
  justify-content: space-around;
}

.favorites_section {
  flex-direction: column;
  align-items: center;
}

.lists_grid {
  display: flex;
  flex-direction: column;
  padding-top: 4px;
}


.add_new {
  color: grey;
  cursor: pointer;
  align-self: flex-end;
  margin-right: 5px;
  margin-top: 5px;
}

.add_new:hover {
  text-decoration: underline;
}

.last__list__section {
  min-width: 50%;
  max-width: 50%;
  flex-direction: column;
}

.center {
  align-self: center;
}


.small__calendar {
  max-height: 300px;
  
}

.last__todo__section {
  flex-direction: column;

}

.calendar__header {
  display: flex;
}

.my__day__header {
  display: flex;
  justify-content: space-between;
}

</style>