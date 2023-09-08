<script setup>
const props = defineProps({
    title: {
        type: String,
        required: true
    }
})
</script>

<template>
    <div class="text-2xl mb-4">{{ props.title }}</div>
</template>