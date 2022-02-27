<template>
  <v-container>
    <v-row>
      <v-col>
        <v-text-field v-model="form.search" label="Search" prepend-icon="mdi-magnify"></v-text-field>
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
      form: {
        search: "",
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
      }
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
      },
    }
  }
</script>
