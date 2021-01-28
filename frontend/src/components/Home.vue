<template>
  <v-container>
    <h1> ladder.ly </h1>
    <p>Upload your files to create an interactive hierarchical value map</p>
    <v-container>
      <v-file-input type="file" label="Click here to select a ladders.xlsx file" show-size v-model="ladders"></v-file-input>
      <v-file-input type="file" label="Click here to select a labels.xlsx file" show-size v-model="labels"></v-file-input>
      <v-btn v-on:click="submitFile()">Submit</v-btn>
    </v-container>
    <v-container>
      <h2> Download example data </h2>
      <p> Please make sure that your data has exactly the same format </p> 
      <v-row>
            <v-col
                cols="12"
                sm="6"
                md="3"
            ><v-btn v-on:click="requestLaddersExample()">ladders_example.xlsx</v-btn>
            </v-col>
            <v-col
                cols="12"
                sm="6"
                md="3"
            ><v-btn v-on:click="requestLabelsExample()">labels_example.xlsx</v-btn>
            </v-col>

      </v-row>
    </v-container>


  </v-container>
</template>

<script>
/**
 * This component represents the home/landing page, where the xlsx data is uploaded
 */
export default {
  data () {
    return {
      /**save uploaded ladders
       * @type xlsx
       */
      ladders: null,
      /**save uploaded labels
       * @type xlsx
       */
      labels: null
    }
  },
  methods: {
    /**used for testing purposes only */
    pingPong () {
      this.$store.dispatch('loadPingPong')
    },
    /**submit uploaded files to store, then push /hvm */
    submitFile () {
      this.$store.dispatch('loadNetworkData', { ladders: this.ladders, labels: this.labels })
        .then(() => this.$store.dispatch('loadGridData'))
        .then(() => this.$router.push('/Hvm'))
    },
    /**request example labels for download */
    requestLabelsExample () {
      this.$store.dispatch('loadLabelsExample')
    },
    /**request example ladders for download */
    requestLaddersExample () {
      this.$store.dispatch('loadLaddersExample')
    },
  },
  computed: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
