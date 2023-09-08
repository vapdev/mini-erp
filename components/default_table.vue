<script setup>
const props = defineProps({
    rows: {
        type: Array,
        required: true
    },
    columns: {
        type: Array,
        required: true
    },
    title: {
        type: String,
        default: ''
    },
    rowKey: {
        type: String,
        default: 'id'
    }
})
</script>

<template>
    <q-table :title="title" :rows="rows" :columns="columns" :row-key="rowKey" />
</template>