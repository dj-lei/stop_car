import Vue from 'vue'
import App from './App.vue'
import store from './store'
import Vuetify from 'vuetify'
import JsonExcel from 'vue-json-excel'
import 'vuetify/dist/vuetify.min.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

import service from '@/plugins/http'
import urls from '@/plugins/urls'
import common from '@/plugins/common'

Vue.config.productionTip = false
Vue.use(Vuetify)

Vue.prototype.$http = service
Vue.prototype.$urls = urls
Vue.prototype.$common = common

Vue.component('downloadExcel', JsonExcel)

new Vue({
  vuetify: new Vuetify(),
  store,
  render: h => h(App)
}).$mount('#app')


