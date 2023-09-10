
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
    name: 'descricao',
    align: 'left',
    label: 'Descrição',
    field: 'descricao',
  },
  {
    name: 'status',
    align: 'left',
    label: 'Status',
    field: 'status',
    sortable: true
  },
  {
    name: 'criado_em',
    align: 'left',
    label: 'Criado em',
    field: 'created_at',
    sortable: true
  },
]);

const form = ref({
  nome: '',
  descricao: '',
  status: '',
});
</script>

<template>
  <q-page padding>
    <PageTitle title="Caixas" />
    <SimpleCrud title="Caixa" v-model="form" :columns="columns" api_route="caixas">
      <div class="row">
        <div class="row q-gutter-md">
          <q-input dense outlined v-model="form.nome" label="Nome" />
          <q-input dense outlined v-model="form.descricao" label="Descrição" />
          <q-toggle v-model="form.status" label="Status" />
        </div>
      </div>
    </SimpleCrud>
  </q-page>
</template>
