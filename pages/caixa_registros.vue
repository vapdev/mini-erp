
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
    name: 'criado_em',
    align: 'left',
    label: 'Criado em',
    field: 'created_at',
    sortable: true
  },
]);

const form = ref({
  checkboxField: false, // Initialize checkbox field
  inputField: '',       // Initialize input field
  selectField: '',      // Initialize select field
  toggleField: false,   // Initialize toggle field
});
</script>

<template>
  <q-page padding>
    <PageTitle title="Registros de Caixa" />
    <div class="ml-16 row q-gutter-md">
      <div class="text-lg">
        Dia referente:
        <QInput outlined v-model="form.data" type="date" />
      </div>
      <div class="text-lg">
        Quanto entrou:
        <QInput outlined readonly v-model="form.entrada" type="number" />
      </div>
      <div class="text-lg">
        Quanto saiu:
        <QInput outlined readonly v-model="form.saida" type="number" />
      </div>
      <div class="text-lg">
        Saldo:
        <QInput outlined readonly v-model="form.saldo" type="number" />
      </div>
    </div>
    <SimpleCrud title="Novo lançamento" v-model="form" :columns="columns" api_route="caixa_registros">
      <div class="q-gutter-md">
        <div class="row q-gutter-md">
          <q-radio v-model="form.tipo" val="entrada" label="Entrada" />
          <q-radio v-model="form.tipo" val="saida" label="Saída" />
        </div>
        <div class="row q-gutter-md">
          <q-input type="number" dense outlined v-model="form.valor" label="Valor" />
        </div>
        <div class="row q-gutter-md">
          <q-input dense outlined v-model="form.descricao" label="Descrição" />
        </div>

      </div>
    </SimpleCrud>
  </q-page>
</template>
