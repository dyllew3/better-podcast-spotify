import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import App from './App.vue'
import Episode from './components/Episode.vue'
import Home from './components/Home.vue'
import ShowList from './components/ShowList.vue'

Vue.use(VueRouter)

const routes: RouteConfig[] = [
  { path: '/', component: Home },
  { path: '/episode/:id', component: Episode, props: true },
  { path: '/show/:id', component: ShowList, props: true }

]

const router = new VueRouter({
  mode: 'history',
  routes: routes
})
new Vue({
  el: '#app',
  router,
  render: h => h(App),
  template: '<router-view/>'
}).$mount('#app')
