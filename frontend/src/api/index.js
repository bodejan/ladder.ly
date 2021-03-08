import axios from 'axios'
// axios.defaults.headers.post['Content-Type'] = 'application/json'
axios.defaults.baseURL = 'http://127.0.0.1:5000/'

/**
 * api call for grid data in the correct format
 * @param {*} upload - ladders and labels uploaded by user
 * @returns grid data --> store/index.js actions.loadGridData 
 */
export function fetchGridData (upload) {
  return axios.post(`${'grid_data'}`,upload, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}
/**
 * api call to (re)load the vis-network/hierarchical value map
 * @param {*} upload - ladders, labels 
 * @param {*} cutOffValue - cutoff-value (user input/default=-1)
 * @param {*} radioIndirect  - selected from of implications to be included (direct, indirect) 
 * @param {*} radioTreatments - selected treatment (user input/default="All")
 * @returns network data --> store/index.js actions.loadNetworkData/updateNetworkData
 */
export function fetchNetworkData (upload, cutOffValue, radioIndirect, radioTreatments) {
  return axios.post(`network_data/${cutOffValue}/${radioIndirect}/${radioTreatments}`,upload, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}
export function fetchPingPong (input) {
  return axios.post(`${'ping'}`, {name: input})
}
/**
 * api call to fetch ladders_example.xlsx from BE
 */
export function fetchLaddersExample () {
  return axios.get(`${'ladders_example'}`, {
    responseType: 'blob',
  })
}
/**
 * api call to fetch labels_example.xlsx from BE
 */
export function fetchLabelsExample () {
  return axios.get(`${'labels_example'}`, {
    responseType: 'blob',
    
  })
}
/**
 * 
 * api call to fetch aim.csv from BE
 */
export function fetchAimDownload () {
  return axios.get(`${'get_aim'}`, {
    responseType: 'blob',
    
  })
}