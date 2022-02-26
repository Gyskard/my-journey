<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>My journey</v-toolbar-title>
      <v-spacer></v-spacer>
      <AddForm @display="setDisplay"/>
    </v-app-bar>
    <v-main>
      <Search class="mt-4" style="max-width: 75em;"/>
      <List class="d-flex justify-center mt-3" @display="setDisplay"/>
    </v-main>
    <SnackBar :display="display"/>
  </v-app>
</template>

<script>
import Search from "@/components/Search";
import List from "@/components/List";
import AddForm from "@/components/AddForm";
import SnackBar from "@/components/SnackBar";

export default {
  name: 'App',

  components: {
    SnackBar,
    AddForm,
    List,
    Search
  },

  data: () => ({
    display: null,
  }),

  methods: {
    setDisplay: function (display) {
      this.display = display
    }
  }
};
</script>

<style>
body {
  background-color: #3d3d3d /* to darken firefox scrollbar */
}
</style>
