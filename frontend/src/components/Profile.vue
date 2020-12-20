<template>
  <div>
    <v-img
        class="profile__cover"
        src="https://images.unsplash.com/photo-1543274420-090dfb67739d?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1077&q=80"
    >
      <div class="user__info">
        <v-img
        :src="user.avatar"
        class="avatar"
        >

        </v-img>

        <h2>{{ user.firstName }}  {{ user.lastName }}</h2>
      </div>
    </v-img>
    <v-container>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi cum fugiat in itaque labore minima minus officiis reiciendis sequi veniam.</p>

    </v-container>
  </div>
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

.data__item p {
  font-size: 20px;
}

.data__item h2 {
  justify-self: center;
}

.profile__cover {
  max-height: 250px;
}

.avatar {
  /*position: absolute;*/
  /*top: 40%;*/
  /*left: 50%;*/
  width: 150px;
  height: 150px;
  /*transform: translate(-50%, -50%);*/
  border-radius: 50%;
  margin-top: 10px;
}

.user__info {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

</style>