<template>
  <v-expansion-panel>
    <v-expansion-panel-header>
      <v-row no-gutters>
        <v-col cols="4">
          {{ event.name }}
        </v-col>
        <v-col cols="8" class="text--secondary">
          <v-row>
            <v-col cols="4">
              {{ this.$dateFormat(event.date) }}
            </v-col>
            <v-col cols="4">
              {{ event.location.name }}
            </v-col>
            <v-col cols="4">
              {{ event.persons.length }} {{ event.persons.length === 1 ? "participant" : "participants" }}
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-expansion-panel-header>
    <v-expansion-panel-content>
      <div class="mt-4"> <!-- used div to prevent visual bug when defocusing -->
        {{ event.description }}
      </div>
      <br/>
      <div>
        <b>{{ event.persons.length === 1 ? "Participant" : "Participants" }}</b> : {{ formatPersonsListToDisplay(event.persons) }}
      </div>
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
