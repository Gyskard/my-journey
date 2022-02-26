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
    events: [],
    filters: {
      search: "daz",
      date: null,
      order_by: "descending",
    }
  }),

  created() {
    this.getEvents()
  },

  methods: {
    getEvents: function () {
      this.$http.post(this.$api + "/event/filter", this.filters)
        .then(events => events.data.map(event => this.events.push(event)))
        .catch(error => {
          this.$emit('display', {
            timeout: 4000,
            message: `An error occurred : "${error.response.data.detail}".`,
            type: "error"
          })
        })

    }
  }
}
</script>
