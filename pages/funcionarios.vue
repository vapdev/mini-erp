<script setup>
const columns = ref([
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
        name: 'rua',
        align: 'left',
        label: 'Rua',
        field: 'rua',
        sortable: true
    },
    {
        name: 'numero',
        align: 'left',
        label: 'Número',
        field: 'numero',
        sortable: true
    },
    {
        name: 'bairro',
        align: 'left',
        label: 'Bairro',
        field: 'bairro',
        sortable: true
    },
    {
        name: 'complemento',
        align: 'left',
        label: 'Complemento',
        field: 'complemento',
        sortable: true
    },
    {
        name: 'cidade',
        align: 'left',
        label: 'Cidade',
        field: 'cidade',
        sortable: true
    },
    {
        name: 'estado',
        align: 'left',
        label: 'Estado',
        field: 'estado',
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
        name: 'sexo',
        align: 'left',
        label: 'Sexo',
        field: 'sexo',
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
        name: 'user_id',
        align: 'left',
        label: 'User ID',
        field: 'user_id',
        sortable: true
    },
    {
        name: 'actions',
        label: 'Ações',
        field: 'actions'
    }
])

const form = ref({
    id: "",
    nome: "",
    email: "",
    telefone: "",
    cpf: "",
    rua: "",
    numero: "",
    bairro: "",
    complemento: "",
    cidade: "",
    estado: "",
    cargo: "",
    salario: "",
    sexo: "",
    data_nascimento: "",
    data_admissao: "",
    data_demissao: "",
    status: "",
    observacoes: "",
    user_id: ""
})
</script>

<template>
    <q-page padding>
        <PageTitle title="Funcionários" /> 
        <SimpleCrud title="Funcionários" v-model="form" :columns="columns" api_route="funcionarios">
            <q-input dense outlined v-model="form.nome" label="Nome" />
            <q-input dense outlined v-model="form.email" label="E-mail" />
            <q-input dense outlined v-model="form.telefone" label="Telefone" />
            <q-input dense outlined v-model="form.cpf" label="CPF" />
            <q-input dense outlined v-model="form.rua" label="Rua" />
            <q-input dense outlined v-model="form.numero" label="Número" />
            <q-input dense outlined v-model="form.bairro" label="Bairro" />
            <q-input dense outlined v-model="form.complemento" label="Complemento" />
            <q-input dense outlined v-model="form.cidade" label="Cidade" />
            <q-input dense outlined v-model="form.estado" label="Estado" />
            <q-input dense outlined v-model="form.cargo" label="Cargo" />
            <q-input dense outlined v-model="form.salario" label="Salário" />
            <q-input dense outlined v-model="form.sexo" label="Sexo" />
            <q-input dense outlined v-model="form.data_nascimento" label="Data de Nascimento" />
            <q-input dense outlined v-model="form.data_admissao" label="Data de Admissão" />
            <q-input dense outlined v-model="form.data_demissao" label="Data de Demissão" />
            <q-input dense outlined v-model="form.status" label="Status" />
            <q-input dense outlined v-model="form.observacoes" label="Observações" />
            <q-input dense outlined v-model="form.user_id" label="User ID" />
        </SimpleCrud>
    </q-page>
</template>
