<template>
  <v-container>
    <div>
      <grid :cols="colsAim" :rows="rowsAim"></grid>
    </div>
    <v-row>
      <v-col
          cols="12"
          sm="6"
          md="3"
      ><v-btn v-on:click="requestAim()">aim.csv</v-btn>
      </v-col>
    </v-row>
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
    },
    methods: {
      requestAim() {
        this.$store.dispatch('loadAim')
      }
    }
  }
</script>

<style scoped>
</style>