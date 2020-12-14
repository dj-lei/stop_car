<template lang="pug">
  v-app(dark)
    v-main(ref='content')
      v-container
        v-card
          v-card-title(class="headline")
            span Stop Car Query
          v-card-text
            v-row
              v-col(:cols="6")
                v-text-field(
                  v-model="carNumber"
                  flat
                  outlined
                  label="carNumber"
                  placeholder="carNumber"
                  prepend-inner-icon='mdi-arrow-up-bold-box-outline'
                  background-color='white'
                  color='blue darken-2'
                  required
                  light
                )
              v-btn(class="mt-4" large color='blue darken-2' dark @click='query' :loading='isLoadingQuery') QUERY
            v-row
              v-col(:cols="6")
                v-file-input(v-model="stop_car_file",  solo,  prepend-icon="mdi-email", color="deep-purple accent-4",  label="Upload cars number", placeholder="Upload cars number", outlined)
              v-btn(class="mt-4 me-2", large color='blue darken-2' :disabled='stop_car_file.length === 0', @click="run" :loading='isLoadingRun') RUN
              v-btn(class="mt-4 me-2", large color='blue darken-2' :disabled='stop_car_file.length === 0', @click="stop") STOP
              v-btn(class="mt-4", large color='blue darken-2' :disabled='stop_car_file.length === 0', @click="exportExcel") EXPORT
          v-data-table(:headers="headers", :items="data", class="elevation-1")
          v-dialog(v-model='progress', persistent, width='200px')
            div(class="text-center")
              v-progress-circular(
              indeterminate
              size='100'
              width='15'
              color='green lighten-3'
              ) Waiting

</template>

<script>
import { get, sync } from 'vuex-pathify'

export default {
  computed: {
    progress: sync('progress')
  },
  data() {
    return {
      isLoadingQuery: false,
      isLoadingRun: false,
      carNumber: '',
      stop_car_file: [],
      headers: [
        { text: 'CarNumber', value: 'CarNumber' },
        { text: 'ETCP', value: 'ETCP'},
        { text: '截停车', value: 'JIETINGCHE' },
      ],
      data: [],
    }
  },
  methods: {
    async query () {
      this.isLoadingQuery = true
      await this.$http.get(this.$urls.stop_car_query, {
        params: {
            car_number: 'car_number',
        },
        })
        .then(response => {
          this.data = response.data.content
          this.isLoadingQuery = false
        })
    },
    run () {

    },
    stop () {

    },
    exportExcel () {

    },
  },
}
</script>

<style lang="scss">

.v-progress-circular {
margin: 2rem;
}

.breadcrumbs-nav {
  .v-btn {
    min-width: 0;
    &__content {
      text-transform: none;
    }
  }
  .v-breadcrumbs__divider:nth-child(2n) {
    padding: 0 6px;
  }
  .v-breadcrumbs__divider:nth-child(2) {
    padding: 0 6px 0 12px;
  }
}

.page-col-sd {
  margin-top: -90px;
  align-self: flex-start;
  position: sticky;
  top: 64px;
  max-height: calc(100vh - 64px);
  overflow-y: auto;
  -ms-overflow-style: none;
}

.page-col-sd::-webkit-scrollbar {
  display: none;
}

</style>
