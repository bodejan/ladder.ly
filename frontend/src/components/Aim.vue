<template>
  <v-container>
    <div>
      <grid :cols="colsAim" :rows="rowsAim"></grid>
    </div>
  </v-container>
</template>

<script>
  import Grid from 'gridjs-vue'
  /**
   * This component displays the AIM in a Grid layout 
   */
  export default {
    components: {
      Grid
    },
    data() {
      return {
        /**columns for aim */
        colsAim: this.$store.state.gridAimCols,
        /**rows for aim */
        rowsAim: this.$store.state.gridAimRows
      }
    }
  }
</script>

<style scoped>
</style>