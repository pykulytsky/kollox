<template>
  <v-container>
    <div
        elevation="16"
        class="profile__main">

      <div class="img__section">
        <v-img
            max-height="300px"
            max-width="300px"
            class="main__img"
        :src="user.avatar"
        ></v-img>
        <h2
        class="name"
        >Oleg Pykulytsky</h2>
      </div>

      <div class="data__section">
        <div class="data__item">
          <h2>Detail</h2>
        </div>
        <div class="data__item">
          <p>First Name</p>
          <p>Oleg</p>
        </div>
        <div class="data__item">
          <p>Last Name</p>
          <p>Pykulytsky</p>
        </div>
        <div class="data__item">
          <p>Age</p>
          <p>20</p>
        </div>
        <div class="data__item">
          <p>E-mail</p>
          <p>pykulytsky@mail.com</p>
        </div>

        <div class="data__item">
          <v-spacer></v-spacer>
          <v-btn>Edit profile</v-btn>
        </div>
      </div>

    </div>
  </v-container>
</template>

<script>

export default {
  title: 'Profile',
  data: () => {
    return {

    }
  },

  beforeCreate() {
    this.$store.dispatch('loadUser')
  },
  computed: {
    loading () {
      return this.$store.getters.loading
    },

    user () {
      return this.$store.getters.user
    }
  }
}
</script>

<style>
.profile__main {
  margin: 30px 40px;
  background-color: #282828;
  border-radius: 10px;
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  flex-wrap: wrap;
}

.img__section {
  margin-left: 50px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  max-width: 50%;
}

.data__section {
  margin-right: 50px;
  margin-top: 10px;
  margin-bottom: 10px;
  padding: 10px;
  background-color: #121212;

  border-radius: 3px  ;
  display: flex;
  flex-direction: column;
  min-width: 50%;

}

.main__img {
  margin: 10px 0px;
  border-radius: 10px;
}

.name {
  align-self: center;
}

.data__item {
  width: 100%;
  display: flex;
  justify-content: space-between;

  padding: 0 50px;

}

.data__item p {
  font-size: 20px;
}

.data__item h2 {
  justify-self: center;
}

</style>