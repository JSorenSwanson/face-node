<!-- EXAMPLE FROM https://dmtrbrl.github.io/vue-trend-chart/?ref=madewithvuejs.com -->
<template>
  <v-container>
    <line-chart :chart-data="datacollection"></line-chart>
  </v-container>
</template>

<script>
  import LineChart from './LineChart.js'

  export default {
    components: {
      LineChart
    },
    data () {
      return {
        datacollection: null
      }
    },
    mounted () {
      this.fillData()
    },
    methods: {
      fillData () {
        this.datacollection = {
          labels: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],
          datasets: [
            {
              label: 'With Mask',
              backgroundColor: '#f87979',
              data: [0, 13, 24, 27, 29, 34, 50, 66, 70, 80, 90,100, 117]
            }, {
              label: 'Without Mask',
              backgroundColor: '#4BE1FF',
              data: [6, 28, 30, 34, 35, 55, 67, 69, 70, 72, 75, 80, 99]
            }
          ]
        }
      }
    }
  }
</script>

<style>
  .small {
    max-width: 600px;
    margin:  150px auto;
  }
</style>