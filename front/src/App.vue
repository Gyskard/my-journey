<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>My journey</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <HelloWorld/>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
body {
  background-color: #3d3d3d /* to darken firefox scrollbar */
}
</style>
