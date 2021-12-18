<template>
  <v-container style="max-width: 75em;">
    <v-row>
      <v-col>
        <v-text-field v-model="search" label="Search" prepend-icon="mdi-magnify" class="mx-5"></v-text-field>
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
            ></v-text-field>
          </template>
          <v-date-picker
              v-model="dates"
              no-title
              scrollable
              range
              color="orange darken-1"
          >
          </v-date-picker>
        </v-menu>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'Search',

    data: () => ({
      search: "",
      dates: null,
      menu: false,
    }),

    computed: {
      dateFormatToDisplay: function() {
        let date;
        if (this.dates === null) date = null
        else if (this.dates.length === 1) date = this.$dateFormat(this.dates[0])
        else if (this.dates.length === 2) {
          if (this.dates[0] === this.dates[1]) date = this.$dateFormat(this.dates[0])
          else date = `${this.$dateFormat(this.dates[0])} to ${this.$dateFormat(this.dates[1])}`
        }
        return date
      },
    }
  }
</script>
