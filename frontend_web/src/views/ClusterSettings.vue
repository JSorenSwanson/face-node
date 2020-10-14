<template>
  <div class="node-settings">
    <v-container fill-height fluid>
    <v-row align="center"
      justify="center">
     <v-col cols=6 style="align:center"> 
         <v-card> 
            <v-tabs>
                <v-tab>
                    Cluster Description
                </v-tab>
                <v-tab-item>
                    <v-container>
                           <v-col cols=12>
                                <v-select
                                    :items="clusteritems"
                                    label="Select Cluster Group"
                                    outlined
                                  ></v-select>
                                    <v-text-field :counter="15" label="Cluster Name" required></v-text-field>
                                     <v-textarea
                                        label="Cluster Description"
                                        counter
                                        maxlength="120"
                                        full-width
                                        single-line
                                        >
                                    </v-textarea>
                                </v-col>
                                
                                <v-btn class="mr-4">
                                    Save
                                </v-btn>
                    </v-container>
                </v-tab-item>
                <v-tab>
                   Cluster Settings
                </v-tab>
                <v-tab-item>
                    <v-container>
                            <form>
                                <v-col cols=12>
                                   <v-select
                                    :items="resitems"
                                    label="Cluster Resolution"
                                    outlined
                                  ></v-select>
                                  <v-select
                                    :items="fpsitems"
                                    label="Cluster Framerate"
                                    outlined
                                  ></v-select>
                                   <v-slider
                                    v-model="ex3.val"
                                    :label="ex3.label"
                                    :thumb-color="ex3.color"
                                    thumb-label="always"
                                  ></v-slider>
                                </v-col>
                               
                                <v-btn class="mr-4">
                                    Save
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
export default class ClusterSettings extends Vue {
    clusteritems= ['Libraries','Restaraunts', 'Tattoo Studios', 'Service Industry']
   resitems= ['1080p', '720p', '480p', '360p']
    fpsitems= ['60', '59', '30', '15']
    ex3= { label: 'Confidence Threshold: ', val: 65, color: 'green' }
}
</script>
