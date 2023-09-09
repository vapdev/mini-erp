<script setup>
const $q = useQuasar()

const props = defineProps({
    api_route: {
        type: String,
        required: true
    },
    title: {
        type: String,
        required: false
    },
    add_title: {
        type: String,
        required: false,
        default: 'Novo registro'
    },
    edit_title: {
        type: String,
        required: false,
        default: 'Editar registro'
    },
    columns: {
        type: Array,
        required: true
    },
    modelValue: {
        required: true
    }
})

const item_id = ref(null)

const form = ref({})

async function handleSubmit() {
    const isUpdate = !!item_id.value;
    const url = `/api/${props.api_route}${isUpdate ? `/${item_id.value}` : ''}`;
    const method = isUpdate ? 'PUT' : 'POST';

    const { error } = await useApiFetch(url, {
        method,
        body: form.value
    })
    if (!error.value) {
        $q.notify({
            position: 'top',
            color: 'green-4',
            textColor: 'white',
            icon: 'cloud_done',
            message: 'Registro salvo com sucesso!'
        })
        closeDialog()
    } else {
        $q.notify({
            position: 'top',
            color: 'red-4',
            textColor: 'white',
            icon: 'cloud_done',
            message: 'Erro ao salvar registro!'
        })
    }
}

const rows = ref([]);

async function fetchItems() {
    const { data } = await useApiFetch(`/api/${props.api_route}`);
    rows.value = data.value.data;
}

const showDialog = ref(false)

fetchItems();

function handleAddItem() {
    emit('update:modelValue', {})
    item_id.value = null
    showDialog.value = true
}

const emit = defineEmits(['update:modelValue'])

async function editItem(evt, row) {
    const { data } = await useApiFetch(`/api/${props.api_route}/${row.id}`)
    form.value = data.value.data;
    item_id.value = row.id
    emit('update:modelValue', form.value)
    showDialog.value = true

}

function closeDialog() {
    item_id.value = null
    showDialog.value = false
}

</script>

<template>
    <div>
        <q-dialog v-model="showDialog">
            <q-card class="p-4 q-dialog-plugin" style="width: 1000px; max-width: 80vw;">
                <div class="text-2xl mb-4">{{ props.title }}</div>
                <q-form @submit.prevent="handleSubmit">
                    <div class="row q-gutter-sm">
                        <slot>
                        </slot>
                    </div>
                </q-form>
                <q-card-actions align="right">
                    <q-btn @click="closeDialog" label="Cancelar" color="secondary" />
                    <q-btn @click="handleSubmit" type="submit" label="Salvar" color="primary" />
                </q-card-actions>
            </q-card>
        </q-dialog>

        <div class="row mb-6">
            <q-space />
            <q-btn @click="handleAddItem" label="Novo registro" color="primary" />
        </div>
        <q-table @row-click="editItem" :rows="rows" :columns="props.columns" row-key="id">
        </q-table>
    </div>
</template>


