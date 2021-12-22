<template>
  <v-snackbar v-model="snackbar" :timeout="timeout" :color="snackbarColor">
    {{ message }}
    <template v-slot:action="{ attrs }">
      <v-btn
          :color="buttonColor"
          text
          v-bind="attrs"
          @click="snackbar = false"
      >
        Close
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script>
export default {
  name: "SnackBar",

  props: ["display"],

  data: () => ({
    snackbar: false,
    message: "",
    timeout: null,
    snackbarColor: "",
    buttonColor: ""
  }),

  watch: {
    display: function(display) {
      if (display !== null) {
        if (display.type === "info") {
          this.timeout = display.timeout
          this.message = display.message
          this.snackbar = true
          this.snackbarColor = ""
          this.buttonColor = "orange darken-1"
        } else if (display.type === "error") {
          this.timeout = display.timeout
          this.message = display.message
          this.snackbar = true
          this.snackbarColor = "red"
          this.buttonColor = ""
        }
      }
    }
  }
}
</script>
