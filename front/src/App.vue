<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>My journey</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <Search class="mt-3"/>
    </v-main>
  </v-app>
</template>

<script>
import Search from "@/components/Search";

export default {
  name: 'App',
  components: {
    Search
  }
};
</script>

<style>
body {
  background-color: #3d3d3d /* to darken firefox scrollbar */
}
</style>
