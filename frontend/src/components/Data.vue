<template>
  <v-container>
    <div>
      <grid :cols="colsLabels" :rows="rowsLabels"></grid>
    </div>
    <v-divider class="pa-4"></v-divider>
    <div>
      <grid :cols="colsLadders" :rows="rowsLadders"></grid>
    </div>
  </v-container>
</template>

<script>
  import Grid from 'gridjs-vue'
  /**
   * This component displays the uploaded xlsx data in a Grid layout 
   */
  export default {
    components: {
      Grid
    },
    data() {
      return {
        /**columns for labels table */
        colsLabels: [
            {
                name: 'ACV',
                id: 'acv'
            },
            {
                name: 'Labelcode',
                id: 'labelcode'
            },
            {
                name: 'Label',
                id: 'name'
            }
        ],
        /**rows for labels table */
        rowsLabels: this.$store.state.gridLabels,
        /**columns for ladders table */
        colsLadders: this.$store.state.gridLaddersCols,
        /**rows for ladders table */
        rowsLadders: this.$store.state.gridLaddersRows,
      }
    }
  }
</script>

<style scoped>
</style>
