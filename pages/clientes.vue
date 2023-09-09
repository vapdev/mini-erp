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
        name: 'endereco',
        align: 'left',
        label: 'Endereço',
        field: 'endereco',
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
]);

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

</script>

<template>
    <q-page padding>
        <PageTitle title="Clientes" />
        <SimpleCrud title="Clientes" v-model="form" :columns="columns" api_route="clientes">
            <q-input dense outlined v-model="form.nome" label="Nome" />
            <q-input dense outlined v-model="form.email" label="E-mail" />
            <q-input dense outlined v-model="form.telefone" label="Telefone" />
            <q-input dense outlined v-model="form.cpf" label="CPF" />
            <q-input dense outlined v-model="form.endereco" label="Endereço" />
            <q-input dense outlined v-model="form.cidade_id" label="Cidade" />
            <q-input dense outlined v-model="form.estado_id" label="Estado" />
            <q-input dense outlined v-model="form.cep" label="CEP" />
            <q-input dense outlined v-model="form.cargo" label="Cargo" />
            <q-input dense outlined v-model="form.salario" label="Salário" />
            <q-input dense outlined v-model="form.data_nascimento" label="Data de nascimento" />
            <q-input dense outlined v-model="form.data_admissao" label="Data de admissão" />
            <q-input dense outlined v-model="form.data_demissao" label="Data de demissão" />
            <q-input dense outlined v-model="form.status" label="Status" />
            <q-input dense outlined v-model="form.observacoes" label="Observações" />
            <q-input dense outlined v-model="form.usuario_id" label="Usuário" />
        </SimpleCrud>
    </q-page>
</template>