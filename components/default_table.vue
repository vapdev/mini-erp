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

const emit = defineEmits([
    'row-click'
])

function handleRowClick(evt, row) {
    emit('row-click', row)
}
</script>

<template>
    <q-table @row-click="handleRowClick" :title="title" :rows="rows" :columns="columns" :row-key="rowKey" />
</template>