<template>
  <div>
    <v-img
        src="https://unsplash.com/photos/Qrjx2nTBHVo"
        gradient="to top right, rgba(100,115,201,.7), rgba(25,32,72,.7)"
    ></v-img>

  <v-app-bar-nav-icon></v-app-bar-nav-icon>

  <v-toolbar-title>Title</v-toolbar-title>

  <v-spacer></v-spacer>

  <v-btn icon>
    <v-icon>mdi-magnify</v-icon>
  </v-btn>

  <v-btn icon>
    <v-icon>mdi-heart</v-icon>
  </v-btn>

  <v-btn icon>
    <v-icon>mdi-dots-vertical</v-icon>
  </v-btn>

    <v-tabs align-with-title>
      <v-tab>Tab 1</v-tab>
      <v-tab>Tab 2</v-tab>
      <v-tab>Tab 3</v-tab>
    </v-tabs>
  </div>
</template>

<script>

export default {

}
</script>

<style>

</style>