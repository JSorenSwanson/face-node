<template>
  <div class="dashboard">
    <!-- Checkout Vuetify docs for info on grid (row/col) markup system --> 
    <v-container>
      <v-toolbar
        dense
        floating
      >
      <v-text-field
        hide-details
        prepend-icon="mdi-magnify"
        single-line
      ></v-text-field>

      <v-btn icon>
        <v-icon>mdi-crosshairs-gps</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-toolbar>
        <v-row>
          <v-col
          v-for="node in nodeList" :key="node.id" cols=4>
          <title-card :title='node.name' :editable='isAuthenticated' :id="node.nodeID"></title-card>
          </v-col>
          <!--
          <v-col
            v-for="n in 9"
            :key="n"
            cols=4
          >
         
          <div v-if="n===1 || n===2">
            <div v-if="n===1">
              <titlecard title="Soren's Laptop Webcam" nodeID="Node0" :editable='isAuthenticated'></titlecard>
            </div>
            <div v-else>
              <titlecard title="Mansfield Tattoo" nodeID="Node1" :editable='isAuthenticated'></titlecard>
            </div>
          </div>
          <div v-else>
            <titlecard nodeID="NodeX" title="Example Node"></titlecard>
          </div>
          </v-col>
          <-->
        </v-row>
      </v-container>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import titlecard from '@/components/container/TitleCard.vue';
import TitleCard from '../components/container/TitleCard.vue';

@Component({
  components: {
    TitleCard
  },
  computed:{
    isAuthenticated: function(){
      return this.$store.getters.authenticated;
    }, 
    nodeList: function(){
      return this.$store.getters.getNodes;
    }
  },
  mounted: async function() {
    await this.$store.dispatch('retrieveNodes'); 
  }
})
export default class Dashboard extends Vue {}
</script>
