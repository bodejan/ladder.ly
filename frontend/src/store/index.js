import Vue from 'vue'
import Vuex from 'vuex'

import {fetchGridData, fetchPingPong, fetchLaddersExample, fetchLabelsExample, fetchNetworkData, fetchAimDownload} from '@/api'

Vue.use(Vuex)

/**
 * @class
 * source of data
 */
const state = {
  /** labels needed for the grid layout, to visualize uploaded data*/
  gridLabels: [],
  /** ladder columns needed for the grid layout, to visualize uploaded data*/
  gridLaddersCols: [],
  /** ladder rows needed for the grid layout, to visualize uploaded data*/
  gridLaddersRows: [],
  /** aim columns needed for the grid layout, to visualize aim*/
  gridAimCols: [],
  /** aim rows needed for the grid layout, to visualize aim*/
  gridAimRows: [],
  /** uploaded ladders, labels */
  upload: new FormData(),
  pingPong: 'Interactive HVM',
  /** cutOffValue default -1 */
  cutOffValue: '-1',
  /** indicates selected radio button in hvm */
  radioInDirect: "direct",
  /** possible treatments */
  treatments: [],
  /** default selected treatment */
  radioTreatments: "All"
}

/**
 * @class
 * asynchronous operations 
 */

const actions = {
  loadPingPong (context) {
    var input = ''
    if (this.state.pingPong=='Interactive HVM') {
      input = 'Ping!'
    } else {
      input = 'notPing!'
    }
    return fetchPingPong(input)
      .then((response) => context.commit('setPingPong', { pingPong: response.data }))
      .catch((error) => {
        console.error(error)
      })
  },
  /**
   * triggers api call to fetch initial vis-network data from BE, safes upload
   * calls setNetworkData to save returned data in state
   * @param {*} context - context 
   * @param {*} upload - uploaded xlsx ladders, labels
   */
  loadNetworkData (context, {ladders, labels}) {
    let upload = new FormData()
    upload.append('uploadLadders', ladders)
    upload.append('uploadLabels', labels)
    context.commit('setUpload', {'ladders': ladders, 'labels': labels})
    return fetchNetworkData(this.state.upload, this.state.cutOffValue, this.state.radioInDirect, this.state.radioTreatments)
      .then((response) => context.commit('setNetworkData', { edges: response.data.edges, nodes: response.data.nodes, treatments: response.data.treatments, cutOffValue: response.data.cutOffValue }))
      .catch((error) => {
        console.error(error)
      })  
  },
  /**
   * triggers api call to fetch grid data
   * calls setGridData to save returned data
   * @param {*} context - context
   */
  loadGridData (context) {
    return fetchGridData(this.state.upload)
      .then((response) => context.commit('setGridData', { labels: response.data.labels, laddersCols: response.data.ladders.cols, laddersRows: JSON.parse(response.data.ladders.rows), aimCols: response.data.aim.cols, aimRows: JSON.parse(response.data.aim.rows) }))
      .catch((error) => {
        console.error(error)
      })
  },
  /**
   * triggers api call to fetch ladders_example.xlsx
   * @returns ladders_example.xlsx
   */
  loadLaddersExample () {
    return fetchLaddersExample()
      .then((response) => {
        var fileURL = window.URL.createObjectURL(new Blob([response.data], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' }))
        var fileLink = document.createElement('a')
        fileLink.href = fileURL
        fileLink.setAttribute('download', 'ladders_example.xlsx')
        document.body.appendChild(fileLink)
        fileLink.click()
      })
      .catch((error) => {console.error(error)})
  },
  /**
   * triggers api call to fetch labels_example.xlsx
   * @returns labels_example.xlsx
   */
  loadLabelsExample () {
    return fetchLabelsExample()
      .then((response) => {
        var fileURL = window.URL.createObjectURL(new Blob([response.data], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' }))
        var fileLink = document.createElement('a')
        fileLink.href = fileURL
        fileLink.setAttribute('download', 'labels_example.xlsx')
        document.body.appendChild(fileLink)
        fileLink.click()
        console.log(response.data)
      })
      .catch((error) => {console.error(error)})
  },
  /**
   * triggers api call to fetch aim.csv
   * @returns aim.csv
   */
  loadAim () {
    return fetchAimDownload()
      .then((response) => {
        var fileURL = window.URL.createObjectURL(new Blob([response.data], { type: 'text/csv' }))
        var fileLink = document.createElement('a')
        fileLink.href = fileURL
        fileLink.setAttribute('download', 'aim.csv')
        document.body.appendChild(fileLink)
        fileLink.click()
        console.log(response.data)
      })
      .catch((error) => {console.error(error)})
  },

  /**
   * triggers api call to fetch data for updated vis-network
   * calls setNetworkData to save returned data
   * @param {*} context - context
   * @param {*} payload - network options
   */
  updateNetwork(context, payload) {
    context.commit('setNetworkOptions', payload)
    return fetchNetworkData(this.state.upload, this.state.cutOffValue, this.state.radioInDirect, this.state.radioTreatments)
    .then((response) => context.commit('setNetworkData', { edges: response.data.edges, nodes: response.data.nodes, treatments: response.data.treatments, cutOffValue: response.data.cutOffValue }))
    .catch((error) => {
      console.error(error)
    }) 
  }
}

/**
 * @class
 * isolated data mutations, change state of data in state
 */
const mutations = {
  /**
   * saves payload in store
   * @param {*} state - state
   * @param {*} payload - labels, ladder columns, rows and aim coumuns, rows
   */
  setGridData (state, payload) {
    state.gridLabels = payload.labels
    state.gridLaddersCols = payload.laddersCols
    state.gridLaddersRows = payload.laddersRows
    state.gridAimCols = payload.aimCols
    state.gridAimRows = payload.aimRows
  },
  setPingPong (state, payload) {
    state.pingPong = payload.pingPong
  },
  /**
   * saves payload in store
   * @param {*} state - state
   * @param {*} payload - edges, nodes, treatments, cutOffValue
   */
  setNetworkData (state, payload) {
    state.edges = payload.edges
    state.nodes = payload.nodes
    state.treatments = payload.treatments
    state.cutOffValue = payload.cutOffValue
  },
  /**
   * saves payload in store 
   * @param {*} state - state
   * @param {*} payload - cutOffValue, radioInDirect, radioTreatments
   */
  setNetworkOptions (state, payload) {
    if (payload.cutOffValue > 0)
      state.cutOffValue = payload.cutOffValue
    state.radioInDirect = payload.radioInDirect
    state.radioTreatments = payload.radioTreatments
  },
  /**
   * saves payload in store
   * @param {*} state - state
   * @param {*} payload - uploaded ladders, labels
   */
  setUpload (state, payload) {
    console.log(payload.ladders)
    state.upload.append('uploadLadders', payload.ladders)
    state.upload.append('uploadLabels', payload.labels)
  }
}

/**
 * @class
 * store date is accessed via this.$store.state.data
 */
const getters = {
  
}

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters
})

export default store
