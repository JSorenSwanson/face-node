<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>
      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          {{msg}}
        </h1>

      </v-col>

      <v-col
        class="mb-5"
        cols="12"
      >
        <h2 class="headline font-weight-bold mb-3">
          Important Links
        </h2>

        <v-row justify="center">
          <a
            v-for="(link, i) in importantLinks"
            :key="i"
            :href="link.href"
            class="subheading mx-3"
            target="_blank"
          >
            {{ link.text }}
          </a>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
  import Vue from 'vue'

  export default Vue.extend({
    name: 'HelloWorld',
    props:{
      msg: {
        type: String,
        required: false,
        default: "About our Application"
      }
    },
    data: () => ({
      importantLinks: [
        {
          text: 'Vuetify',
          href: 'https://vuetifyjs.com',
        },
        {
          text: 'GitHub Repository',
          href: 'https://github.com/JSorenSwanson/face-node',
        },
        {
          text: 'Vue',
          href: 'https://vuejs.org/v2/api/',
        },
        {
          text: 'Docker',
          href: 'https://docs.docker.com/get-started/',
        }
      ],
    }),
  })
</script>
