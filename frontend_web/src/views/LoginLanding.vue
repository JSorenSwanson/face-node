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
                                    <v-text-field :counter="10" label="Username" required></v-text-field>
                                    <v-text-field
                                        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                                        :type="show1 ? 'text' : 'password'"
                                        label="Password"
                                        hint="Hope it's a good one."
                                        counter
                                        @click:append="show0 = !show0"
                                    ></v-text-field>
                                </v-col>
                                
                                <v-btn class="mr-4" to='/dashboard'>
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
                                    <v-text-field :counter="10" label="Username" required></v-text-field>
                                    <v-text-field label="E-mail" required></v-text-field>
                                    <!-- Example of some more detailed input configuration --> 
                                    <v-text-field
                                        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                                        :type="show1 ? 'text' : 'password'"
                                        label="Password"
                                        hint="At least 8 characters"
                                        counter
                                        @click:append="show1 = !show1"
                                    ></v-text-field>
                                    <v-text-field
                                        :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                                        :type="show2 ? 'text' : 'password'"
                                        label="Confirm Password"
                                        hint="At least 8 characters"
                                        counter
                                        @click:append="show2 = !show2"
                                    ></v-text-field>
                                </v-col>
                               
                                <v-btn class="mr-4" to='/dashboard'>
                                    Register
                                </v-btn>
                         </form>
                    </v-container>
                </v-tab-item>
            </v-tabs>
        </v-card>
     </v-col>
  </v-row>
    </v-container>
  </div>
</template>

<script lang="ts">
  import { Component, Vue } from 'vue-property-decorator';
 

 
@Component({
  components: {
  
  },
})

// This is a terrible way to declare our data-binding variables. How can we improve this?
export default class Dashboard extends Vue {
    show0= false
    show1= false
    show2= false
}
</script>
