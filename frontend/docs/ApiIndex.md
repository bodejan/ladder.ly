## Functions

<dl>
<dt><a href="#fetchGridData">fetchGridData(upload)</a> ⇒</dt>
<dd><p>api call for grid data in the correct format</p>
</dd>
<dt><a href="#fetchNetworkData">fetchNetworkData(upload, cutOffValue, radioIndirect, radioTreatments)</a> ⇒</dt>
<dd><p>api call to (re)load the vis-network/hierarchical value map</p>
</dd>
<dt><a href="#fetchLaddersExample">fetchLaddersExample()</a></dt>
<dd><p>api call to fetch ladders_example.xlsx from BE</p>
</dd>
<dt><a href="#fetchLabelsExample">fetchLabelsExample()</a></dt>
<dd><p>api call to fetch labels_example.xlsx from BE</p>
</dd>
<dt><a href="#fetchAimDownload">fetchAimDownload()</a></dt>
<dd><p>api call to fetch aim.csv from BE</p>
</dd>
</dl>

<a name="fetchGridData"></a>

## fetchGridData(upload) ⇒
api call for grid data in the correct format

**Kind**: global function  
**Returns**: grid data --> store/index.js actions.loadGridData  

| Param | Type | Description |
| --- | --- | --- |
| upload | <code>\*</code> | ladders and labels uploaded by user |

<a name="fetchNetworkData"></a>

## fetchNetworkData(upload, cutOffValue, radioIndirect, radioTreatments) ⇒
api call to (re)load the vis-network/hierarchical value map

**Kind**: global function  
**Returns**: network data --> store/index.js actions.loadNetworkData/updateNetworkData  

| Param | Type | Description |
| --- | --- | --- |
| upload | <code>\*</code> | ladders, labels |
| cutOffValue | <code>\*</code> | cutoff-value (user input/default=-1) |
| radioIndirect | <code>\*</code> | selected from of implications to be included (direct, indirect) |
| radioTreatments | <code>\*</code> | selected treatment (user input/default="All") |

<a name="fetchLaddersExample"></a>

## fetchLaddersExample()
api call to fetch ladders_example.xlsx from BE

**Kind**: global function  
<a name="fetchLabelsExample"></a>

## fetchLabelsExample()
api call to fetch labels_example.xlsx from BE

**Kind**: global function  
<a name="fetchAimDownload"></a>

## fetchAimDownload()
api call to fetch aim.csv from BE

**Kind**: global function 

-----
## Frontend Documentation: 
* [About.vue](About.md)
* [Home.vue](Home.md)
* [Data.vue](Data.md)
* [Hvm.vue](Hvm.md)
* [Aim.vue](Aim.md)
* [api/index.js](ApiIndex.md)
* [store/index.js](StoreIndex.md)