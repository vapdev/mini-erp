<script lang="ts" setup>
import { useAuthStore } from "~/stores/useAuthStore";
definePageMeta({
    layout: "empty",
});
const form = ref({
    email: "test@example.com",
    password: "password"
});

const auth = useAuthStore();

async function handleLogin() {
    if (auth.isLoggedIn) navigateTo("/")

    const { error } = await auth.login(form.value)

    if (!error.value) {
        navigateTo("/")
    }
}
</script>

<template>
    <q-page class="flex justify-center items-center" padding>
        <div class="w-60">
            <div class="text-blue text-3xl">Mini-ERP</div>
            <PageTitle title="Login" />
            <q-form class="q-gutter-md q-mt-md" style="max-width: 500px" @submit="handleLogin">
                <q-input outlined v-model="form.email" label="E-mail" />
                <q-input outlined v-model="form.password" label="Senha" type="password" />
                <q-btn type="submit" label="Entrar" color="primary" />
            </q-form>
        </div>
    </q-page>
</template>