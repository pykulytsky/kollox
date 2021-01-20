<template>
<div class="container">
  <div
      v-if="isSearchParamsGivenOver"
      class="wrapper">

    <div class="search__info search_item">
      <h1
      class="search__header"
      >Search result for "{{ searchParams }}" : </h1>
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid, dolor.
    </div>

    <hr>

    <div class="search__lists search_item">
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium, eaque veniam! Architecto magni molestias tenetur.
    </div>

    <hr>

    <div class="search__todos search_item">
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab at ea, eius eligendi, fugiat hic magnam maxime molestiae nemo pariatur praesentium quae quia rerum suscipit.
    </div>

  </div>

  <div
      v-else
      class="wrapper__error">
    <h1>Enter a search query</h1>
  </div>
</div>
</template>

<script>

export default {
  title () {
    return 'Search: ' + this.searchParams
  },
  data: () => {
    return {
      searchParams: '',
      isSearchParamsGivenOver: false
    }
  },

  computed: {

  },

  methods: {

  },

  mounted() {
    if (this.$route.query['s']) {
      this.searchParams = this.$route.query['s']
      this.isSearchParamsGivenOver = true
    }
    else {
      this.isSearchParamsGivenOver = false
    }
  }

}

</script>

<style scoped>

.search__header {
  margin: 30px;
  margin-left: 10px;
}

.wrapper {
  display: flex;
  flex-direction: column;

}

.search_item {
  margin: 15px;
}

.wrapper__error {
  display: flex;
  justify-content: center;
  margin-top: 50px;
}
</style>