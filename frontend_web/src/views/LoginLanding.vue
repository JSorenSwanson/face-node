<!-- This implementation will not satisfy initial iteration, but will serve a static example for feature demonstration. --> 
<template>
  <div class="login-landing">
    <v-container fill-height fluid>
    <v-row align="center"
      justify="center">
     <v-col cols=6 style="align:center"> 
         <v-card> 
            <v-tabs>
                <v-tab>
                    Login
                </v-tab>
                <v-tab-item>
                    <v-container>
                           <v-col cols=12>
                                    <v-text-field 
                                        outlined 
                                        v-model="validateUserInput.email"
                                        label="Email"
                                        required>
                                      </v-text-field>
                                    <v-text-field
                                        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                                        :type="show1 ? 'text' : 'password'"
                                        label="Password"
                                        hint="case sensitive"
                                        outlined
                                        v-model="validateUserInput.password"
                                        @click:append="show0 = !show0"
                                    ></v-text-field>
                                </v-col>
                                
                                <v-btn class="mr-4" @click='loginUser'>
                                    Login
                                </v-btn>
                    </v-container>
                </v-tab-item>
                <v-tab>
                    Register
                </v-tab>
                <v-tab-item>
                    <v-container>
                            <form>
                                <v-col cols=12>
                                    <v-text-field
                                      outlined  
                                      label="Username"
                                      required 
                                      v-model="createUserInput.username">
                                    </v-text-field>
                                    <v-text-field 
                                      outlined  
                                      label="E-Mail" 
                                      hint="Please use a valid email address."
                                      v-model="createUserInput.email" 
                                      required>
                                    </v-text-field>
                                    <!-- Example of some more detailed input configuration --> 
                                    <v-text-field
                                        outlined
                                        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                                        :type="show1 ? 'text' : 'password'"
                                        label="Password"
                                        hint="At least 8 characters"
                                        counter
                                        @click:append="show1 = !show1"
                                    ></v-text-field>
                                    <v-text-field
                                        outlined
                                        :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                                        :type="show2 ? 'text' : 'password'"
                                        label="Confirm Password"
                                        hint="At least 8 characters"
                                        v-model="createUserInput.password"
                                        counter
                                        @click:append="show2 = !show2"
                                    ></v-text-field>
                                </v-col>
                               
                                <v-btn class="mr-4" @click='registerUser'>
                                    Register
                                </v-btn>
                         </form>
                    </v-container>
                </v-tab-item>
            </v-tabs>
        </v-card>
     </v-col>
  </v-row>
    <v-snackbar
        v-model="resultBar"
        :timeout="2000"
      >
        {{ promiseResult }}

        <template v-slot:action="{ attrs }">
          <v-btn
            color="primary"
            text
            v-bind="attrs"
            @click="snackbar = false"
          >
            Close
          </v-btn>
        </template>
      </v-snackbar>
    </v-container>
  </div>
</template>

<script lang="ts">
  import { Component, Vue } from 'vue-property-decorator';
  import UserDataService from '../services/UserDataService';  

 
@Component({
  components: {
  
  },
})

// This is a terrible way to declare our data-binding variables. How can we improve this?
export default class Dashboard extends Vue {
    // UI bools (password hide/show)
    show0= false
    show1= false
    show2= false
    
    // Used for end-user determination of 'loading' / promise fulfillment. 
    syncPromise = false;
    // Message returned from web req result, success/error
    promiseResult = ""; 
    resultBar = false;  

    private createUserInput = {
        username:"",
        email:"",
        password:""
    }
    private validateUserInput = {
      email:"", 
      password:""
    }

    loginUser(){
      const data = this.validateUserInput
      this.syncPromise = true;
       
     this.$store.dispatch('login', data)
        .then((response) => {
          console.log(response);
          this.syncPromise = false;
          this.promiseResult = response.message;
          this.resultBar = true;
          const authenticated = response.authenticated;
          if(authenticated)
            this.$router.push('/dashboard')
        })
        .catch((e) => {
          this.syncPromise = false;
          this.promiseResult = "Response timed out: " + e;
          this.resultBar = true;
        });
    }
    registerUser(){
      const data = this.createUserInput
      this.syncPromise = true;
       
      UserDataService.create(data)
        .then((response) => {
          this.syncPromise = false;
          this.promiseResult = "Successfully registered!";
          this.resultBar = true;
          const authenticated = response.authenticated;
          if(authenticated)
            this.$router.push('/dashboard')
        })
        .catch((e) => {
          this.syncPromise = false;
          this.promiseResult = "Response timed out: " + e;
          this.resultBar = true;
        });
    }
}
</script>
