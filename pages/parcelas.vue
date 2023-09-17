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
        name: 'origem_id',
        align: 'left',
        label: 'Origem ID',
        field: 'origem_id',
        sortable: true
    },
    {
        name: 'origem',
        align: 'left',
        label: 'Origem',
        field: 'origem',
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
        name: 'valor',
        align: 'left',
        label: 'Valor',
        field: 'valor',
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
    origem_id: "",
    origem: "",
    data_vencimento: "",
    data_pagamento: null,
    valor: "",
    created_at: "",
    updated_at: ""
});
</script>

<template>
    <q-page padding>
        <PageTitle title="Parcelas" />
        <SimpleCrud title="Parcelas" v-model="form" :columns="columns" api_route="parcelas">
            <q-input dense outlined v-model="form.origem_id" label="Origem ID" />
            <q-input dense outlined v-model="form.origem" label="Origem" />
            <q-date v-model="form.data_vencimento" label="Data de Vencimento" />
            <q-date v-model="form.data_pagamento" label="Data de Pagamento" />
            <q-input dense outlined v-model="form.valor" label="Valor" />
        </SimpleCrud>
    </q-page>
</template>
