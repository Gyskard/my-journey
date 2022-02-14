<template>
  <v-container>
    <v-row>
      <v-col>
        <v-text-field v-model="search" label="Search" prepend-icon="mdi-magnify"></v-text-field>
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
      <v-col>
        <v-select
            v-model="sort"
            :items="sortMethods"
            label="Sort by"
            prepend-icon="mdi-sort-reverse-variant"
            clearable
        ></v-select>
      </v-col>
      <v-col>
        <v-select
            v-model="order"
            :items="orderMethods"
            label="Order by"
            :prepend-icon="orderIcon"
            clearable
        ></v-select>
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
      sort: null,
      sortMethods: ["Name", "Date", "Location"],
      order: null,
      orderMethods: ["Ascending", "Descending"],
      orderIcon: "mdi-arrow-top-right-thin"
    }),

    computed: {
      dateFormatToDisplay: function() {
        if (this.dates === null) return null
        if (this.dates.length === 1) return this.$dateFormat(this.dates[0])
        if (this.dates[0] === this.dates[1]) return this.$dateFormat(this.dates[0])
        return `${this.$dateFormat(this.dates[0])} to ${this.$dateFormat(this.dates[1])}`
      },
    },

    watch: {
      order: function () {
        this.orderIcon = `mdi-arrow-top-right-thin ${this.order === "Descending" ? "mdi-rotate-90" : ""}`
      }
    }
  }
</script>
