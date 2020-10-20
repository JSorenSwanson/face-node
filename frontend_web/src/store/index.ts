import Vue from 'vue'
import Vuex from 'vuex'
import UserDataService from '@/services/UserDataService'; 
import { isValidJwt } from '@/utils/GlobalUtils'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {},
    jwt: ''
  },
  mutations: {
    setUserData (state, payload) {
      state.user = payload.user
    },
    setJwtToken (state, payload) {
      localStorage.token = payload.jwt.token
      state.jwt = payload.jwt
    }
  },
  actions: {
    login (context, userData) {
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
    }
  },
  getters:{
    isAuthenticated: state=> {
      return isValidJwt(state.jwt)
    },
    getJWT: state=> {
      return isValidJwt(state.jwt) == true ? state.jwt : null
    }
  }
 
})
