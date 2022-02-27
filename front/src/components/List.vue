<template>
  <v-container>
    <v-expansion-panels focusable style="max-width: 75em;">
      <Event v-for="event in events" :key="event" :event="event" class="mt-3"/>
    </v-expansion-panels>
  </v-container>
</template>

<script>
import Event from "@/components/Event"

export default {
  name: 'List',

  components: {
    Event
  },

  props: ["searchForm"],

  data: () => ({
    events: []
  }),

  created() {
    this.getEvents({
      search: null,
      date: null,
      order_by: "Descending",
    })
  },

  methods: {
    getEvents: function (search) {
      this.$http.post(this.$api + "/event/filter", search)
        .then(response => {
          this.events = response.data
        })
        .catch(error => {
          this.$emit('display', {
            timeout: 4000,
            message: `An error occurred : "${error.response.data.detail}".`,
            type: "error"
          })
        })
    }
  },

  watch: {
    searchForm: {
      handler(search) {
        this.getEvents(search)
      },
      deep: true
    }
  }
}
</script>
