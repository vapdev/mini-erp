
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
    <PageTitle title="Produto" />
    <SimpleCrud title="Produto" v-model="form" :columns="columns" api_route="produtos">
      <!------ SLOT DO CONTEUDO DO DIALOG ------>

      <!-- Checkbox -->
      <q-checkbox v-model="form.checkboxField" label="Checkbox Label" />
      <!-- Input -->
      <q-input v-model="form.inputField" label="Input Label" />
      <!-- Select -->
      <q-select v-model="form.selectField" label="Select Label" :options="['Option 1', 'Option 2', 'Option 3']" />
      <!-- Toggle -->
      <q-toggle v-model="form.toggleField" label="Toggle Label" />

      <!------ SLOT DO CONTEUDO DO DIALOG ------>
    </SimpleCrud>
  </q-page>
</template>
