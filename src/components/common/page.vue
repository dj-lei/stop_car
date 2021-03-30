<template lang="pug">
  v-app(dark)
    v-main(ref='content')
      v-container
        v-card
          v-card-title(class="headline")
            span 位置查询
            v-spacer
            v-btn(rounded @click='logout') 注销
          v-card-text
            v-row
              v-col(:cols="6")
                v-file-input(v-model="stop_car_file",  solo,  prepend-icon="mdi-arrow-up-bold-box-outline", color="deep-purple accent-4",  label="上传车牌号excel文件", placeholder="上传车牌号excel文件", outlined)
              v-btn(class="mt-4 me-2", large color='blue darken-2' :disabled='stop_car_file.length === 0', @click="run" :loading='isLoadingRun') 开始运行
            v-row
              v-col(:cols="6")
                v-text-field(
                  v-model="carNumber"
                  flat
                  outlined
                  label="增加车牌号"
                  placeholder="增加车牌号"
                  background-color='white'
                  color='blue darken-2'
                  required
                  light
                )
              v-btn(class="mt-4" large color='blue darken-2' @click='query') 查询
              //- v-btn(class="mt-4 me-2", large color='blue darken-2' :disabled='data.length === 0', @click="stop") STOP
              //- download-excel(:data="data" type="csv" name="stop_car_query.csv")
                v-btn(class="mt-4 me-2" large color='blue darken-2' :disabled='data.length === 0') EXPORT
                v-btn(class="mt-4 me-2", large color='blue darken-2' :disabled='data.length === 0', @click="clear") CLEAR
          v-data-table(:headers="headers", :items="data", class="elevation-1")

</template>

<script>
import { get, sync } from 'vuex-pathify'


export default {
  computed: {
    username: sync('username')
  },
  data() {
    return {
      isLoadingQuery: false,
      isLoadingRun: false,
      isStop: false,
      carNumber: '',
      stop_car_file: [],
      interval: '',
      headers: [
        { text: '车牌号', value: 'card' },
        { text: '停车场', value: 'pltName' },
        { text: '地址1', value: 'address1' },
        { text: '地址2', value: 'address2'},
        { text: '入场时间', value: 'comeTime' },
        // { text: '车详情', value: 'detail' },
        { text: '状态', value: 'state' },
      ],
      data: [],
    }
  },
  mounted () {
    let that = this

    history.pushState(null, null, document.URL)
    window.addEventListener('popstate', function () {
      history.pushState(null, null, document.URL)
    })
    this.interval = setInterval(function() {
      that.get_data()
    },3000)
  },
  methods: {
    async get_data () {
      await this.$http.get(this.$urls.stop_car_get, {
        params: {
            username: this.username,
        },
        })
        .then(response => {
          this.data = response.data.content
        })
    },
    async query () {
      await this.$http.get(this.$urls.stop_car_query, {
        params: {
            username: this.username,
            car_number: this.carNumber,
        },
        })
        .then(response => {
          this.data = response.data.content
        })
    },
    async run () {
      let formData = new FormData()
      this.isLoadingRun = true
      formData.append("username", this.username)
      formData.append("file", this.stop_car_file)
      
      let config = {
        headers: {
        'Content-Type': 'multipart/form-data'
        }
      }

      await this.$http.post(this.$urls.stop_car_run, formData, config).then(
        (response)=>{
        setTimeout(() =>{
          this.isLoadingRun = false
          console.log(response.data.content)
        },1000)
      }, (error) => {
      })
    },
    logout () {
      clearInterval(this.interval)
      this.$router.push('/')
    }
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
