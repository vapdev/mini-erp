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
        name: 'descricao',
        align: 'left',
        label: 'Descrição',
        field: 'descricao',
        sortable: true
    },
    {
        name: 'valor',
        align: 'left',
        label: 'Valor',
        field: 'valor',
        sortable: true
    },
    {
        name: 'data_vencimento',
        align: 'left',
        label: 'Data de Vencimento',
        field: 'data_vencimento',
        sortable: true
    },
    {
        name: 'data_pagamento',
        align: 'left',
        label: 'Data de Pagamento',
        field: 'data_pagamento',
        sortable: true
    },
    {
        name: 'cliente_id',
        align: 'left',
        label: 'Cliente ID',
        field: 'cliente_id',
        sortable: true
    },
    {
        name: 'created_at',
        align: 'left',
        label: 'Criado em',
        field: 'created_at',
        sortable: true
    },
    {
        name: 'updated_at',
        align: 'left',
        label: 'Atualizado em',
        field: 'updated_at',
        sortable: true
    },
    {
        name: 'actions',
        label: 'Ações',
        field: 'actions'
    }
]);

const form = ref({
    id: "",
    descricao: "",
    valor: "",
    data_vencimento: "",
    data_pagamento: null,
    cliente_id: "",
    created_at: "",
    updated_at: ""
});
</script>

<template>
    <q-page padding>
        <PageTitle title="Contas a Receber" />
        <SimpleCrud title="Contas a Receber" v-model="form" :columns="columns" api_route="contas-receber">
            <q-input dense outlined v-model="form.descricao" label="Descrição" />
            <q-input dense outlined v-model="form.valor" label="Valor" />
            <q-date v-model="form.data_vencimento" label="Data de Vencimento" />
            <q-date v-model="form.data_pagamento" label="Data de Pagamento" />
            <q-input dense outlined v-model="form.cliente_id" label="Cliente ID" />
        </SimpleCrud>
    </q-page>
</template>
