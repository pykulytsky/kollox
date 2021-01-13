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
        <h2>Last actions</h2>

        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate accusantium at numquam molestias, nemo iste deserunt earum modi ea perspiciatis aspernatur fugiat laudantium saepe sint. Velit minima corporis magnam eaque.</p>
      </div>

    </div>

    <div class="last__section base-section">
      <div class="last__list__section base-section">
        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ratione, ab?</p>
      </div>

      <div class="last__todo__section base-section">
        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ratione, ab?</p>
      </div>
    </div>
  </div>
</template>

<script>
import HomeSmallCard from '@/components/core/HomeSmallCard.vue'

export default {
  title: 'home',

  components: {
    homeSmallCard: HomeSmallCard
  },

  data: () => {
    return {

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

</style>