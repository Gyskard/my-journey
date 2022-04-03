<template>
  <v-container>
    <v-row>
      <v-col>
        <v-text-field v-model="form.search" label="Search" prepend-icon="mdi-magnify"></v-text-field>
      </v-col>
      <v-col v-if="persons.length > 0">
        <v-autocomplete
            v-model="form.selectedParticipants"
            :items="persons"
            item-text="displayName"
            item-value="id"
            label="Participants"
            multiple
            clearable
            prepend-icon="mdi-account"
            small-chips
            deletable-chips
        ></v-autocomplete>
      </v-col>
      <v-col>
        <v-text-field v-model="form.location" label="Location" prepend-icon="mdi-map-marker"></v-text-field>
      </v-col>
      <v-col>
        <v-menu
            ref="menu"
            v-model="menu"
            :close-on-content-click="false"
            transition="scale-transition"
            offset-y
            min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
                v-model="dateFormatToDisplay"
                label="Date"
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
                clearable
                @click:clear="clearDates"
            ></v-text-field>
          </template>
          <v-date-picker
              v-model="form.dates"
              no-title
              scrollable
              range
              color="orange darken-1"
          >
          </v-date-picker>
        </v-menu>
      </v-col>
      <v-col>
        <v-select
            v-model="form.order_by"
            :items="orderMethods"
            label="Order by (date)"
            :prepend-icon="orderIcon"
        ></v-select>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'Search',

    data: () => ({
      menu: false,
      persons: [],
      form: {
        search: "",
        selectedParticipants: [],
        location: "",
        dates: null,
        order_by: "Descending",
      },
      orderMethods: ["Ascending", "Descending"],
      orderIcon: "mdi-rotate-90 mdi-arrow-top-right-thin"
    }),

    methods: {
      clearDates: function () {
        this.form.dates = null
        this.$emit('searchFormChanged', this.form)
      },
      getPersons: function () {
        this.$http.get(this.$api + "/person/all")
            .then((response) => {
              this.persons = []
              for (const person of response.data) {
                this.persons.push({
                  id: person.id,
                  displayName: `${person["first_name"]} ${person["last_name"] ? person["last_name"].toUpperCase() : ''}`
                })
              }
              if (this.persons.length > 0) {
                console.log(this.persons[0]["id"])
                this.selectedParticipants = [this.persons[0]["id"]]
              }
            })
            .catch((error) => {
              this.displayErrorMessage(error.response.data.detail)
            })
      },
    },

    computed: {
      dateFormatToDisplay: function() {
        if (this.form.dates === null) return null
        if (this.form.dates.length === 1) return this.$dateFormat(this.form.dates[0])
        if (this.form.dates[0] === this.form.dates[1]) return this.$dateFormat(this.form.dates[0])
        return `${this.$dateFormat(this.form.dates[0])} to ${this.$dateFormat(this.form.dates[1])}`
      },
    },

    watch: {
      form: {
        handler() {
          this.$emit('searchFormChanged', this.form)
        },
        deep: true
      },
      'form.order_by': function () {
        this.orderIcon = `mdi-arrow-top-right-thin ${this.form.order_by === "Descending" ? "mdi-rotate-90" : ""}`
      }
    },

    created() {
      this.getPersons()
    }
  }
</script>

<style>
.v-select__selections {
  min-height: 33px !important;
}
</style>