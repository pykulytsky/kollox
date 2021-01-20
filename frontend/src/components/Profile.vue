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
        <h2
          v-if="user.firstName && user.lastName"
        >{{ user.firstName }}  {{ user.lastName }}</h2>

        <h2
          v-else
        >{{ user.username }}</h2>
      </div>

      <input
          name="avatarUpload"
          type="file"
          ref="avatarUpload"
          id="avatarUpload"
          class="avatar__upload"
          @change="onFileChange"
          accept="image/*"
      >

      <v-btn
          icon
          @click="uploadAvatar"
          class="avatar__upload__btn"
      >
        <v-icon>
          mdi-image-edit
        </v-icon>
      </v-btn>


      <v-btn
        icon
        class="edit__btn"
      >
        <v-icon>
          mdi-lead-pencil
        </v-icon>
      </v-btn>
    </v-img>
    <div class="profile__main">
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Placeat, rem!</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nisi, <repellendus class=""></repellendus></p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima, suscipit!</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque, harum?</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fuga, tempore?</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  title: 'Profile',
  data: () => {
    return {

    }
  },

  beforeCreate() {
    this.$store.dispatch('loadUser')
  },

  updated() {
    console.log(this.user.id)

  },
  computed: {
    loading () {
      return this.$store.getters.loading
    },

    user () {
      return this.$store.getters.user
    }
  },

  methods: {
    uploadAvatar () {
      this.$refs.avatarUpload.click()
    },


    async onFileChange (event) {
      const file = event.target.files[0]

      const reader = new FileReader()
      var imageSrc = null
      var image = null

      reader.onload = e => {
        imageSrc = reader.result
      }
      reader.readAsDataURL(file)
      image = file

      var formData = new FormData();
      formData.append('avatar', image)

      await axios.patch('http://localhost:8000/api/auth/user/' + this.user.id + '/', formData, {
        headers: {Authorization: `Bearer ${JSON.parse(localStorage.getItem('auth'))['token']}`}
      })
      .then(response => {
        this.$notify({
          group: 'main',
          type: 'info',
          title: "You have successfully changed your avatar"
        })
      })
      .catch(error => {
        this.$notify({
          group: 'main',
          type: 'error',
          title: "Some problems occured when changed your avatar"
        })
      })
    }
  },

}
</script>

<style>

.data__item p {
  font-size: 20px;
}

.edit__btn {
  position: absolute;
  bottom: 5%;
  right: 2%;
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

.profile__main {
  margin-top: 25px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.avatar__upload {
  display: none;

  /*position: absolute;*/
  /*z-index: -1;*/
  /*opacity: 0;*/
}

.avatar__upload__btn {
  position: absolute;
  top: 55%;
  left: 53%;
}

</style>