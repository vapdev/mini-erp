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
        name: 'ativo',
        align: 'left',
        label: 'Ativo',
        field: 'ativo',
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
    ativo: true,
    created_at: "",
    updated_at: ""
});
</script>

<template>
    <q-page padding>
        <PageTitle title="Formas de Pagamento" />
        <SimpleCrud title="Formas de Pagamento" v-model="form" :columns="columns" api_route="formas-pagamento">
            <q-input dense outlined v-model="form.descricao" label="Descrição" />
            <q-toggle v-model="form.ativo" label="Ativo" />
        </SimpleCrud>
    </q-page>
</template>
