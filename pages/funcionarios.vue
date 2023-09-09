<script setup>
const columns = [
    {
        name: 'id',
        required: true,
        label: 'ID',
        align: 'left',
        field: 'id',
        sortable: true
    },
    {
        name: 'nome',
        align: 'left',
        label: 'Nome',
        field: 'nome',
        sortable: true
    },
    {
        name: 'email',
        align: 'left',
        label: 'Email',
        field: 'email',
        sortable: true
    },
    {
        name: 'telefone',
        align: 'left',
        label: 'Telefone',
        field: 'telefone',
        sortable: true
    },
    {
        name: 'cpf',
        align: 'left',
        label: 'CPF',
        field: 'cpf',
        sortable: true
    },
    {
        name: 'endereco',
        align: 'left',
        label: 'Endereço',
        field: 'endereco',
        sortable: true
    },
    {
        name: 'cidade_id',
        align: 'left',
        label: 'Cidade ID',
        field: 'cidade_id',
        sortable: true
    },
    {
        name: 'estado_id',
        align: 'left',
        label: 'Estado ID',
        field: 'estado_id',
        sortable: true
    },
    {
        name: 'cep',
        align: 'left',
        label: 'CEP',
        field: 'cep',
        sortable: true
    },
    {
        name: 'cargo',
        align: 'left',
        label: 'Cargo',
        field: 'cargo',
        sortable: true
    },
    {
        name: 'salario',
        align: 'left',
        label: 'Salário',
        field: 'salario',
        sortable: true
    },
    {
        name: 'data_nascimento',
        align: 'left',
        label: 'Data de Nascimento',
        field: 'data_nascimento',
        sortable: true
    },
    {
        name: 'data_admissao',
        align: 'left',
        label: 'Data de Admissão',
        field: 'data_admissao',
        sortable: true
    },
    {
        name: 'data_demissao',
        align: 'left',
        label: 'Data de Demissão',
        field: 'data_demissao',
        sortable: true
    },
    {
        name: 'status',
        align: 'left',
        label: 'Status',
        field: 'status',
        sortable: true
    },
    {
        name: 'observacoes',
        align: 'left',
        label: 'Observações',
        field: 'observacoes',
        sortable: true
    },
    {
        name: 'usuario_id',
        align: 'left',
        label: 'Usuário ID',
        field: 'usuario_id',
        sortable: true
    }
];

const rows = ref([]);

async function fetchFuncionarios() {
    const { data } = await useApiFetch('/api/funcionarios');
    rows.value = data.value.data;
}

fetchFuncionarios();

const $q = useQuasar()
import { FuncionarioDialog } from '#components'

function handleAddFuncionario() {
    $q.dialog({
        component: FuncionarioDialog,
        componentProps: {
            title: 'Adicionar funcionário'
        }
    }).onOk(() => {
        fetchFuncionarios()
    })
}

function openDialog(row) {
    $q.dialog({
        component: FuncionarioDialog,
        componentProps: {
            title: 'Editar funcionário',
            funcionario_id: row.id
        }
    }).onOk(() => {
        fetchFuncionarios()
    })
}

</script>

<template>
    <q-page padding>
        <PageTitle title="Funcionários" />
        <div class="row mb-6">
            <q-space />
            <q-btn @click="handleAddFuncionario" label="Novo funcionário" color="primary" />
        </div>
        <DefaultTable @row-click="openDialog" :columns="columns" :rows="rows" />
    </q-page>
</template>