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
        field: 'actions',
        align: 'center'
    }
]);

const form = ref({
    id: "",
    nome: "",
    ativo: true,
    created_at: "",
    updated_at: ""
});
</script>

<template>
    <q-page padding>
        <PageTitle title="Categorias" />
        <SimpleCrud title="Categorias" v-model="form" :columns="columns" api_route="categorias">
            <q-input dense outlined v-model="form.nome" label="Nome" />
            <q-toggle v-model="form.ativo" label="Ativo" />
        </SimpleCrud>
    </q-page>
</template>
