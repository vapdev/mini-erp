<script setup>
definePageMeta({
    layout: "empty",
});
</script>

<template>
    <q-page class="flex justify-center items-center" padding>
        <div class="w-60">
            <div class="text-blue text-3xl">Mini-ERP</div>
            <PageTitle title="Registrar usuário" />
            <q-form class="q-gutter-md q-mt-md" style="max-width: 500px" @submit="register">
                <q-input outlined v-model="name" label="Nome" />
                <q-input outlined v-model="email" label="E-mail" />
                <q-input outlined v-model="password" label="Senha" type="password" />
                <q-input outlined v-model="passwordConfirmation" label="Confirmação de senha" type="password" />
                <q-btn type="submit" label="Cadastrar" color="primary" />
            </q-form>
        </div>
    </q-page>
</template>