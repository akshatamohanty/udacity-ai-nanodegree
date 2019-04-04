<template>
  <div id="app">
    <AppList headline="Artificial Intelligence Nanodegree"/>
  </div>
</template>

<script>
import AppList from './components/AppList.vue'

export default {
  name: 'app',
  components: {
    AppList
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
