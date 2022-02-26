<template>
  <v-expansion-panel>
    <v-expansion-panel-header>
      <v-row no-gutters>
        <v-col cols="4">
          {{ event.event_name }}
        </v-col>
        <v-col cols="8" class="text--secondary">
          <v-row>
            <v-col cols="4">
              {{ this.$dateFormat(event.date) }}
            </v-col>
            <v-col cols="4">
              {{ event.location.name }}
            </v-col>
            <v-col cols="4" v-if="event.persons.length > 0">
              {{ event.persons.length }} {{ event.persons.length === 1 ? "participant" : "participants" }}
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-expansion-panel-header>
    <v-expansion-panel-content>
      <v-card>
        <v-card-text>
          <p class="text-h6 text--primary">
            {{ event.event_name }}
          </p>
          <p v-if="event.description">{{ event.description }}</p>
          <v-chip-group column v-if="event.persons.length > 0" active-class="secondary">
            <v-chip class="secondary accent-4 white--text" v-for="person in event.persons" :key="person">
              {{ formatPerson(person) }}
            </v-chip>
          </v-chip-group>
        </v-card-text>
      </v-card>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
export default {
  name: 'Event',

  props: ["event"],

  methods: {
    formatPerson: function(person) {
      let result = person["first_name"][0].toUpperCase() + person["first_name"].slice(1).toLowerCase()
      if (person["last_name"] !== null) result += ` ${person["last_name"].toUpperCase()}`
      return result
    },
    formatPersonsListToDisplay: function(persons) {
      let result = ""
      for (const person of persons) result += `${result !== "" ? ", " : ""}${this.formatPerson(person)}`
      return result
    }
  }
}
</script>

<style>
.v-card {
  box-shadow: none !important;
}
</style>
