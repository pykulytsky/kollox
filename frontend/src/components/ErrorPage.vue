<template>
<v-container>
  <div class="main__section">
    <h1>404!</h1>
    <p>Your page didnt found:( Try again!</p>
  </div>
</v-container>
</template>

<script>
export default {
  data: () => {
    return {

    }
  }
}
</script>

<style>
.main__section {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.main__section h1 {
  font-size: 115px;
}
</style>