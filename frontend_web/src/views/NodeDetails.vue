<template>
  <div class="node-details">
      <v-container>
        {{id}}
        <RandomChart></RandomChart>
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
