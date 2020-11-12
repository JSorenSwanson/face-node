import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import {Plotly} from 'vue-plotly'
import ActivityChart from '@/components/charts/ActivityChart.vue'; // @ is an alias to /src

Vue.config.productionTip = false
Vue.component('Plotly', Plotly)
Vue.component('ActivityChart', ActivityChart)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
