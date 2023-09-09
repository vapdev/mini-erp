<script setup>

const $q = useQuasar()

defineEmits([
    ...useDialogPluginComponent.emits,
])

const { dialogRef, onDialogHide, onDialogOK, onDialogCancel } = useDialogPluginComponent()

const props = defineProps({
    title: {
        type: String,
        required: true
    },
    funcionario_id: {
        type: Number,
    }
})

const form = ref({
    nome: "",
    email: "",
    telefone: "",
    cpf: "",
    endereco: "",
    cidade_id: "",
    estado_id: "",
    cep: "",
    cargo: "",
    salario: "",
    data_nascimento: "",
    data_admissao: "",
    data_demissao: "",
    status: "",
    observacoes: "",
    usuario_id: "",
})

onMounted(async () => {
    if (props.funcionario_id) {
        const { data } = await useApiFetch(`/api/funcionarios/${props.funcionario_id}`)
        form.value = data.value.data;
    }
})

async function handleSalvar() {
    const isUpdate = !!props.funcionario_id;
    const url = `/api/funcionarios${isUpdate ? `/${props.funcionario_id}` : ''}`;
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
            message: 'Funcionário salvo com sucesso!'
        })
        onDialogOK()
    } else {
        $q.notify({
            position: 'top',
            color: 'red-4',
            textColor: 'white',
            icon: 'cloud_done',
            message: 'Erro ao salvar funcionário!'
        })
    }
}

</script>

<template>
    <q-dialog ref="dialogRef" @hide="onDialogHide">
        <q-card class="p-4 q-dialog-plugin" style="width: 1000px; max-width: 80vw;">
            <div class="text-2xl mb-4">{{ props.title }}</div>
            <q-form @submit.prevent="handleSalvar">
                <div class="row q-gutter-sm">
                    <q-input outlined v-model="form.nome" label="Nome" />
                    <q-input outlined v-model="form.email" label="E-mail" />
                    <q-input outlined v-model="form.telefone" label="Telefone" />
                    <q-input outlined v-model="form.cpf" label="CPF" />
                    <q-input outlined v-model="form.endereco" label="Endereço" />
                    <q-input outlined v-model="form.cidade_id" label="Cidade" />
                    <q-input outlined v-model="form.estado_id" label="Estado" />
                    <q-input outlined v-model="form.cep" label="CEP" />
                    <q-input outlined v-model="form.cargo" label="Cargo" />
                    <q-input outlined v-model="form.salario" label="Salário" />
                    <q-input outlined v-model="form.data_nascimento" label="Data de nascimento" />
                    <q-input outlined v-model="form.data_admissao" label="Data de admissão" />
                    <q-input outlined v-model="form.data_demissao" label="Data de demissão" />
                    <q-input outlined v-model="form.status" label="Status" />
                    <q-input outlined v-model="form.observacoes" label="Observações" />
                    <q-input outlined v-model="form.usuario_id" label="Usuário" />
                </div>
            </q-form>
            <q-card-actions align="right">
                <q-btn @click="onDialogCancel" label="Cancelar" color="secondary" />
                <q-btn @click="handleSalvar" type="submit" label="Salvar" color="primary" />
            </q-card-actions>
        </q-card>
    </q-dialog>
</template>


