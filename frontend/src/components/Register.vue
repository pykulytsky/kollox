<template>
  <v-container>
    <v-card
        class="main__register__form"
    >
      <h2>Register your account</h2>
      <v-form
          v-model="valid"

      >
        <v-text-field
            v-model="username"
            class="register__field"
            hint="This field uses counter prop"
            label="Username"
        ></v-text-field>
        <v-text-field
            v-model="email"
            class="register__field"
            hint="This field uses counter prop"
            label="Email"

        ></v-text-field>
        <v-text-field
            v-model="password"
            class="register__field"
            hint="This field uses counter prop"
            type="password"
            label="Password"
        ></v-text-field>

        <v-card-actions>
          <v-checkbox
              label="Remember password"
          ></v-checkbox>
          <v-spacer></v-spacer>
          <v-btn
          @click="onSubmit"
          >Register</v-btn>
        </v-card-actions>
        <router-link
            tag="a"
            to="/login"
        >
          <a >Already have an account?</a>
        </router-link>
      </v-form>
    </v-card>
  </v-container>
</template>

<script>
export default {

  data: () => {
    return {
      valid: false,
      username: '',
      email: '',
      password: ''
    }
  },

  methods: {
    onSubmit () {
      // this.$store.dispatch('registerUser', {
      //   username: this.username,
      //   email: this.email,
      //   password: this.password
      // })
      this.$http.post('http://localhost:8000/api/auth/register/',
          {username: this.username,
            email: this.email,
            password: this.password
          })
      .then(response => {
        console.log(response)
        return response.json()
      })
      .then( token => {
        console.log(token)
      })
    }
  }
}
</script>

<style>

.main__register__form {
  padding: 50px 50px;
  position: absolute;
  left: 50%;
  top: 50%;
  display: flex;
  flex-direction: column;
  transform: translate(-50%, -50%);
}

.register__btn {
  margin: 50px 50px 50px 50px;
}

.register__field {
  width: 350px;
}
</style>