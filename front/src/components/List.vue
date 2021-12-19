<template>
  <v-container>
    <v-expansion-panels focusable style="max-width: 75em;">
      <Event v-for="event in events" :key="event" :event="event" class="mt-3"/>
    </v-expansion-panels>
  </v-container>
</template>

<script>
import Event from "@/components/Event";
export default {
  name: 'List',

  components: {
    Event
  },

  data: () => ({
    events: [
      {
        name: "Event 1",
        description: "This is a description.",
        date: "2021-03-24",
        location: {
          name: "Location",
          house_number_street: 0,
          street_name: "Street",
          city: "City",
          country: "Country",
          postal_code: 0
        },
        persons: [
          {
            first_name: "First_name",
            last_name: "Last_name"
          }
        ]
      },
      {
        name: "Event 2",
        description: "This is a description.",
        date: "2021-03-24",
        location: {
          name: "Location",
          house_number_street: null,
          street_name: null,
          city: null,
          country: null,
          postal_code: null
        },
        persons: [
          {
            first_name: "First_name",
            last_name: "Last_name"
          },
          {
            first_name: "First_name",
            last_name: "Last_name"
          }
        ]
      }
    ],
  }),
}
</script>
