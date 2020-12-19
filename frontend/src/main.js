import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import VueResource from "vue-resource";
import VueSelectImage from 'vue-select-image'
import titleMixin from "@/mixins/titleMixin";

require('vue-select-image/dist/vue-select-image.css')

Vue.config.productionTip = false
Vue.use(VueResource)
Vue.use(VueSelectImage)
Vue.mixin(titleMixin)

new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount('#app')
