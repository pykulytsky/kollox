<template>
  <v-container>
    <v-card
    class="main__login__form"
    >
      <h2>Login to your account</h2>
      <v-form
      v-model="valid"

      >
        <v-text-field
            class="login__field"
            hint="This field uses counter prop"
            label="Username"
        ></v-text-field>
        <v-text-field

            hint="This field uses counter prop"
            label="Email"

        ></v-text-field>
        <v-text-field

            hint="This field uses counter prop"
            type="password"
            label="Password"
        ></v-text-field>

        <v-card-actions>
          <v-checkbox
          label="Remember password"
          ></v-checkbox>
          <v-spacer></v-spacer>
          <v-btn>Login</v-btn>
        </v-card-actions>
        <router-link
            tag="a"
            to="/register"
        >
          <a >Dont have an account?</a>
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
  }
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
</style>