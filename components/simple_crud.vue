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
    },
    actions: {
        type: Boolean,
        required: false,
        default: false
    },
    ativo: {
        type: Boolean,
        required: false,
        default: false
    }
})

const item_id = ref(null)

async function handleSubmit() {
    const isUpdate = !!item_id.value;
    const url = `/api/${props.api_route}${isUpdate ? `/${item_id.value}` : ''}`;
    const method = isUpdate ? 'PUT' : 'POST';

    const { error } = await useApiFetch(url, {
        method,
        body: props.modelValue
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
        fetchItems()
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
await fetchItems()

const showDialog = ref(false)
const showDeleteDialog = ref(false)
function openDeleteDialog(id) {
    showDeleteDialog.value = true
    item_id.value = id
}
function handleAddItem() {
    emit('update:modelValue', {
        ativo: true
    })
    item_id.value = null
    showDialog.value = true
}

const emit = defineEmits(['update:modelValue'])

async function editItem(evt, row) {
    const { data } = await useApiFetch(`/api/${props.api_route}/${row.id}`)
    const form = data.value.data;
    item_id.value = row.id
    emit('update:modelValue', form)
    showDialog.value = true

}

async function deleteItem() {
    const { error } = await useApiFetch(`/api/${props.api_route}/${item_id.value}`, {
        method: 'DELETE'
    })
    if (!error.value) {
        $q.notify({
            position: 'top',
            color: 'green-4',
            textColor: 'white',
            icon: 'cloud_done',
            message: 'Registro excluído com sucesso!'
        })
        fetchItems()
        showDeleteDialog.value = false
        item_id.value = null
    } else {
        $q.notify({
            position: 'top',
            color: 'red-4',
            textColor: 'white',
            icon: 'cloud_done',
            message: 'Erro ao excluir registro!'
        })
    }
}

function closeDialog() {
    item_id.value = null
    showDialog.value = false
}

const columns_ref = ref([])

onMounted(() => {
    columns_ref.value = props.columns
    if (props.ativo) {
        columns_ref.value.push({
            name: 'ativo',
            align: 'left',
            label: 'Ativo',
            field: 'ativo',
            sortable: true
        })
    }
    if (props.actions) {
        columns_ref.value.push({
            name: 'actions',
            label: 'Ações',
            field: 'actions',
            align: 'center'
        })
    }
})

</script>

<template>
    <div>
        <q-dialog v-model="showDialog">
            <q-card class="p-4 q-dialog-plugin" style="width: 50rem; max-width: 50rem;">
                <div class="text-2xl mb-4">{{ props.title }}</div>
                <q-form @submit.prevent="handleSubmit">
                    <div class="row q-gutter-sm">
                        <slot>
                        </slot>
                    </div>
                </q-form>
                <q-card-actions class="mt-5" align="right">
                    <q-btn @click="closeDialog" label="Cancelar" color="secondary" />
                    <q-btn @click="handleSubmit" type="submit" label="Salvar" color="primary" />
                </q-card-actions>
            </q-card>
        </q-dialog>

        <q-dialog v-model="showDeleteDialog">
            <q-card class="p-4 q-dialog-plugin" style="width: 876px; max-width: 80vw;">
                <div class="text-2xl mb-4">Excluir registro</div>
                <div class="text-lg mb-4">Deseja realmente excluir este registro?</div>
                <q-card-actions class="mt-5" align="right">
                    <q-btn @click="showDeleteDialog = false" label="Cancelar" color="secondary" />
                    <q-btn @click="deleteItem" type="submit" label="Excluir" color="primary" />
                </q-card-actions>
            </q-card>
        </q-dialog>

        <div class="row mb-6">
            <q-space />
            <q-btn @click="handleAddItem" label="Novo registro" color="primary" />
        </div>
        <q-table @row-click="editItem" :rows="rows" :columns="columns_ref" row-key="id">
            <template v-slot:body-cell-created_at="props">
                <q-td :props="props">
                    <div>
                        {{ formatDate(props.row.created_at) }}
                    </div>
                </q-td>
            </template>
            <template v-slot:body-cell-updated_at="props">
                <q-td :props="props">
                    <div>
                        {{ formatDate(props.row.updated_at) }}
                    </div>
                </q-td>
            </template>
            <template v-if="ativo" v-slot:body-cell-ativo="props">
                <q-td :props="props">
                    <div>
                        <q-icon size="sm" name="check" v-if="props.row.ativo" color="green" />
                        <q-icon size="sm" name="close" v-else color="red" />
                    </div>
                </q-td>
            </template>
            <template v-if="actions" v-slot:body-cell-actions="props">
                <q-td :props="props">
                    <div class="row justify-center items-center">
                        <q-icon @click.stop="openDeleteDialog(props.row.id)" size="sm" name="delete" color="red"
                            class="cursor-pointer" />
                    </div>
                </q-td>
            </template>
        </q-table>
    </div>
</template>


