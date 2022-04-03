<template>
  <div class="d-flex flex-column">
    <v-container id="counter" class="d-flex justify-end">{{ eventNumber }} results</v-container>
    <v-container class="d-flex justify-center">
        <v-expansion-panels focusable class="mx-3" style="max-width: 75em">
          <Event v-for="event in events" :key="event" :event="event" />
        </v-expansion-panels>
    </v-container>
    <v-container>
      <div v-if="eventsPageNumber !== 0" class="mt-7">
        <v-pagination v-model="selectedPage" :length="eventsPageNumber"></v-pagination>
      </div>
    </v-container>
  </div>
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
    events: [],
    eventsPageNumber: 1,
    eventNumber: 0,
    selectedPage: null,
    oldSelectedPage: null
  }),

  created() {
    this.getEvents({
      search: null,
      date: null,
      order_by: "Descending",
    }, 0)
  },

  methods: {
    getEvents: function (search, selectedPage) {
      search.offset = selectedPage
      console.log(search)
      this.$http.post(this.$api + "/event/filter", search)
        .then(response => {
          this.events = response.data["events"]
          this.eventsPageNumber = response.data["events_page_number"]
          this.selectedPage = selectedPage + 1
          this.eventNumber = response.data["event_number"]
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
        this.getEvents(search, 0)
      },
      deep: true
    },
    selectedPage: function (value) {
      if (this.oldSelectedPage !== null) {
        if (value !== undefined) {
          let form = this.searchForm
          if (form.order_by === undefined) form.order_by = "Descending"
          this.getEvents(form, value - 1)
        }
      }
      this.oldSelectedPage = value
    }
  }
}
</script>

<style>

#counter {
  max-width: 75em;
  padding-bottom: 0;
  padding-top: 0
}

</style>