<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>My journey</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <Search class="mt-4" style="max-width: 75em;"/>
      <List class="d-flex justify-center mt-3"/>
    </v-main>
  </v-app>
</template>

<script>
import Search from "@/components/Search";
import List from "@/components/List";

export default {
  name: 'App',
  components: {
    List,
    Search
  }
};
</script>

<style>
body {
  background-color: #3d3d3d /* to darken firefox scrollbar */
}
</style>
