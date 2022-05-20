<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>My journey</v-toolbar-title>
      <v-spacer></v-spacer>
      <Form @display="setDisplay"/>
    </v-app-bar>
    <v-main>
      <Search class="mt-4" style="max-width: 75em;" @searchFormChanged="getNewResults"/>
      <List class="d-flex justify-center mt-3" @display="setDisplay" :searchForm="searchForm"/>
    </v-main>
    <SnackBar :display="display"/>
  </v-app>
</template>

<script>
import Search from "@/components/Search";
import List from "@/components/List";
import Form from "@/components/Form";
import SnackBar from "@/components/SnackBar";

export default {
  name: 'App',

  components: {
    SnackBar,
    Form,
    List,
    Search
  },

  data: () => ({
    display: null,
    searchForm: {}
  }),

  methods: {
    setDisplay: function (display) {
      this.display = display
    },
    getNewResults: function (searchForm) {
      this.searchForm = searchForm
    }
  }
};
</script>

<style>
body {
  background-color: #3d3d3d /* to darken firefox scrollbar */
}

:root {
  color-scheme: dark /* to darken chrome/edge scrollbar */
}
</style>