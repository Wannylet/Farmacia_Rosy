<script setup>
  import { RouterView, useRouter } from 'vue-router'
  import { onMounted } from 'vue'

  const router = useRouter()

  const isLoggedIn = false

  onMounted(() => {
    if (isLoggedIn) {
      router.push('/inicio')
    } else {
      router.push('/iniciar-sesion')
    }
  })
</script>

<template>
  <RouterView/>
</template>

<style scoped>
  
</style>
