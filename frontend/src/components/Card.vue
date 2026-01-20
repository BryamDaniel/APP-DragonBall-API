<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    transformation: {
        type: Object,
        required: true
    }
})

</script>


<template>

    <div class="flex flex-col items-center justify-center group">
        <div class="relative flex flex-col items-center justify-center">
            <img :src="transformation.image" :alt="transformation.name" class="w-70 h-70 object-contain">
            <h1 class="title-modal">{{ transformation.name }}</h1>

        </div>

    </div>
</template>