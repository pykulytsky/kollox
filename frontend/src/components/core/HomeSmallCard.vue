<template>
    <router-link
    to="/about"
    v-slot="{navigate}"
    >
    <div
        @click="navigate"
        class="wrapper">
        <div class="card__image">
            <v-img
                class="main__image"
                width="250px"
                height="70px"
                src="@/assets/cover1.jpg"
            >
            </v-img>
        </div>

        <div class="info__section">
            <p>test</p>
            <small>test small</small>
        </div>
    </div>
    </router-link>
</template>


<script>
export default {
    props: {
        todoList: {
            required: false
        }
    }
}
</script>


<style scoped>

.main__image {
    border-radius: 5px;
}


.wrapper {
    cursor: pointer;
    max-width: 250px;
    max-height: 100px;

    display: flex;
    flex-direction: column;
    justify-content: space-between;


    border-radius: 3px;
    background-color: #1d1d1d;

    margin-top: 15px;
}

.info__section {
    margin: 5px 5px 5px 5px;
    display: flex;
    justify-content: space-between;
}

</style>