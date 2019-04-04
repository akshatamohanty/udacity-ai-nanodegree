<template>
  <div class="container">
    <h1>{{ headline }}</h1>
    <p>Cillum dolore ullamco voluptate proident sit aliquip Lorem aute commodo. Incididunt consequat Lorem incididunt non aute et adipisicing dolore laboris non laboris amet. Dolore non reprehenderit et deserunt labore laboris deserunt nostrud occaecat ipsum esse.</p>
    <hr />
    <Sudoku />
  </div>
</template>

<script>
import Sudoku from './Sudoku.vue'

export default {
  name: 'AppList',
  props: {
    headline: String
  }, 
  components: {
    Sudoku,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  max-width: 750px;
  margin: 0 auto;
}

</style>
