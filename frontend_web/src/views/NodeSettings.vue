<template>
  <div class="node-settings">
    <HelloWorld msg="Modify node configuration"/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src

@Component({
  components: {
    HelloWorld,
  },
})
export default class NodeSettings extends Vue {}
</script>
