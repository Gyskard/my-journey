<template>
  <div>
    <!-- used @click.stop instead of v-slot to disable auto-focus on button after closing dialog -->
    <v-btn color="secondary" @click.stop="event.dialog = true">Add an event</v-btn>
    <v-dialog v-model="event.dialog" max-width="900px">
      <v-card>
        <v-card-title>
          <span class="text-h5">Add an event</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-container class="mt-4 mb-5">
              <v-btn small color="secondary" dark @click="location.dialog = !location.dialog">
                Add a location
              </v-btn>
              <v-btn class="ml-4" small color="secondary" dark>
                Add a person
              </v-btn>
            </v-container>
            <v-text-field v-model="event.form.name" label="Name" required></v-text-field>
            <v-text-field v-model="event.form.description" label="Description"></v-text-field>
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
                  v-model="event.form.date"
                  @input="event.dateMenu = false"
                  no-title color="orange darken-1"
              ></v-date-picker>
            </v-menu>
            <v-select
                v-model="event.form.selectedLocations"
                :items="event.form.locations"
                label="Location"
                required
            ></v-select>
            <v-combobox
                v-model="event.form.selectedParticipants"
                :items="event.form.participants"
                label="Participant"
                multiple
                chips
            ></v-combobox>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="event.dialog = false">
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="location.dialog" max-width="500px">
      <v-card>
        <v-card-title>
          Add a location
        </v-card-title>
        <v-card-text>
          <v-form ref="locationForm" v-model="location.valid">
            <v-text-field
                v-model="location.form.name"
                label="Name"
                :rules="[rules.required(), rules.maxSize(50)]"
            ></v-text-field>
            <v-text-field
                v-model="location.form.houseNumberStreet"
                label="House number street"
                :rules="[rules.maxSize(7), rules.onlyNumbers()]"
            ></v-text-field>
            <v-text-field
                v-model="location.form.streetName"
                label="Street name"
                :rules="[rules.maxSize(25)]"
            ></v-text-field>
            <v-text-field
                v-model="location.form.postalCode"
                label="Postal code"
                :rules="[rules.maxSize(7), rules.onlyNumbers()]"
            ></v-text-field>
            <v-text-field
                v-model="location.form.city"
                label="City"
                :rules="[rules.maxSize(75)]"
            ></v-text-field>
            <v-text-field
                v-model="location.form.country"
                label="Country"
                :rules="[rules.maxSize(50)]"></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="saveLocation">
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: 'AddForm',

  data: () => ({
    menu: false,
    event: {
      dialog: false,
      dateMenu: false,
      form: {
        name: "",
        description: "",
        date: "",
        locations: ['Location1', 'Location2'],
        selectedLocations: null,
        participants: ['First_name1 LAST_NAME1', 'First_name2 LAST_NAME2'],
        selectedParticipants: null,
      }
    },
    location: {
      dialog: null,
      valid: true,
      form: {
        name: "",
        houseNumberStreet: "",
        streetName: "",
        postalCode: "",
        city: "",
        country: "",
      },
      rules: {
        houseNumberStreet: [
          v => /^[0-9]*$/.test(v || '') || `Only numbers are allowed`,
          v => (v || '').length <= 7 || `A maximum of 7 characters is allowed`,
        ],
        streetName: [
          v => (v || '').length <= 25 || `A maximum of 25 characters is allowed`,
        ],
        postalCode: [
          v => /^[0-9]*$/.test(v || '') || `Only numbers are allowed`,
          v => (v || '').length <= 7 || `A maximum of 7 characters is allowed`,
        ],
        city: [
          v => (v || '').length <= 75 || `A maximum of 75 characters is allowed`,
        ],
        country: [
          v => (v || '').length <= 50 || `A maximum of 50 characters is allowed`,
        ],
      },
    },
    rules: {
      required() {
        return v => !!v || 'Name is required'
      },
      maxSize(size) {
        return v => (v || '').length <= size || `A maximum of ${size} characters is allowed`
      },
      onlyNumbers() {
        return v => /^[0-9]*$/.test(v || '') || `Only numbers are allowed`
      }
    }
  }),

  computed: {
    dateFormat: function () {
      return this.event.form.date !== "" ?  this.$dateFormat(this.event.form.date) : ""
    }
  },

  methods: {
    saveLocation: function () {
      this.$refs.locationForm.validate()
      console.log(this.location.valid)
    }
  }
}
</script>
