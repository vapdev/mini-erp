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
        name: 'cnpj',
        align: 'left',
        label: 'CNPJ',
        field: 'cnpj',
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
    cnpj: "",
    cep: "",
    endereco: "",
    cidade_id: "",
    estado_id: "",
})

</script>

<template>
    <q-page padding>
        <PageTitle title="Fornecedores" />
        <SimpleCrud title="Fornecedores" v-model="form" :columns="columns" api_route="fornecedores">
            <q-input dense outlined v-model="form.nome" label="Nome" />
            <q-input dense outlined v-model="form.email" label="E-mail" />
            <q-input dense outlined v-model="form.telefone" label="Telefone" />
            <q-input dense outlined v-model="form.cnpj" label="CNPJ" />
            <q-input dense outlined v-model="form.endereco" label="Endereço" />
            <q-input dense outlined v-model="form.cidade_id" label="Cidade" />
            <q-input dense outlined v-model="form.estado_id" label="Estado" />
            <q-input dense outlined v-model="form.cep" label="CEP" />
        </SimpleCrud>
    </q-page>
</template>