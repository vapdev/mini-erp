<script setup>
const props = defineProps({
    modelValue: {
        type: String,
        required: true
    },
    model: {
        type: String,
        required: true
    },
    option_label: {
        type: String,
        default: 'nome'
    }
})

const emit = defineEmits(['update:modelValue'])
const options = ref([])
const selectedObj = ref(null)

onMounted(async () => {
    if (props.modelValue) {
        const { data } = await useApiFetch(`/api/${props.model}/${props.modelValue}`);
        selectedObj.value = data.value.data;
    }
    const { data } = await useApiFetch(`/api/${props.model}`);
    options.value = data.value.data;
})

watch(selectedObj, (value) => {
    if (value) {
        emit('update:modelValue', value.id)
    }
})

</script>

<template>
    <q-select outlined :option-label="option_label"  v-model="selectedObj" :options="options" />
</template>