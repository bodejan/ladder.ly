## Classes

<dl>
<dt><a href="#state">state</a></dt>
<dd><p>source of data</p>
</dd>
<dt><a href="#actions">actions</a></dt>
<dd><p>asynchronous operations</p>
</dd>
<dt><a href="#mutations">mutations</a></dt>
<dd><p>isolated data mutations, change state of data in state</p>
</dd>
<dt><a href="#getters">getters</a></dt>
<dd><p>store date is accessed via this.$store.state.data</p>
</dd>
</dl>

<a name="state"></a>

## state
source of data

**Kind**: global class  

* [state](#state)
    * [.gridLabels](#state.gridLabels)
    * [.gridLaddersCols](#state.gridLaddersCols)
    * [.gridLaddersRows](#state.gridLaddersRows)
    * [.upload](#state.upload)
    * [.cutOffValue](#state.cutOffValue)
    * [.radioInDirect](#state.radioInDirect)
    * [.treatments](#state.treatments)
    * [.radioTreatments](#state.radioTreatments)

<a name="state.gridLabels"></a>

### state.gridLabels
labels needed for the grid layout, to visualize uploaded data

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.gridLaddersCols"></a>

### state.gridLaddersCols
ladder columns needed for the grid layout, to visualize uploaded data

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.gridLaddersRows"></a>

### state.gridLaddersRows
ladder rows needed for the grid layout, to visualize uploaded data

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.upload"></a>

### state.upload
uploaded ladders, labels

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.cutOffValue"></a>

### state.cutOffValue
cutOffValue default -1

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.radioInDirect"></a>

### state.radioInDirect
indicates selected radio button in hvm

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.treatments"></a>

### state.treatments
possible treatments

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.radioTreatments"></a>

### state.radioTreatments
default selected treatment

**Kind**: static property of [<code>state</code>](#state)  
<a name="actions"></a>

## actions
asynchronous operations

**Kind**: global class  

* [actions](#actions)
    * [.loadNetworkData(context, upload)](#actions.loadNetworkData)
    * [.loadGridData(context)](#actions.loadGridData)
    * [.loadLaddersExample()](#actions.loadLaddersExample) ⇒
    * [.loadLabelsExample()](#actions.loadLabelsExample) ⇒
    * [.updateNetwork(context, payload)](#actions.updateNetwork)

<a name="actions.loadNetworkData"></a>

### actions.loadNetworkData(context, upload)
triggers api call to fetch initial vis-network data from BE, safes upload
calls setNetworkData to save returned data in state

**Kind**: static method of [<code>actions</code>](#actions)  

| Param | Type | Description |
| --- | --- | --- |
| context | <code>\*</code> | context |
| upload | <code>\*</code> | uploaded xlsx ladders, labels |

<a name="actions.loadGridData"></a>

### actions.loadGridData(context)
triggers api call to fetch grid data
calls setGridData to save returned data

**Kind**: static method of [<code>actions</code>](#actions)  

| Param | Type | Description |
| --- | --- | --- |
| context | <code>\*</code> | context |

<a name="actions.loadLaddersExample"></a>

### actions.loadLaddersExample() ⇒
triggers api call to fetch ladders_example.xlsx

**Kind**: static method of [<code>actions</code>](#actions)  
**Returns**: ladders_example.xlsx  
<a name="actions.loadLabelsExample"></a>

### actions.loadLabelsExample() ⇒
triggers api call to fetch labels_example.xlsx

**Kind**: static method of [<code>actions</code>](#actions)  
**Returns**: labels_example.xlsx  
<a name="actions.updateNetwork"></a>

### actions.updateNetwork(context, payload)
triggers api call to fetch data for updated vis-network
calls setNetworkData to save returned data

**Kind**: static method of [<code>actions</code>](#actions)  

| Param | Type | Description |
| --- | --- | --- |
| context | <code>\*</code> | context |
| payload | <code>\*</code> | network options |

<a name="mutations"></a>

## mutations
isolated data mutations, change state of data in state

**Kind**: global class  

* [mutations](#mutations)
    * [.setGridData(state, payload)](#mutations.setGridData)
    * [.setNetworkData(state, payload)](#mutations.setNetworkData)
    * [.setNetworkOptions(state, payload)](#mutations.setNetworkOptions)
    * [.setUpload(state, payload)](#mutations.setUpload)

<a name="mutations.setGridData"></a>

### mutations.setGridData(state, payload)
saves payload in store

**Kind**: static method of [<code>mutations</code>](#mutations)  

| Param | Type | Description |
| --- | --- | --- |
| state | <code>\*</code> | state |
| payload | <code>\*</code> | labels, ladder columns, rows |

<a name="mutations.setNetworkData"></a>

### mutations.setNetworkData(state, payload)
saves payload in store

**Kind**: static method of [<code>mutations</code>](#mutations)  

| Param | Type | Description |
| --- | --- | --- |
| state | <code>\*</code> | state |
| payload | <code>\*</code> | edges, nodes, treatments, cutOffValue |

<a name="mutations.setNetworkOptions"></a>

### mutations.setNetworkOptions(state, payload)
saves payload in store

**Kind**: static method of [<code>mutations</code>](#mutations)  

| Param | Type | Description |
| --- | --- | --- |
| state | <code>\*</code> | state |
| payload | <code>\*</code> | cutOffValue, radioInDirect, radioTreatments |

<a name="mutations.setUpload"></a>

### mutations.setUpload(state, payload)
saves payload in store

**Kind**: static method of [<code>mutations</code>](#mutations)  

| Param | Type | Description |
| --- | --- | --- |
| state | <code>\*</code> | state |
| payload | <code>\*</code> | uploaded ladders, labels |

<a name="getters"></a>

## getters
store date is accessed via this.$store.state.data

**Kind**: global class


-----
## Frontend Documentation: 
* [About.vue](About.md)
* [Home.vue](Home.md)
* [Data.vue](Data.md)
* [Hvm.vue](Hvm.md)
* [api/index.js](ApiIndex.md)
* [store/index.js](StoreIndex.md)