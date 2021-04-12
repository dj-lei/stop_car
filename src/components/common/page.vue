<template lang="pug">
  v-app(dark)
    v-main(ref='content')
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
          v-row
            v-col(:cols="6")
              v-menu(v-model="pick_time" :close-on-content-click="false" :nudge-right="40" transition="scale-transition" offset-y min-width="auto")
                template(v-slot:activator="{ on, attrs }")
                  v-text-field(v-model="date" label="限制时间" prepend-icon="mdi-calendar" clearable readonly v-bind="attrs" v-on="on")
                v-date-picker(v-model="date" locale="zh-cn" no-title scrollable @input="pick_time = false")
        v-card
          v-card-title
            v-text-field(v-model="search" label="Search" single-line hide-details)
          v-data-table(:search="search" :headers="headers", :items="data", sort-by="comeTime", sort-desc class="elevation-1")
            template(v-slot:item.img="{ item }")
              v-img(max-height="150" max-width="250" :src="item.img")
            template(v-slot:item.actions="{ item }")
              v-tooltip(bottom)
                template(v-slot:activator="{ on,attrs }")
                  v-icon(small, class="mr-2", v-bind="attrs", v-on="on", @click="history_query(item)") mdi-history
                span 历史记录
              v-tooltip(bottom)
                template(v-slot:activator="{ on,attrs }")
                  v-icon(small, class="mr-2", v-bind="attrs", v-on="on", @click="detail_query(item)") mdi-content-copy
                span 车辆详情
              v-tooltip(bottom)
                template(v-slot:activator="{ on,attrs }")
                  v-icon(small, class="mr-2", v-bind="attrs", v-on="on", @click="hide_car(item)") mdi-delete
                span 隐藏该车
        v-dialog(v-model='dialogDetail', max-width="600px")
          v-card
            v-simple-table(dense)
              template(v-slot="")
                thead
                  tr
                    th(class="text-left") 名称
                    th(class="text-left") 信息
                tbody
                  tr(v-for="item in detail" :key="item.name")
                    td {{ item.name }}
                    td {{ item.value }}
            v-text-field(id="id_text" :value="detail_copy")
            v-spacer(class="mt-8")
              v-btn(
                width='100%'
                large
                color='blue darken-2'
                dark
                @click='copy_info'
                ) 复制车辆信息
        v-dialog(v-model='dialogHistory', max-width="600px")
          v-card
            v-simple-table(dense)
              template(v-slot="")
                thead
                  tr
                    th(class="text-left") 地址1
                    th(class="text-left") 地址2
                    th(class="text-left") 入场时间
                    th(class="text-left") 出场时间
                tbody
                  tr(v-for="item in history" :key="item.name")
                    td {{ item.address1 }}
                    td {{ item.address2 }}
                    td {{ item.comeTime }}
                    td {{ item.leaveTime }}
        v-snackbar(v-model="snackbar", :timeout="3000") {{ info }}
          template(v-slot:action="{ attrs }")
            v-btn(color="blue", text, v-bind="attrs", @click="snackbar = false") 关闭
</template>

<script>
import { get, sync } from 'vuex-pathify'
import tip_sound from '../../assets/recovery.mp3'


export default {
  computed: {
    username: sync('username')
  },
  data() {
    return {
      dialogHistory:false,
      dialogDetail:false,
      isLoadingQuery: false,
      isLoadingRun: false,
      isStop: false,
      snackbar: false,
      search:'',
      pick_time:'',
      carNumber: '',
      date: '2021-04-01',
      stop_car_file: [],
      interval: '',
      info: '已成功加载车辆信息,并在后台查询,一旦查询成功会自动返回,请耐心等待.',
      headers: [
        { text: '车牌号', value: 'card' },
        { text: '停车场', value: 'pltName' },
        { text: '图片', value: 'img' },
        { text: '地址1', value: 'address1' },
        { text: '地址2', value: 'address2'},
        { text: '入场时间', value: 'comeTime' },
        // { text: '车详情', value: 'detail' },
        { text: '状态', value: 'state' },
        { text: '操作', value: 'actions', sortable: false },
      ],
      data: [],
      history: '',
      detail: '',
      detail_copy: '',
      hide_pool: [],
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
          let tmp = this.data
          this.limit_time(response.data.content)
          this.hide_cars()
          if(tmp.length !== this.data.length){
            let tip = new Audio(tip_sound)
            tip.play()
          }
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
          this.info = '已成功加载车辆信息,并在后台查询,一旦查询成功会自动返回,请耐心等待.'
          this.snackbar = true
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
          this.info = '已成功加载车辆信息,并在后台查询,一旦查询成功会自动返回,请耐心等待.'
          this.snackbar = true
        },1000)
      }, (error) => {
      })
    },
    async history_query(item){
      await this.$http.get(this.$urls.stop_car_history, {
        params: {
            username: this.username,
            car_number: item.card,
        },
        })
        .then(response => {
          this.history = response.data.content
          this.dialogHistory = true
        })
    },
    async detail_query(item){
      await this.$http.get(this.$urls.stop_car_detail, {
        params: {
            username: this.username,
            car_number: item.card,
        },
        })
        .then(response => {
          this.detail = response.data.content
          this.combine_info(response.data.content)
          this.dialogDetail = true
        })
    },
    hide_car(item){
      this.hide_pool.push(item.card)
      this.hide_cars()
    },
    hide_cars(){
      let tmp = []
      this.data.forEach((elm) => {
        if(this.hide_pool.indexOf(elm.card) == -1){
          tmp.push(elm)
        }
      })
      this.data = tmp
    },
    limit_time(data){
      this.data = []
      data.forEach((elm) => {
        let date1 = new Date(this.date)
        let date2 = new Date(elm['comeTime'])
        if(date2.getTime() >= date1.getTime()){
          this.data.push(elm)
        }
      })
    },
    combine_info(data){
      this.detail_copy = ''
      data.forEach((elm) => {
        this.detail_copy = this.detail_copy + elm['name'] + ':' + elm['value'] + ' '  
      })
    },
    copy_info(){
      document.getElementById('id_text').select()
      document.execCommand("Copy")
      this.info = '车辆信息已复制'
      this.snackbar = true
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
