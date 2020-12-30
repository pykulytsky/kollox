<template>
  <v-container>
    <v-card
        elevation="16"
    class="main__login__form"
    >
      <h2>Login to your account</h2>
      <v-form
      v-model="valid"
      ref="form"
      validation
      >
        <v-text-field
            prepend-icon="mdi-account"
            v-model="username"
            class="login__field field"
            hint="This field uses counter prop"
            label="Username"

            :rules="rules"
        ></v-text-field>
        <v-text-field
            class="field"
            prepend-icon="mdi-email"
            v-model="email"
            type="email"
            hint="This field uses counter prop"
            label="Email"
            :rules="emailRules"
        ></v-text-field>
        <v-text-field
            class="field"
            prepend-icon="mdi-key"
            v-model="password"
            hint="This field uses counter prop"
            type="password"
            label="Password"
            :rules="passwordRules"
        ></v-text-field>

        <v-card-actions>
          <v-checkbox
          label="Remember password"
          ></v-checkbox>
          <v-spacer></v-spacer>
          <v-btn
            :disabled="!valid || loading"
            :loading="loading"
            @click="onSubmit"
          >Login</v-btn>
        </v-card-actions>
        <router-link
            tag="a"
            to="/register"
        >
          <a >Dont have an account?</a>
        </router-link>
      </v-form>
      <g-signin-button
          :params="googleSignInParams"
          @success="onSignInSuccess"
          @error="onSignInError">
        <v-btn
            class="google__btn"
            >
          <v-icon
            left
          >
            mdi-google
          </v-icon>
          Login with Google
        </v-btn>
      </g-signin-button>
    </v-card>

  </v-container>
</template>

<script>
import GSignInButton from 'vue-google-signin-button'

const emailRegex = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/
export default {
  components: {
    GSignInButton
  },

  title: 'Login',

  // TODO Fix double loading on login and registration
  data: () => {
    return {
      googleSignInParams: {
        client_id: '923957093905-14peq0qa7l5lfvi17col6jmigbqtepbm.apps.googleusercontent.com'
      },

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
        v => (v && v.length >= 6) || 'Password must be equal or more than 6 characters'
      ]
    }
  },

  methods: {
    onSignInSuccess (googleUser) {
      // `googleUser` is the GoogleUser object that represents the just-signed-in user.
      // See https://developers.google.com/identity/sign-in/web/reference#users
      const profile = googleUser.getBasicProfile() // etc etc
      console.log("profile: ", profile)
      console.log('user: ', googleUser)
      const accessToken = googleUser.xc.access_token
      console.log("token: ", googleUser.Zi.access_token)


    },
    onSignInError (error) {
      // `error` contains any error occurred.
      console.log('OH NOES', error)
    },

    onSubmit() {

      if (this.$refs.form.validate() ) {
        const user = {
          username: this.username,
          email: this.email,
          password: this.password
        }

        this.$store.dispatch('loginUser', user)
            .then(() => {
              if (!this.$store.getters.error) {
                this.$store.dispatch('loadAllTodoLists')
                this.$router.push('/all-todo-lists?msg=verify_email')
              }
            })
      }

    }
  },

  computed: {
    loading () {
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
  },
  beforeMount() {
    this.$store.dispatch('clearUser')
    this.$store.dispatch('clearAuth')
  },
}
</script>

<style>

.main__login__form {
  padding: 50px 50px;
  position: absolute;
  left: 50%;
  top: 50%;
  display: flex;
  flex-direction: column;
  transform: translate(-50%, -50%);
}

.login__btn {
  margin: 50px 50px 50px 50px;
}

.login__field {
  width: 350px;
}

.google__btn {
  width: 100%;
  margin-top: 10px;
}
</style>