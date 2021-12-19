<template>
  <v-dialog v-model="dialog" persistent max-width="900px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="secondary" v-bind="attrs" v-on="on">Add an event</v-btn>
    </template>
    <v-card>
      <v-card-title>
        <span class="text-h5">Add an event</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-text-field v-model="eventName" label="Name" required></v-text-field>
          <v-text-field v-model="eventDescription" label="Description"></v-text-field>
          <v-menu
              v-model="menu"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                  v-model="dateFormat"
                  label="Date"
                  readonly
                  v-bind="attrs"
                  v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
                v-model="date"
                @input="menu = false"
                no-title color="orange darken-1"
            ></v-date-picker>
          </v-menu>
          <v-row>
            <v-col cols="10">
              <v-select
                  v-model="location"
                  :items="locations"
                  label="Location"
                  required
              ></v-select>
            </v-col>
            <v-col  cols="4">
              <v-btn color="primary">Add a location</v-btn>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" text @click="dialog = false">
          Close
        </v-btn>
        <v-btn color="primary" text @click="dialog = false">
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'AddForm',

  data: () => ({
    dialog: false,
    eventName: "",
    eventDescription: "",
    date: "",
    menu: false,
    locations: ['Location1', 'Location2'],
    location: null,
  }),

  computed: {
    dateFormat: function () {
      return this.date !== "" ?  this.$dateFormat(this.date) : ""
    }
  }
}
</script>
