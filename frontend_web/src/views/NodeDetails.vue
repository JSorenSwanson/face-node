<template>
  <div class="node-details">
      <v-container>
        <v-row>
          <v-col cols=12>
            <h2>{{id}}</h2>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols=12>
                <ActivityChart :nodeID=nodeID></ActivityChart>
                <h5><u>Masks presence over time @ {{id}}</u></h5>
          </v-col>
        </v-row>
      </v-container>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';


/* Example of instance vars. Ideally this will be retrieved from our store rather than clumsily set here.
   for static demonstration this will do. */ 
@Component  
export default class NodeDetails extends Vue {
   id: string = this.$route.params.id
   @Prop(String) readonly nodeID: string | undefined
}
</script>
