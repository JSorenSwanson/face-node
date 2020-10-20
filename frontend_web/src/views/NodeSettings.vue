<template>
 <div id="node-settings">
   <v-container fill-height fluid>
       <v-row align="center"
      justify="center">
         <h2> 
           Edit Node Settings
         </h2>
       </v-row>
    <v-row align="center"
      justify="center">
      <v-col cols=8> 
                <v-card>
                    <v-tabs>
                    <v-tab>
                        Node Description
                    </v-tab>
                    <v-tab-item>
                        <v-container>
                            <v-col cols=12>
                                        <v-text-field :counter="15" label="Node Name" 
                                        v-model="createNodeInput.node_id"
                                        required></v-text-field>
                                        <v-textarea
                                            v-model="createNodeInput.note"
                                            label="Node Description"
                                            counter
                                            maxlength="120"
                                            full-width
                                            single-line
                                            outlined
                                            >
                                        </v-textarea>
                                    </v-col>
                                    <v-btn class="mr-4" color="primary" @click='saveNode'>
                                        Save
                                    </v-btn>
                        </v-container>
                    </v-tab-item>
                    <v-tab>
                    Capture Settings
                    </v-tab>
                    <v-tab-item>
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
                                    
                                    <v-slider
                                        v-model="ex3.val"
                                        :label="ex3.label"
                                        :thumb-color="ex3.color"
                                        thumb-label="always"
                                    ></v-slider>
                                    </v-col>
                                
                                    <v-btn class="mr-4" color="primary" @click='saveNode'>
                                        Save
                                    </v-btn>
                            </form>
                        </v-container>
                    </v-tab-item>
                </v-tabs>
            </v-card>
      </v-col>
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
export default class NodeSettings extends Vue {
    id: string = this.$route.params.id

    // Used for end-user determination of 'loading' / promise fulfillment. 
    syncPromise = false;
    // Message returned from web req result, success/error
    promiseResult = ""; 
    resultBar = false;  

    // Presets
    resitems= ['1080p', '720p', '480p', '360p']
    fpsitems= ['60', '59', '30', '15']
    // Threshold for classification heuristic certainty
    ex3= { label: 'Confidence Threshold: ', val: 50, color: 'blue' }
    saved=false; 

    // Type representing our input model
    // We'll eventually organize these into domains for clarity. 
    // SNEAKY quick/dirty: node_id is our TITLE, shortcut. 
    // Eventually we'll need to generate a GUID
    private createNodeInput = {
        note:"",
        node_id:"",
        ip:"",
        fps:"",
        res:"",
        location:""
        };
    
    saveNode() {
      // Build JSON object we'll be 
      // If we weren't utilizing all fields, we could prune this object into a Data Transfer Object. 
      const data = this.createNodeInput
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
          this.promiseResult = "FAILED to create Node.\n" + e;
          console.log(e);
          this.resultBar = true;
        });
    }
    
    // This component's state retrieval should be moved to Vuex posthaste ;)
    getNode() {
      console.log('hooked')
      // Build JSON object we'll be 
      // If we weren't utilizing all fields, we could prune this object into a Data Transfer Object. 
      this.syncPromise = true;
      const jwtToken = this.$store.getters.getJWT.token;

      NodeDataService.get(this.id, jwtToken)
        .then((response) => {
          // Check your console -- our response is a JSON object. 
          // Chrome allows you to inspect this dumped mem. 
          console.log(response);
          this.syncPromise = false;
          // Set our fields 
          // This should later be part of a class method in domain objects
          // Alternatively, we utilize an object mapper.
          this.createNodeInput.node_id = response.data.node_id
          this.createNodeInput.ip = response.data.ip
          this.createNodeInput.res = response.data.res
          this.createNodeInput.res = response.data.fps
          this.createNodeInput.location = response.data.location
          this.createNodeInput.note = response.data.note

          this.promiseResult = "Successfully loaded Node.";
          this.resultBar = true;
        })
        .catch((e) => {
          this.syncPromise = false;
          this.promiseResult = "FAILED to load Node.\n" + e;
          console.log(e);
          this.resultBar = true;
        });
    }

    // Hook into component mount lifecycle
    mounted() {
        this.getNode()
    }
}


</script>
