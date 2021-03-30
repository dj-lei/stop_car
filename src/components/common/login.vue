<template lang="pug">
  v-app
    v-card
      v-card-title
        span {{ "登录" }}
      v-card-text
        v-alert(
          v-model='errorShown'
          transition='slide-y-reverse-transition'
          color='red darken-2'
          tile
          dark
          dense
          icon='mdi-alert'
        ) {{ errorMsg }}
        template(v-if='screen === `login`')
          v-text-field(
            ref="username"
            v-model="username"
            flat
            outlined
            :rules="[() => !!username || '请输入用户名!']"
            label="用户名"
            placeholder="用户名"
            prepend-inner-icon='mdi-clipboard-account'
            background-color='white'
            color='blue darken-2'
            required
            light
          )
          v-text-field(
            ref="password"
            v-model='password'
            flat
            outlined
            :rules="[() => !!password || '请输入密码!']"
            prepend-inner-icon='mdi-clipboard-account'
            background-color='white'
            color='blue darken-2'
            type="password"
            label="密码"
            placeholder='密码'
            required
            light
            @keyup.enter='login'
            )
          v-spacer(class="mt-8")
          v-btn(
              width='100%'
              large
              color='blue darken-2'
              dark
              @click='login'
              :loading='isLoading'
              ) 登录
    v-snackbar(v-model="snackbar", :timeout="timeout") {{ info }}
      template(v-slot:action="{ attrs }")
        v-btn(color="blue", text, v-bind="attrs", @click="snackbar = false") Close
</template>

<script>

export default {
  data () {
    return {
      screen: 'login',
      username: '',
      password: '',
      isLoading: false,
      errorShown: false,
      snackbar: false,
      errorMsg: '',
      info: '',
      timeout: 4000,
    }
  },
  computed: {
    form () {
      return {
        username: this.username,
        password: this.password,
      }
    },
  },
  methods: {
    async login() {
      if (this.username !== '' && this.password !== ''){
        this.isLoading = true

        let formData = new FormData()
        formData.append("username", this.username)
        formData.append("password", this.password)
        let config = {
          headers: {
          'Content-Type': 'multipart/form-data'
          }
        }

        await this.$http.post(this.$urls.stop_car_login, formData, config).then(
          (response)=>{
            this.info = 'Hi ' + this.username + ',welcome!'
            setTimeout(() =>{
              this.snackbar = true
              this.$router.push('/vip')
              this.$store.set('username', this.username)
            },1000)
        }, (error) => {
          this.errorMsg = '账户或者密码不正确!'
          this.errorShown = true
          this.isLoading = false
          setTimeout(() =>{
            this.errorShown = false
          },4000)
        })
      }else{
        this.$refs['username'].validate(true)
        this.$refs['password'].validate(true)
      }
    },
  }
}
</script>
