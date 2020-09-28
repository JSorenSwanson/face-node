import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import About from '../views/About.vue'
import Account from '../views/Account.vue'
import NodeSettings from '../views/NodeSettings.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard
  }, 
  {
    path: '/account',
    name: 'Account',
    component: Account
  }, 
  {
    path: '/node-settings',
    name: 'Settings',
    component: NodeSettings
  },
  {
    path: '/about',
    name: 'About',
    component: About
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
