<template>
  <div class="node-details">
      <v-container>
        <v-row>
          <v-col cols=12>
            <h2>{{id}}</h2>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols=6>
            <v-container fluid>
                <h5><u>Masks over time @ {{id}}</u></h5>
                <RandomChart></RandomChart>
            </v-container>
          </v-col>
        </v-row>
      </v-container>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import RandomChart from '@/components/charts/RandomChart.vue'; // @ is an alias to /src

@Component({
  components: {
    RandomChart
  },
})

/* Example of instance vars. Ideally this will be retrieved from our store rather than clumsily set here.
   for static demonstration this will do. */ 
  
export default class NodeDetails extends Vue {
   id: string = this.$route.params.id

}
</script>
