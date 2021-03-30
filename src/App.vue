<template lang="pug">
  div(id="app")
    v-app(id="inspire")
      v-main(ref='content')
        v-container
          <router-view></router-view>
</template>

<script>

export default {
  data () {
    return {
    }
  }
}
</script>
