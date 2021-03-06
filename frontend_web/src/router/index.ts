import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import LoginLanding from '../views/LoginLanding.vue'
import About from '../views/About.vue'
import Account from '../views/Account.vue'
import NodeSettings from '../views/NodeSettings.vue'
import NodeDetails from '../views/NodeDetails.vue'
import ClusterSettings from '../views/ClusterSettings.vue'
import CreateNode from '../views/CreateNode.vue'
import store from '@/store'

Vue.use(VueRouter)

// Define application routes and related rendered components. 
const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Login',
    component: LoginLanding
  }, 
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  }, 
  {
    path: '/account',
    name: 'Account',
    component: Account,
    beforeEnter (to, from, next) {
      if (!store.getters.authenticated) {
        next('/')
      } else {
        next()
      }
    }
  }, 
  {
    path: '/node-settings/:id',
    name: 'Settings',
    component: NodeSettings,
    beforeEnter (to, from, next) {
      if (!store.getters.authenticated) {
        next('/')
      } else {
        next()
      }
    }
  },
  {
    path: '/create-node',
    name: 'Create Node',
    component: CreateNode,
    beforeEnter (to, from, next) {
      if (!store.getters.authenticated) {
        next('/')
      } else {
        next()
      }
    }
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/node_details/:id',
    name: 'Node Details',
    component: NodeDetails
  },
  {
    path: '/cluster-settings',
    name: 'Cluster Settings',
    component: ClusterSettings,
    beforeEnter (to, from, next) {
      if (!store.getters.authenticated) {
        next('/')
      } else {
        next()
      }
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
