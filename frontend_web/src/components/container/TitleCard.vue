<template>
<!-- example of DOM style binding -->
  <v-card :height=height v-on:click="redirectDetail">
    <v-col cols=12>
      <v-container >
        <v-row>
          <!-- example of moustache-style binding directive (reactive!) -->
          {{title}}
        </v-row>
      </v-container>
    </v-col>
  </v-card>
</template>

<script lang="ts">
  import Vue from 'vue'

  // Example of props. Here, our static component takes id, title & height as example prop data fields. 
  export default Vue.extend({
    methods:{
        redirectDetail() {
            this.$router.push({ name: 'Node Details', params: { id: this.title } })
        }
    },
    name: 'TitleCard',
    props:{
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
