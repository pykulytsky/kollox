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
            class="register__field"
            hint="This field uses counter prop"
            label="Username"
        ></v-text-field>
        <v-text-field
            class="register__field"
            hint="This field uses counter prop"
            label="Email"

        ></v-text-field>
        <v-text-field
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
          <v-btn>Register</v-btn>
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