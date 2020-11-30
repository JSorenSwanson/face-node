<template>
  <div>
   <v-col cols="6">
     <v-slider
        v-model="bucket.val"
        :label="bucket.label"
        :thumb-color="bucket.color"
        thumb-label="always"
        track-color="orange"
        min="15"
        max="300"
      ></v-slider>
   </v-col>
      
    <Plotly :data="seriesData" :layout="layout" :display-mode-bar="false"></Plotly>
  </div>
</template>

<script lang="ts">
import NodeDataService from '../../services/NodeDataService'
import { Component, Prop, Vue } from 'vue-property-decorator';

// Example of a lint rule disable; Our backend expects key likeness, we'll have to
// approach snake_case to camelCase at a later time. 
/* eslint-disable @typescript-eslint/camelcase */

@Component
export default class ActivityChart extends Vue {
    
    // Define component props
    @Prop(Number) readonly nodeID!: number 
    @Prop(String) readonly title!: string 

    // store interval so that we can clear polling when this component isn't mounted 
    pollInterval: any
    
    // Ideally controls would be disjointed from this component
    bucket = { label: 'Bucket Size (MS): ', val: 45, color: 'blue' }
    private maskSeries = {
      x: [],
      y: [],
      name: "Masks",
      type: "scatter"
    };
    private faceSeries = {
      x:[],
      y: [],
      name: "Faces",
      type: "scatter"
    };
    
    private layout = {
        title: "Time-Series data for " + this.title + " (Node" + this.nodeID+ ")",
        xaxis: {
          title: "Time",
          titlefont: {
            family: "Courier New, monospace",
            size: 18,
            color: "#7f7f7f",
            weight: "bold"
          }
        },
        yaxis: {
          title: "Classification Magnitude",
          titlefont: {
            family: "Courier New, monospace",
            size: 18,
            color: "#7f7f7f",
            weight: "bold"
          }
        }
    };
    // TODO: Create type for series data. 
    seriesData: any[] = [this.maskSeries, this.faceSeries]
    
    // Helper function for timestamp conversion 
    toDate(timestamp: number){
      return new Date(timestamp*1000)
    }

    //GETNODEACTIVITY
    // This component's state retrieval should be moved to Vuex posthaste ;)
    async getNode() {
      NodeDataService.nodeActivity(this.nodeID, this.bucket.val)
        .then((response) => {
          // Check your console -- our response is a JSON object. 
          // Chrome allows you to inspect this dumped mem. 
          
          const nodeData = response.data
          console.log(nodeData) 
          this.faceSeries.x = nodeData[0].map(this.toDate)
          this.faceSeries.y = nodeData[1]
          this.maskSeries.x = nodeData[2].map(this.toDate)
          this.maskSeries.y = nodeData[3]

        })
        .catch((e) => {
          console.log(e);
        });
    }
  //*/

    // Component lifecycle hooks
    // Before this component is mounted into application we will invoke getNode and poll getNode 
    mounted() {
       this.getNode()
       this.pollInterval = window.setInterval(() => {
        this.getNode()
  }, 3000)
    }
   // Clear interval to prevent extraneous API calls outside of view. 
    beforeDestroy(){
      clearInterval(this.pollInterval)
    }
}


</script>
