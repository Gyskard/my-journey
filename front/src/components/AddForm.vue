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
              <v-btn class="ml-4" small color="secondary" dark  @click="person.dialog = !person.dialog">
                Add a person
              </v-btn>
            </v-container>
            <v-form ref="eventForm">
              <v-text-field v-model="event.form.name" label="Name" required clearable></v-text-field>
              <v-text-field v-model="event.form.description" label="Description" clearable></v-text-field>
              <v-menu
                  v-model="menu"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  transition="scale-transition"
                  offset-y
                  min-width="auto"
                  clearable
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                      v-model="dateFormat"
                      label="Date"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                      clearable
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
                  clearable
              ></v-select>
              <v-combobox
                  v-model="event.form.selectedParticipants"
                  :items="event.form.persons"
                  :label="event.form.participantLabel"
                  multiple
                  chips
                  clearable
              ></v-combobox>
            </v-form>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="resetForm('event')">
            Cancel
          </v-btn>
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
                clearable
            ></v-text-field>
            <v-text-field
                v-model="location.form.houseNumberStreet"
                label="House number street"
                :rules="[rules.maxSize(7), rules.onlyNumbers()]"
                clearable
            ></v-text-field>
            <v-text-field
                v-model="location.form.streetName"
                label="Street name"
                :rules="[rules.maxSize(25)]"
                clearable
            ></v-text-field>
            <v-text-field
                v-model="location.form.postalCode"
                label="Postal code"
                :rules="[rules.maxSize(7), rules.onlyNumbers()]"
                clearable
            ></v-text-field>
            <v-text-field
                v-model="location.form.city"
                label="City"
                :rules="[rules.maxSize(75)]"
                clearable
            ></v-text-field>
            <v-text-field
                v-model="location.form.country"
                label="Country"
                :rules="[rules.maxSize(50)]"
                clearable
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="resetForm('location')">
            Cancel
          </v-btn>
          <v-btn color="primary" text @click="saveLocation">
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="person.dialog" max-width="500px">
      <v-card>
        <v-card-title>
          Add a person
        </v-card-title>
        <v-card-text>
          <v-form ref="personForm" v-model="person.valid">
            <v-text-field
                v-model="person.form.firstName"
                label="First name"
                :rules="[rules.required(), rules.maxSize(20)]"
                clearable
            ></v-text-field>
            <v-text-field
                v-model="person.form.lastName"
                label="Last name"
                :rules="[rules.maxSize(50)]"
                clearable
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="resetForm('person')">
            Cancel
          </v-btn>
          <v-btn color="primary" text @click="savePerson">
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
        name: null,
        description: null,
        date: "",
        locations: ['Location1', 'Location2'],
        selectedLocations: null,
        persons: ['First_name1 LAST_NAME1', 'First_name2 LAST_NAME2'],
        selectedParticipants: null,
        participantLabel: "Participant"
      }
    },
    location: {
      dialog: null,
      valid: true,
      form: {
        name: null,
        houseNumberStreet: null,
        streetName: null,
        postalCode: null,
        city: null,
        country: null,
      },
    },
    person: {
      dialog: null,
      valid: true,
      form: {
        firstName: null,
        lastName: null,
      }
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
    dateFormat: {
      get: function () {
        return this.event.form.date !== "" ?  this.$dateFormat(this.event.form.date) : ""
      },
      set: function () {
        this.event.form.date = ""
      }
    }
  },

  methods: {
    saveLocation: function () {
      this.$refs.locationForm.validate()
      if (this.location.valid) {
        let json = {}
        json["name"] = this.location.form.name
        if (this.location.form.houseNumberStreet) json["house_number_street"] = this.location.form.houseNumberStreet
        if (this.location.form.streetName) json["street_name"] = this.location.form.streetName
        if (this.location.form.city) json["city"] = this.location.form.city
        if (this.location.form.country) json["country"] = this.location.form.country
        if (this.location.form.postalCode) json["postal_code"] = this.location.form.postalCode
        this.$http.put(this.$api + "/location", json)
            .then(() => {
              this.resetForm("location")
              this.$emit('display', {
                timeout: 2000,
                message: `The location ${json["name"]} has been created.`,
                type: "info"
              })
            })
            .catch((error) => {
              this.$emit('display', {
                timeout: 4000,
                message: `An error occurred : "${error.response.data.detail}".`,
                type: "error"
              })
            })
      } else {
        this.$emit('display', {
          timeout: 2000,
          message: `The form is not completed correctly.`,
          type: "error"
        })
      }
    },
    savePerson: function () {
      this.$refs.personForm.validate()
      if (this.person.valid) {
        let json = {}
        json["first_name"] = this.person.form.firstName
        if (this.person.form.lastName) json["last_name"] = this.person.form.lastName
        this.$http.put(this.$api + "/person", json)
            .then(() => {
              const person = `${json["first_name"]} ${this.person.form.lastName ? json["last_name"].toUpperCase() : ""}`
              this.resetForm("person")
              this.$emit('display', {
                timeout: 2000,
                message: `The person ${person} has been created.`,
                type: "info"
              })
              this.getPersons()
            })
            .catch((error) => {
              this.$emit('display', {
                timeout: 4000,
                message: `An error occurred : "${error.response.data.detail}".`,
                type: "error"
              })
            })
      } else {
        this.$emit('display', {
          timeout: 2000,
          message: `The form is not completed correctly.`,
          type: "error"
        })
      }
    },
    getPersons: function () {
      this.$http.get(this.$api + "/person/all")
          .then((response) => {
            this.event.form.persons = []
            for (const person of response.data) {
              this.event.form.persons.push(
                  `${person["first_name"]} ${person["last_name"] ? person["last_name"].toUpperCase() : ''}`
              )
            }
          })
          .catch((error) => {
            this.$emit('display', {
              timeout: 4000,
              message: `An error occurred : "${error.response.data.detail}".`,
              type: "error"
            })
          })
    },
    getLocations: function () {
      this.$http.get(this.$api + "/location/all")
          .then((response) => {
            this.event.form.locations = []
            for (const location of response.data) {
              this.event.form.locations.push(this.$locationFormat(location))
            }
          })
          .catch((error) => {
            console.log(error)
            this.$emit('display', {
              timeout: 4000,
              message: `An error occurred : "${error.response.data.detail}".`,
              type: "error"
            })
          })
    },
    resetForm: function (form) {
      switch (form) {
        case "event":
          this.$refs.eventForm.reset()
          this.event.dialog = false
          break
        case "location":
          this.$refs.locationForm.reset()
          this.location.dialog = false
          break
        case "person":
          this.$refs.personForm.reset()
          this.person.dialog = false
          break
        default:
          break;
      }
    }
  },

  created() {
    this.getPersons()
    this.getLocations()
  }
}
</script>
