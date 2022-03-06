<template>
  <v-container>
    <div>
      <v-expansion-panels focusable class="mx-3" style="max-width: 75em">
        <Event v-for="event in events" :key="event" :event="event" />
      </v-expansion-panels>
      <div v-if="eventsPageNumber !== 0" class="text-center mt-7">
        <v-pagination v-model="selectedPage" :length="eventsPageNumber" class="d-block"></v-pagination>
      </div>
    </div>
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
    events: [],
    eventsPageNumber: 1,
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
      this.$http.post(this.$api + "/event/filter", search)
        .then(response => {
          this.events = response.data["events"]
          this.eventsPageNumber = response.data["events_page_number"]
          this.selectedPage = selectedPage + 1
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
