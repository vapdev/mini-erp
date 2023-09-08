<script setup>
const props = defineProps({
    title: {
        type: String,
        required: true
    }
})
</script>

<template>
    <span class="text-2xl">{{ props.title }}</span>
</template>