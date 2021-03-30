import Vue from 'vue'
import App from './App.vue'
import store from './store'
import Vuetify from 'vuetify'
import VueRouter from 'vue-router'
import JsonExcel from 'vue-json-excel'
import 'vuetify/dist/vuetify.min.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

import Page from './components/common/page'
import Login from './components/common/login'

import service from '@/plugins/http'
import urls from '@/plugins/urls'
import common from '@/plugins/common'

Vue.config.productionTip = false
Vue.use(Vuetify)

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}
Vue.use(VueRouter)

Vue.prototype.$http = service
Vue.prototype.$urls = urls
Vue.prototype.$common = common

const routes = [
  { path: '/', component: Login },
  { path: '/vip', component: Page }
]

const router = new VueRouter({
  routes
})


Vue.component('downloadExcel', JsonExcel)

new Vue({
  vuetify: new Vuetify(),
  store,
  router,
  render: h => h(App)
}).$mount('#app')


