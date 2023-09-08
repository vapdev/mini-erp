<script setup>
</script>

<template>
    <q-layout view="hHr lpR fFr" container style="height: 100vh" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-3'">
        <q-page-container>
            <NuxtPage />
        </q-page-container>
    </q-layout>
</template>


<style>
.q-layout-padding {
    padding: 16px !important;
}
</style>