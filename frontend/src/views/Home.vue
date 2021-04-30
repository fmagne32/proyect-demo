<template>
  <v-container>
    <h5>Primero</h5>
    <v-row class="text-center"> <hello-world /></v-row>
  </v-container>
</template>

<script>
import HelloWorld from "../components/HelloWorld";

export default {
  name: "Home",

  components: {
    HelloWorld,
  },
};
</script>
