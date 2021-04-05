<template lang="pug">
  div(id="app")
    v-app(id="inspire")
      v-main(ref='content')
        //- v-card(min-width="1200px", min-height="1000px")
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
