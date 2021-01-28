# Data

This component displays the uploaded xlsx data in a Grid layout

## Data

| Name          | Type     | Description               | Initial value                                                                                           |
| ------------- | -------- | ------------------------- | ------------------------------------------------------------------------------------------------------- |
| `colsLabels`  | `array`  | columns for labels table  | `[ { name: 'acv', id: 'acv' }, { name: 'labelcode', id: 'labelcode' }, { name: 'label', id: 'name' } ]` |
| `rowsLabels`  | `object` | rows for labels table     | `this.$store.state.gridLabels`                                                                          |
| `colsLadders` | `object` | columns for ladders table | `this.$store.state.gridLaddersCols`                                                                     |
| `rowsLadders` | `object` | rows for ladders table    | `this.$store.state.gridLaddersRows`                                                                     |



-----
## Frontend Documentation: 
* [About.vue](About.md)
* [Home.vue](Home.md)
* [Data.vue](Data.md)
* [Hvm.vue](Hvm.md)
* [api/index.js](ApiIndex.md)
* [store/index.js](StoreIndex.md)