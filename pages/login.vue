<script setup lang="ts">
definePageMeta({
    layout: "empty",
});

const email = ref('test@example.com')
const password = ref('password')

async function handleLogin() {
    await useApiFetch("/sanctum/csrf-cookie");

    await useApiFetch("/login", {
        method: "POST",
        body: JSON.stringify({
            email: email.value,
            password: password.value,
        }),
    })

    const { data } = await useApiFetch("/api/user")
}
</script>

<template>
    <q-page class="flex justify-center items-center" padding>
        <div class="w-60">
            <div class="text-blue text-3xl">Mini-ERP</div>
            <PageTitle title="Login" />
            <q-form class="q-gutter-md q-mt-md" style="max-width: 500px" @submit="handleLogin">
                <q-input outlined v-model="email" label="E-mail" />
                <q-input class="border-black" outlined v-model="password" label="Senha" type="password" />
                <q-btn type="submit" label="Entrar" color="primary" />
            </q-form>
        </div>
    </q-page>
</template>