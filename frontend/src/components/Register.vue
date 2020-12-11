<template>
  <v-container>
    <v-card
        elevation="16"
        class="main__register__form"
    >
      <h2>Register your account</h2>
      <v-form
          v-model="valid"
          ref="form"
          validation

      >
        <v-text-field
            v-model="username"
            class="register__field"
            hint="This field uses counter prop"
            label="Username"
            :rules="rules"
            required
        ></v-text-field>
        <v-text-field
            v-model="email"
            class="register__field"
            hint="This field uses counter prop"
            label="Email"
            :rules="emailRules"

            required
        ></v-text-field>
        <v-text-field
            v-model="password"
            class="register__field"
            hint="This field uses counter prop"
            type="password"
            label="Password"
            :rules="passwordRules"
            required
        ></v-text-field>

        <v-card-actions>
          <v-checkbox
              label="Remember password"
          ></v-checkbox>
          <v-spacer></v-spacer>
          <v-btn
              :loading="loading"
              :disabled="!valid || loading"
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
const emailRegex = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/
export default {

  data: () => {
    return {
      valid: false,
      username: '',
      email: '',
      password: '',
      maxLetters: 32,
      allowSpaces: false,

      emailRules: [
        v => !!v || 'E-mail is required',
        v => emailRegex.test(v) || 'E-mail must be valid'
      ],
      passwordRules: [
        v => !!v || 'Password is required',
        v => (v && v.length >= 8) || 'Password must be equal or more than 8 characters'
      ]
    }
  },

  methods: {
    onSubmit() {

      if (this.$refs.form.validate() ) {
        // this.$store.dispatch('setLoading', true)

        const user = {
          username: this.username,
          email: this.email,
          password: this.password
        }

        this.$store.dispatch('registerUser', user)
            .then(() => {
              if (!this.$store.getters.error) {
                this.$router.push('/login')
              }
            })
            .catch(error => {
              console.log("error on submit")
            })

        // this.$store.dispatch('setError', null)
        // this.$store.dispatch('clearError')
        // this.$http.post('http://localhost:8000/api/auth/register/', user)
        //     .then(response => {
        //       if (response.status == 200) {
        //         console.log('success')
        //         return response.json()
        //       } else {
        //         console.log(response.statusText)
        //       }
        //     })
        //     .then(token => {
        //       this.$store.dispatch('registerUser', token)
        //       console.log("Registered user: ", this.$store.getters.user)
        //       this.$router.push('/todo-list/1')
        //
        //     })
        // this.$store.dispatch('setLoading', false)
      }
      // this.$store.dispatch('registerUser', user)
      // .then(() => {
      //   this.$router.push('/')
      // })
      //     .catch(error => {
      //       console.log(error)
      //     })
      //
      // }
      // this.$store.dispatch('registerUser', {
      //   username: this.username,
      //   email: this.email,
      //   password: this.password
      // })
      // this.$http.post('http://localhost:8000/api/auth/register/',
      //     {username: this.username,
      //       email: this.email,
      //       password: this.password
      //     })
      // .then(response => {
      //   console.log(response)
      //   return response.json()
      // })
      // .then( token => {
      //   console.log(token)
      // })
    }
  },
  computed: {
    loading() {
      return this.$store.getters.loading
    },

    rules() {
      const rules = []

      if (this.maxLetters) {
        const rule =
            v => (v || '').length <= this.maxLetters ||
                `A maximum of ${this.max} characters is allowed`

        rules.push(rule)
      }

      if (!this.allowSpaces) {
        const rule =
            v => (v || '').indexOf(' ') < 0 ||
                'No spaces are allowed'

        rules.push(rule)
      }
      return rules
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