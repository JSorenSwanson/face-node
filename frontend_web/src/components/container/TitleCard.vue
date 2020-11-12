<template>
<div>
<!-- example of DOM style binding -->
  <v-card :height=height v-on:click="redirectDetail" class="d-flex flex-column">
      <v-container >
        <v-row>
          <v-col>
          <!-- example of moustache-style binding directive (reactive!) -->
              {{title}}  
          </v-col>
          <div v-if="this.editable">
            <v-row cols=6  style="margin-right:5%">
              <v-btn
                color="primary"
                small
                dark
                @click=redirectEdit
              >
                <v-icon>mdi-cog</v-icon>
              </v-btn>
            </v-row>
          </div>
        </v-row>
         <v-spacer></v-spacer>
        <v-row>
          <ActivityChartCompact></ActivityChartCompact>
        </v-row>
      </v-container>
  </v-card>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  import ActivityChartCompact from '@/components/charts/ActivityChartCompact.vue'; 


  // Example of props. Here, our static component takes id, title & height as example prop data fields. 
  export default Vue.extend({
    components:{
      ActivityChartCompact
    },
    methods:{
      redirectEdit() {
          this.$router.push({ name: 'Settings', params: { id: this.title } })
      },
        redirectDetail() {
            this.$router.push({ name: 'Node Details', params: { id: this.title, nodeID: this.nodeID } })
        }
    },
    name: 'TitleCard',
    props:{
      nodeID:{
        type: String, 
        required: true, 
        default: "Node0"
      },
      editable:{
        type: Boolean,
        required: false, 
        default: false 
      },
      title: {
          type: String, 
          required: false,
          default: "Ex. Node Title"
      },  
      id: {
        type: Number,
        required: false
      }, 
      height: {
        type: Number,
        required: false, 
        default: 250
      }
    },
  })
</script>
