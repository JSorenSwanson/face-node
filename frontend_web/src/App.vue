<template>
  <v-app id="node-web">
     <v-navigation-drawer
      v-model="drawer"
      app
    >
       <sidebar></sidebar>
    </v-navigation-drawer>
    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer">
      </v-app-bar-nav-icon>
      <v-toolbar-title>face-nodes frontend</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import sidebar from '@/components/Sidebar.vue';

export default Vue.extend({
  name: 'App',
  components: {
    sidebar
  },
  data: () => ({
   drawer:null
  }),
});
</script>
