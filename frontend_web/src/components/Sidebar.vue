<template>
  <v-container>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            Face-Nodes
          </v-list-item-title>
          <v-list-item-subtitle>
            v0.0.1
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :to="item.route"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
  </v-container>
</template>

<script lang="ts">
  import Vue from 'vue'
  export default Vue.extend({
    name: 'Sidebar',
    data: () => ({
       items: [
          { title: 'Dashboard', icon: 'mdi-view-dashboard', route:"/" },
          { title: 'Account', icon: 'mdi-account-circle', route:"/account"  },
          { title: 'Settings', icon: 'mdi-cog-box', route:"/node-settings"  },
          { title: 'About', icon: 'mdi-help-box', route:"/about"  },
        ]
    }),
  })
</script>
      
      
      
      
      
    