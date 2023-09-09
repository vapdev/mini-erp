<script setup>
import { useAuthStore } from "~/stores/useAuthStore";
const drawerLeft = ref(true)
const drawerRight = ref(false)
const menuList = [
    {
        icon: 'dashboard',
        label: 'Dashboard',
        to: '/',
        separator: false
    },
    {
        icon: 'mdi-chart-bar',
        label: 'Relatórios',
        to: '/relatorios',
        separator: true
    },
    {
        icon: 'mdi-cart-plus',
        label: 'Vender',
        to: '/vender',
        separator: false
    },
    {
        icon: 'mdi-cart-arrow-down',
        label: 'Comprar',
        to: '/comprar',
        separator: false
    },
    {
        icon: 'mdi-package-variant-closed',
        label: 'Estoque',
        to: '/estoque',
        separator: true
    },
    {
        icon: 'mdi-cash-minus',
        label: 'Contas a pagar',
        to: '/contas_pagar',
        separator: false
    },
    {
        icon: 'mdi-cash-plus',
        label: 'Contas a receber',
        to: '/contas_receber',
        separator: false
    },
    {
        icon: 'mdi-cash-register',
        label: 'Caixa',
        to: '/caixa',
        separator: true
    },
    {
        icon: 'mdi-account-group',
        label: 'Funcionários',
        to: '/funcionarios',
        separator: false
    },
    {
        icon: 'mdi-account-group',
        label: 'Fornecedores',
        to: '/fornecedores',
        separator: false
    },
    {
        icon: 'mdi-account-group',
        label: 'Clientes',
        to: '/clientes',
        separator: true
    },
    {
        icon: 'settings',
        label: 'Configurações',
        to: '/configuracoes',
        separator: false
    },
]
const auth = useAuthStore();
async function handleLogout() {
    await auth.logout();
}
const send = () => {

}

</script>

<template>
    <q-layout view="hHr lpR fFr" container style="height: 100vh" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-3'">

        <!-- HEADER -->
        <q-header reveal :class="$q.dark.isActive ? 'bg-secondary' : 'bg-black'">
            <q-toolbar>
                <q-btn flat @click="drawerLeft = !drawerLeft" round dense icon="menu" />
                <q-toolbar-title>Mini-ERP</q-toolbar-title>
                <q-btn flat @click="drawerRight = !drawerRight" round dense icon="mdi-chat" />
            </q-toolbar>
        </q-header>
        <!-- END HEADER -->

        <!-- FOOTER -->
        <q-footer>
            <q-toolbar>
                <q-toolbar-title>Mini-ERP. Todos direitos reservados.</q-toolbar-title>
            </q-toolbar>
        </q-footer>
        <!-- END FOOTER -->

        <!-- LEFT DRAWER -->
        <q-drawer v-model="drawerLeft" :width="200" :breakpoint="700" bordered>
            <q-scroll-area class="fit">
                <q-list>
                    <template v-for="(menuItem, index) in menuList" :key="index">
                        <NuxtLink :to="menuItem.to">
                            <q-item clickable v-ripple>
                                <q-item-section avatar>
                                    <q-icon :name="menuItem.icon" />
                                </q-item-section>
                                <q-item-section>
                                    {{ menuItem.label }}
                                </q-item-section>
                            </q-item>
                        </NuxtLink>
                        <q-separator :key="'sep' + index" v-if="menuItem.separator" />
                    </template>

                </q-list>
                <q-list class="mt-10">
                    <q-item clickable @click="handleLogout">
                        <q-item-section avatar>
                            <q-icon size="25px" name="mdi-logout" />
                        </q-item-section>
                        <q-item-section>
                            <div color="primary">Sair</div>
                        </q-item-section>
                    </q-item>
                    <q-item>
                        <div class="mt-2">Logado como: {{ auth.user.name }}</div>
                    </q-item>
                </q-list>
            </q-scroll-area>

        </q-drawer>
        <!-- END LEFT DRAWER -->

        <!-- RIGHT DRAWER -->
        <q-drawer class="flex flex-col justify-between" v-model="drawerRight" side="right" :width="500" :breakpoint="400">
            <div class="q-pa-md row justify-center">
                <div style="width: 100%;">
                    <q-chat-message name="me" :text="['hey, how are you?']" sent />
                    <q-chat-message name="Jane" :text="['doing fine, how r you?']" />
                </div>
            </div>
            <div>
                <q-input outlined @keyup.enter="send">
                    <template v-slot:append>
                        <q-btn flat round dense icon="send" @click="send" />
                    </template>
                </q-input>
            </div>
        </q-drawer>
        <!-- END RIGHT DRAWER -->

        <!-- MAIN CONTENT -->
        <q-page-container>
            <NuxtPage />
        </q-page-container>
        <!-- END MAIN CONTENT -->

    </q-layout>
</template>

<style>
.q-layout-padding {
    padding: 16px !important;
}
</style>