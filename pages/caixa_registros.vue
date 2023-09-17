
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
        name: 'tipo',
        align: 'left',
        label: 'Tipo',
        field: 'tipo',
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
        name: 'caixa_id',
        align: 'left',
        label: 'Caixa ID',
        field: 'caixa_id',
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
        name: 'a_prazo',
        align: 'left',
        label: 'À Prazo',
        field: 'a_prazo',
        sortable: true
    },
    {
        name: 'forma_pagamento_id',
        align: 'left',
        label: 'Forma de Pagamento ID',
        field: 'forma_pagamento_id',
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
