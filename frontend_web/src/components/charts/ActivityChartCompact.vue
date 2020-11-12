<template>
<v-container>
    <v-sparkline
      :fill="fill"
      :gradient="gradient"
      :line-width="width"
      :padding="padding"
      :smooth="radius || false"
      :value="value"
      auto-draw
    ></v-sparkline>
</v-container>
</template>

<style scoped>
.v-sheet--offset {
    top: -24px;
    position: relative;
  }
</style>
<script lang="ts">
  import Vue from 'vue'

  // Example of props. Here, our static component takes id, title & height as example prop data fields. 
  export default Vue.extend({
    name: 'ComplianceChartCompact',
    props:{
     
    },
    data: () => ({
      gradient:['purple', 'violet'],
      fill: true,
      padding: 25,
      radius: 6,
      value: [Math.random() * 10, Math.random() * 10, Math.random() * 10, Math.random() * 10, 
      Math.random() * 10, Math.random() * 10, Math.random() * 10, Math.random() * 10, Math.random() * 10, 
      Math.random() * 10, Math.random() * 10, Math.random() * 10, Math.random() * 10, Math.random() * 10, Math.random() * 10],
      width: 2
    })
  })
</script>
