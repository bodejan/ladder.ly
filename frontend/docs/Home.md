# Home

This component represents the home/landing page, where the xlsx data is uploaded

## Data

| Name      | Type   | Description           | Initial value |
| --------- | ------ | --------------------- | ------------- |
| `ladders` | `xlsx` | save uploaded ladders | `null`        |
| `labels`  | `xlsx` | save uploaded labels  | `null`        |

## Methods

### pingPong()

used for testing purposes only

**Syntax**

```typescript
pingPong(): void
```

### submitFile()

submit uploaded files to store, then push /hvm

**Syntax**

```typescript
submitFile(): void
```

### requestLabelsExample()

request example labels for download

**Syntax**

```typescript
requestLabelsExample(): void
```

### requestLaddersExample()

request example ladders for download

**Syntax**

```typescript
requestLaddersExample(): void
```

-----
## Frontend Documentation: 
* [About.vue](About.md)
* [Home.vue](Home.md)
* [Data.vue](Data.md)
* [Hvm.vue](Hvm.md)
* [Aim.vue](Aim.md)
* [api/index.js](ApiIndex.md)
* [store/index.js](StoreIndex.md)
