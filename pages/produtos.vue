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
        name: 'preco',
        align: 'left',
        label: 'Preço',
        field: 'preco',
        sortable: true
    },
    {
        name: 'quantidade',
        align: 'left',
        label: 'Quantidade',
        field: 'quantidade',
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
        name: 'imagem',
        align: 'left',
        label: 'Imagem',
        field: 'imagem',
        sortable: true
    },
    {
        name: 'categoria_id',
        align: 'left',
        label: 'Categoria ID',
        field: 'categoria_id',
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
    nome: "",
    preco: "",
    quantidade: "",
    descricao: "",
    imagem: "",
    categoria_id: "",
    ativo: true,
    created_at: "",
    updated_at: ""
});
</script>

<template>
    <q-page padding>
        <PageTitle title="Produtos" />
        <SimpleCrud title="Produtos" v-model="form" :columns="columns" api_route="produtos">
            <q-input dense outlined v-model="form.nome" label="Nome" />
            <q-input dense outlined v-model="form.preco" label="Preço" />
            <q-input dense outlined v-model="form.quantidade" label="Quantidade" />
            <q-input dense outlined v-model="form.descricao" label="Descrição" />
            <q-input dense outlined v-model="form.imagem" label="Imagem" />
            <q-input dense outlined v-model="form.categoria_id" label="Categoria ID" />
            <q-toggle v-model="form.ativo" label="Ativo" />
        </SimpleCrud>
    </q-page>
</template>
