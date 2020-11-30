import Vue from 'vue'
import Vuex from 'vuex'
import UserDataService from '@/services/UserDataService'; 
import NodeDataService from '@/services/NodeDataService';

import { isValidJwt } from '@/utils/GlobalUtils'

Vue.use(Vuex)
Vue.config.devtools = true

export default new Vuex.Store({
  state: {
    user: {},
    nodes: {},
    jwt: ''
  },
  mutations: {
    setUserData (state, payload) {
      state.user = {'email':payload.userData.email}
    },
    setJwtToken (state, payload) {
      localStorage.token = payload.jwt.token
      state.jwt = payload.jwt
    }, 
    setNodeEndpoints(state, payload){
      console.log('SET:\n' + payload)
      state.nodes = payload
    }
  },
  actions: {
    login (context, userData) {
      console.log(userData);
      context.commit('setUserData', { userData })
      return UserDataService.login(userData)
        .then(response => {
          context.commit('setJwtToken', { jwt: response.data });
          return {
            message:'Logged in successfully.', 
            authenticated:true
          }
        })
        .catch(error => {
          // Eventually this return should be strictly typed.
          return {
            message:error,
            authenticated:false
          };
        })
    },
    register (context, userData) {
      context.commit('setUserData', { userData })
      return UserDataService.create(userData)
        .then(response => { 
          context.dispatch('login', userData)
          console.log(response);
          // TODO: We should implement an email confirmation system.
          return {
            message:'Registered successfully, please login with your credentials.', 
            authenticated:true
          }
        })
        .catch(error => {
          return {
            message:error,
            authenticated:false
          };
        })
    }, 
    async retrieveNodes (context){
      const nodeData = await NodeDataService.getAll();
      context.commit('setNodeEndpoints', nodeData.data);
    }
  },
  getters:{
    authenticated: (state) => {
      // Again, jwt should be statically typed. 
      return isValidJwt(state.jwt)
    },
    getJWT: (state) => {
      return isValidJwt(state.jwt) == true ? state.jwt : null
    }, 
    getNodes: (state) => 
    {
      return state.nodes;
    }
  }
 
})
