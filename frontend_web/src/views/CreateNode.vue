<template>
  <div class="node-settings">
    <v-container fill-height fluid>
       <v-row align="center"
      justify="center">
         <h2> 
           Generate Node
         </h2>
       </v-row>
    <v-row align="center"
      justify="center">
     <v-col cols=8> 
         <v-card> 
           <v-stepper v-model="e13" vertical>
              <v-stepper-step
                step="1"
              >
               Node Description
              </v-stepper-step>

              <v-stepper-content step="1">
                 <v-text-field 
                 v-model="createNodeInput.name"
                  label="Node Name" required>
                  </v-text-field>
                <v-textarea
                    v-model="createNodeInput.description"
                    label="Node Description"
                    counter
                    maxlength="500"
                    full-width
                    single-line
                    outlined
                    >
                </v-textarea>
                <v-btn
                  color="primary"
                  @click="e13 = 2"
                >
                  Continue
                </v-btn>
              </v-stepper-content>

              <v-stepper-step
                step="2"
              >
                Node Settings
              </v-stepper-step>

              <v-stepper-content step="2">
               <v-container>
                                <form>
                                    <v-col cols=12>
                                    <v-row>
                                       <v-col cols=6>
                                          <v-select
                                          v-model="createNodeInput.res"
                                          :items="resitems"
                                          label="Resolution"
                                          outlined
                                      ></v-select>
                                      </v-col>
                                      <v-col cols=6>
                                        <v-select
                                        v-model="createNodeInput.fps"
                                            :items="fpsitems"
                                            label="Framerate"
                                            outlined
                                        ></v-select>
                                      </v-col>
                                    </v-row>
                                    <v-row>
                                      <v-col cols=12>
                                         <v-text-field 
                                           v-model="createNodeInput.ip"
                                           label="Network Location" required>
                                          </v-text-field>
                                      </v-col>
                                    </v-row>
                                    <v-slider
                                        v-model="ex3.val"
                                        :label="ex3.label"
                                        :thumb-color="ex3.color"
                                        thumb-label="always"
                                    ></v-slider>
                                    </v-col>
                            </form>
                        </v-container>
                <v-btn
                  color="primary"
                  @click="e13 = 3"
                >
                  Continue
                </v-btn>
                 <v-btn text
                @click="e13 = 1">
                  Back
                </v-btn>
              </v-stepper-content>

              <v-stepper-step
                :rules="[() => true]"
                step="3"
              >
                Social
              
              </v-stepper-step>

              <v-stepper-content step="3">
                <v-card
                  color="grey lighten-1"
                  class="mb-12"
                  height="200px"
                ></v-card>
                <!-- Good example of promise fulfillment + reactivity -->
                 <v-btn
                  class="ma-2"
                  :loading="syncPromise"
                  :disabled="syncPromise"
                  color="primary"
                  @click="saveNode"
                >
                  Submit
                  <template v-slot:loader>
                    <span class="custom-loader">
                      <v-icon light>mdi-cached</v-icon>
                    </span>
                  </template>
                </v-btn>
                 <v-btn text
                @click="e13 = 2">
                  Back
                </v-btn>
              </v-stepper-content>
            </v-stepper>
          </v-card>
      </v-col>
    </v-row>
    <v-row>
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
    </v-row>
  </v-container>
  </div>
</template>
           

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import NodeDataService from '../services/NodeDataService';

// Example of a lint rule disable; Our backend expects key likeness, we'll have to
// approach snake_case to camelCase at a later time. 
/* eslint-disable @typescript-eslint/camelcase */

@Component
export default class CreateNode extends Vue {

    // Used for end-user determination of 'loading' / promise fulfillment. 
    syncPromise = false;
    // Message returned from web req result, success/error
    promiseResult = ""; 
    resultBar = false; 

    // Tab n
    e13 = 1
    // Presets
    resitems= ['1080p', '720p', '480p', '360p']
    fpsitems= ['60', '59', '30', '15']
    // Threshold for classification heuristic certainty
    ex3= { label: 'Confidence Threshold: ', val: 50, color: 'blue' }
    saved=false; 

  private createNodeInput = {
       
       description:"",
       name:"",
       location:"",
       ip:"localhost",
       fps:"60",
       res:"1080p", 
       confidence:0
    };
    
    saveNode() {
      // Build JSON object we'll be 
      // If we weren't utilizing all fields, we could prune this object into a Data Transfer Object. 
      const data = this.createNodeInput;
      data.confidence = this.ex3.val;
      this.syncPromise = true;
      const jwtToken = this.$store.getters.getJWT.token;

      NodeDataService.create(data, jwtToken)
        .then((response) => {
          this.syncPromise = false;
          this.promiseResult = "Successfully created Node.";
          this.resultBar = true;
          
        })
        .catch((e) => {
          this.syncPromise = false;
          this.promiseResult = "FAILED: " + e;
          console.log(e.message);
          this.resultBar = true;
        });
    }
}
</script>
