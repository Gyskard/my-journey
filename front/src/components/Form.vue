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
            <v-form ref="eventForm" v-model="event.valid">
              <v-text-field
                  v-model="event.form.name"
                  label="Name" required clearable
                  :rules="[rules.required(), rules.maxSize(50)]"
              ></v-text-field>
              <v-text-field
                  v-model="event.form.description"
                  label="Description"
                  clearable
                  :rules="[rules.maxSize(100)]"
              ></v-text-field>
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
                      :rules="[rules.required()]"
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
                  :item-text="item => this.$locationFormat(item)"
                  item-value="id"
                  label="Location"
                  required
                  clearable
                  :rules="[rules.required()]"
              ></v-select>
              <v-autocomplete
                  v-model="event.form.selectedParticipants"
                  :items="event.form.persons"
                  item-text="displayName"
                  item-value="id"
                  :label="event.form.participantLabel"
                  multiple
                  chips
                  clearable
                  :rules="[rules.required()]"
              ></v-autocomplete>
              <v-file-input
                  v-model="event.form.pictures"
                  label="Pictures"
                  counter
                  prepend-icon=""
                  multiple
                  truncate-length="15"
              ></v-file-input>
            </v-form>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="resetForm('event')">
            Cancel
          </v-btn>
          <v-btn color="primary" text @click="saveEvent">
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
      valid: true,
      form: {
        name: null,
        description: null,
        date: "",
        locations: "",
        selectedLocations: null,
        persons: [],
        selectedParticipants: null,
        participantLabel: "Participant",
        pictures: []
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
        country: null
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
        return v => !!v || 'This field is required'
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
    saveEvent: function() {
      this.$refs.eventForm.validate()
      if (!this.event.valid) return

      const uploadPicturesRequest = async () => {
        if (this.event.form.pictures.length === 0) return Promise.resolve()
        let files = new FormData()
        for (const picture of this.event.form.pictures) files.append("pictures", picture)
        return await this.$http.post(this.$api + "/pictures", files)
      }

      const createEventRequest = async (filenames) => {
        let jsonEvent = {
          event_name: this.event.form.name,
          date: this.event.form.date,
          location_id: this.event.form.selectedLocations
        }
        if (this.event.form.description) jsonEvent["description"] = this.event.form.description
        if (filenames.length > 0) jsonEvent["pictures"] = filenames
        return await this.$http.put(this.$api + "/event", jsonEvent)
      }

      const createParticipationRequest = async (eventId) => {
        return await this.$http.put(this.$api + "/participation", {
          event_id: eventId,
          person_id_list: this.event.form.persons.map(person => person.id)
        })
      }

      uploadPicturesRequest()
          .then((uploadPicturesResponse) => {
            createEventRequest(uploadPicturesResponse ? uploadPicturesResponse.data : [])
              .then((createEventResponse) => {
                createParticipationRequest(createEventResponse.data)
                  .then(() => {
                    this.displaySuccessMessage(`The event ${this.event.form.name} has been created.`)
                    this.resetForm("event")
                  })
                  .catch((error) => {
                    this.displayErrorMessage(error.response.data.detail)
                  })
              })
              .catch((error) => {
                this.displayErrorMessage(error.response.data.detail)
              })
          })
          .catch((error) => {
            this.displayErrorMessage(error.response.data.detail)
          })
    },
    saveLocation: function () {
      this.$refs.locationForm.validate()
      if (!this.location.valid) {
        this.displayErrorMessage('The form is not completed correctly.')
        return
      }
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
            this.displaySuccessMessage(`The location ${json["name"]} has been created.`)
          })
          .catch((error) => {
            this.displayErrorMessage(error.response.data.detail)
          })
    },
    savePerson: function () {
      this.$refs.personForm.validate()
      if (!this.person.valid) {
        this.displayErrorMessage('The form is not completed correctly.')
        return
      }
      let json = {}
      json["first_name"] = this.person.form.firstName
      if (this.person.form.lastName) json["last_name"] = this.person.form.lastName
      this.$http.put(this.$api + "/person", json)
          .then(() => {
            const person = `${json["first_name"]} ${this.person.form.lastName ? json["last_name"].toUpperCase() : ""}`
            this.resetForm("person")
            this.displaySuccessMessage(`The person ${person} has been created.`)
            this.getPersons()
          })
          .catch((error) => {
            this.displayErrorMessage(error.response.data.detail)
          })
    },
    getPersons: function () {
      this.$http.get(this.$api + "/person/all")
          .then((response) => {
            this.event.form.persons = []
            for (const person of response.data) {
              this.event.form.persons.push({
                id: person.id,
                displayName: `${person["first_name"]} ${person["last_name"] ? person["last_name"].toUpperCase() : ''}`
              })
            }
          })
          .catch((error) => {
            this.displayErrorMessage(error.response.data.detail)
          })
    },
    getLocations: function () {
      this.$http.get(this.$api + "/location/all")
          .then((response) => {
            this.event.form.locations = []
            for (const location of response.data) {
              this.event.form.locations.push(location)
            }
          })
          .catch((error) => {
            this.displayErrorMessage(error.response.data.detail)
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
    },
    displaySuccessMessage: function(msg) {
      this.$emit('display', {
        timeout: 2000,
        message: msg,
        type: "info"
      })
    },
    displayErrorMessage: function(msg) {
      this.$emit('display', {
        timeout: 4000,
        message: `An error occurred : "${msg}".`,
        type: "error"
      })
    }
  },

  created() {
    this.getPersons()
    this.getLocations()
  }
}
</script>
