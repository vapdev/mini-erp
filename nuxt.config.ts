// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    'nuxt-quasar-ui',
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt',
  ],
  quasar: { 
    plugins: [
      'Dialog',
      'Notify',
    ],
    extras: {
      font: 'roboto-font',
      fontIcons: ['material-icons', 'mdi-v7'],
      animations: 'all',
    },
  },
})
