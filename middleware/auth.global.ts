import { useAuthStore } from "~/stores/useAuthStore";

export default defineNuxtRouteMiddleware(async (to, from) => {
    console.log("caio aqui: to = ", to, "from = ", from);
    const auth = useAuthStore();

    if (!auth.isLoggedIn && to.path !== "/login" && to.path !== "/register") {
        return navigateTo("/login", { replace: true });
    }
})