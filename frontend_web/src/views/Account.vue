<template>
  <div class="account-panel">
   <v-container fill-height fluid>
    <v-row align="center"
      justify="center">
     <v-col cols=6 style="align:center"> 
         <v-card> 
            <v-tabs>
                <v-tab>
                    Profile Information
                </v-tab>
                <v-tab-item>
                    <v-container>
                           <v-col cols=12>
                                    <v-text-field :counter="10" label="Organization Name" required></v-text-field>
                                     <v-textarea
                                        label="Bio"
                                        counter
                                        maxlength="120"
                                        full-width
                                        single-line
                                        >
                                    </v-textarea>
                                </v-col>
                                
                                <v-btn class="mr-4" to='/dashboard'>
                                    Submit
                                </v-btn>
                    </v-container>
                </v-tab-item>
                <v-tab>
                    Account Information8
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
                                        label="New Password"
                                        hint="At least 8 characters"
                                        counter
                                        @click:append="show1 = !show1"
                                    ></v-text-field>
                                    <v-text-field
                                        :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                                        :type="show2 ? 'text' : 'password'"
                                        label="Confirm New Password"
                                        hint="At least 8 characters"
                                        counter
                                        @click:append="show2 = !show2"
                                    ></v-text-field>
                                </v-col>
                               
                                <v-btn class="mr-4" to='/dashboard'>
                                    Submit
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
export default class Account extends Vue {
  show1= false
  show2= false
}
</script>
