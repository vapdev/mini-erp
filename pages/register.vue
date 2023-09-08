<script setup>
definePageMeta({
    layout: "empty",
});
import { useAuthStore } from "~/stores/useAuthStore";

const form = ref({
    name: "",
    email: "",
    password: "",
    password_confirmation: ""
});

const auth = useAuthStore();

async function handleRegister() {
    const { error } = await auth.register(form.value);
    if (!error.value) {
        navigateTo("/");
    }
}
</script>

<template>
    <q-page class="flex justify-center items-center" padding>
        <div class="w-60">
            <div class="text-blue text-3xl">Mini-ERP</div>
            <PageTitle title="Registrar usuário" />
            <q-form class="q-gutter-md q-mt-md" style="max-width: 500px" @submit="register">
                <q-input outlined v-model="form.name" label="Nome" />
                <q-input outlined v-model="form.email" label="E-mail" />
                <q-input outlined v-model="form.password" label="Senha" type="password" />
                <q-input outlined v-model="form.password_confirmation" label="Confirmação de senha" type="password" />
                <q-btn type="submit" label="Cadastrar" color="primary" />
            </q-form>
        </div>
    </q-page>
</template>