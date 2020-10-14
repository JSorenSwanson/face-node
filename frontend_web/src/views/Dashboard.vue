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
            v-for="n in 9"
            :key="n"
            cols=4
          >
          <!-- Example of nested conditional rendering in Vue. --> 
          <div v-if="n===1 || n===2">
            <div v-if="n===1">
              <titlecard title="UT Arlington Library" editable></titlecard>
            </div>
            <div v-else>
              <titlecard title="Mansfield Tattoo" editable></titlecard>
            </div>
          </div>
          <div v-else>
            <titlecard title="Example Node"></titlecard>
          </div>
          </v-col>
        </v-row>
      </v-container>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import titlecard from '@/components/container/TitleCard.vue';

@Component({
  components: {
    titlecard
  },
})

export default class Dashboard extends Vue {}
</script>
