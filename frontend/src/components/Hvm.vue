<template>
<v-container>
    <h1>Interactive Hierarchical Value Map</h1>
    <v-divider class="pa-4"></v-divider>
    <div id="mynetwork"></div>
    <div id="networkOptions"></div>
    <div>
    </div>
     <v-divider class="pa-4"></v-divider>
    <v-card class="pa-4">
        <v-card-title>Configure your hierarchical value map</v-card-title>
        <v-row>
            <v-col
                cols="12"
                sm="6"
                md="3"
            >select a cut-off-value
            (currently selected: {{this.$store.state.cutOffValue}}):
            </v-col>
            <v-col
                cols="12"
                sm="6"
                md="3"
            >select implications:
            </v-col>
            <v-col
                cols="12"
                sm="6"
                md="3"
            >select treatment:
            </v-col>
        
        </v-row>
        <v-row>
            <v-col
                cols="12"
                sm="6"
                md="3"
            >
                <v-text-field
                    label="Cutoff-Value"
                    v-model="cutOffValue"
                ></v-text-field>
            </v-col>
            <v-col
                cols="12"
                sm="6"
                md="3"
            >
                <v-radio-group v-model="radioInDirect">
                    <v-radio
                        label="only direct implications"
                        key="direct"
                        value="direct"
                    ></v-radio>
                    <v-radio
                        label="direct and indirect implications"
                        key="indirect"
                        value="indirect"
                    ></v-radio>
                </v-radio-group>
            </v-col>
            <v-col
                cols="12"
                sm="6"
                md="3"
            >
                <v-radio-group v-model="radioTreatments">
                    <v-radio
                        label="All"
                        key="All"
                        value="All"
                    ></v-radio>
                    <v-radio
                        v-for="n in this.$store.state.treatments"
                        :key="n"
                        :label="n"
                        :value="n"
                    ></v-radio>
                </v-radio-group>
            </v-col>
            <v-col
                cols="12"
                sm="6"
                md="3"
            >
                <v-btn 
                    outlined style="margin-bottom: 3px"
                    @click="reload()">
                    Submit
                </v-btn>
            </v-col>

        </v-row>
    </v-card>

</v-container>
</template>

<script>

import vis from 'vis'
import "vis-network/styles/vis-network.css"
/**
 * This component displays the interactive hierarchical value map
 */
export default {
    data() {
        return {
            /**select whether to include direct or direct and indirect implications */
            radioInDirect: this.$store.state.radioInDirect,
            /**select treatments, treatments are stored in store*/
            radioTreatments: this.$store.state.radioTreatments,
            /**used to update cutOffValue in store */
            cutOffValue: "",
            /**nodes to initialize the network */
            nodes: this.$store.state.nodes,
            /**edges to initialize the network */
            edges: this.$store.state.edges,
            /**options for the network, hierarchical layout, custom shapes for ACV's etc. */
            options: {
                    autoResize: true,
                    height: '100%',
                    width: '100%',
                nodes: {
                    borderWidth: 4
                },
                configure: {
                    enabled: false,
                    filter: 'nodes,edges',
                    showButton: true
                },
                edges: {
                    color: 'lightgray',
                    arrows: {
                        to: {
                            enabled: true,
                            type: "arrow"
                        }
                    }

                },
                layout: {
                    hierarchical: {
                        enabled: true,
                        levelSeparation: 250,
                        nodeSpacing: 300,
                        parentCentralization: true
                    }
                },
                physics: {
                    enabled: false
                },
                groups: {
                    values: {
                        shape: 'circle'

                    },
                    consequences: {
                        shape: 'triangle'
                    },
                    attributes: {
                        shape: 'square'
                    }
                }
            },
            /**container for vis-network */
            container: '',
            /**initialize network, create on mounted */
            network: null
        }
    },
    methods: {
        /**reload network with selected cutOffValue, radioInDirect, radioTreatments */
        reload() {
            //not exactly elegant but works
            this.$store.dispatch('updateNetwork', {cutOffValue: this.cutOffValue, radioInDirect: this.radioInDirect, radioTreatments: this.radioTreatments})
                .then(() => this.$router.push('/home'))
                .then(() => this.$router.push('/hvm'))

        }
    }, 
    components: {
        
    },
    computed: {
        /**create graph/network data based on the values stored in store, used to create the network with container and options */
        graph_data() {
            return {
                nodes: this.$store.state.nodes,
                edges: this.$store.state.edges
            }
        }
    },
    /**create network with container, graph_data and options */
    mounted() {
        this.container = document.getElementById('mynetwork');
        this.network = new vis.Network(this.container, this.graph_data, this.options);
    }
}
</script>

<style scoped>
    #mynetwork {
        border-radius: 25px;
        border: 2px solid #000000;
        height: 800px;
        width: 100%;
    }
</style>