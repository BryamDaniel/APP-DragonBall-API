<script setup>
import TablaDatos from './components/Tabla.vue';
</script>

<template>
  <div class="bg-gray-900 min-h-screen p-4 items-center justify-center p-8">
    <header class="mb-10 text-center">
      <h1 class="text-5xl  text-yellow-300 italic font-bold text-center mb-8">
        DRAGON BALL API
      </h1>
    </header>
    <div class="w-full max-w-7xl mx-auto">
      <TablaDatos />
    </div>
  </div>
</template>
