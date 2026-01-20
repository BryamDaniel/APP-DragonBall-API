<script setup>
import { defineProps, defineEmits } from 'vue';
import Card from './card.vue';

const props = defineProps({
    character: {
        type: Object,
        required: true
    },
    isOpen: {
        type: Boolean,
        required: true
    }
});

// defineEmits(['close']);

const emit = defineEmits(['close']);

const closeModal = () => {
    emit('close');
};
</script>

<template>
    <div class="fixed inset-0 z-5 flex items-center justify-center p-6 bg-black bg-opacity-75 backdrop-blur-sm">
        <div
            class="bg-gray-900 border-2  max-h-[100vh] border-orange-500 rounded-5xl w-full overflow-hidden shadow-2xl">
            <div class="bg-orange-600 p-4 flex justify-between items-center">
                <h3 class="text-2xl font-bold italic text-white ">{{ character?.name }}</h3>
                <button @click="$emit('close')" class="text-white hover:text-black text-2xl">&times;</button>
            </div>

            <div class="p-6 flex flex-col md:flex-row gap-6 overflow-y-auto max-h-[70vh]">
                <img :src="character?.image" :alt="character?.name"
                    class="h-64 object-contain bg-gray-800 rounded-lg p-2 " />
                <div class="flex-1 space-y-3">
                    <div class="flex gap-3">
                        <p class="estadisitcas"><span
                                class="text-orange-400 font-bold ">Raza:</span> {{ character?.race }}</p>
                        <p class="estadisitcas"><span
                                class="text-orange-400 font-bold">Ki:</span> {{ character?.ki }}</p>
                        <p class="estadisitcas"><span
                                class="text-orange-400 font-bold">Máximo Ki:</span> {{ character?.maxKi }}</p>
                        <p class="estadisitcas"><span
                                class="text-orange-400 font-bold">Afiliación:</span> {{ character?.affiliation }}</p>
                    </div>

                    <div class="mt-4 bg-gray-800 p-3 rounded-lg">
                        <h4 class="title-modal">Descripción:</h4>
                        <p class="text-sm text-gray-300 leading-relaxed h-32 overflow-y-auto">
                            {{ character?.description || 'No hay descripción disponible.' }}
                        </p>
                    </div>
                    <div class="mt-4 bg-purple-900 p-3 rounded-lg">
                        <h4 class="title-modal">Planeta de Origen:</h4>
                        <div class="flex gap-4">
                            <img :src="character?.originPlanet.image" :alt="character?.originPlanet.name"
                                class="w-26 h-26 object-cover rounded-lg">
                            <div>
                                <p class="text-white font-bold text-xl mb-2"> {{ character?.originPlanet.name }}</p>
                                <p class="text-sm text-gray-300 leading-relaxed  overflow-y-auto">
                                    {{ character?.originPlanet.description }}
                                </p>
                                <p v-if="character?.originPlanet.isDestroyed" class="text-red-500 font-bold">
                                    <span class=" bg-red-600 rounded-full text-white p-1 text-xs px-2"> DESTRUIDO
                                    </span>
                                </p>
                            </div>

                        </div>

                    </div>
                    <div v-if="character?.transformations && character?.transformations.length > 0"
                        class="space-y-4 bg-gray-800 rounded-lg p-4">
                        <h4 class="title-modal">Transformaciones:</h4>
                        <div class="grid grid-cols-3 gap-4 flex tex-center justify-center items-center">
                            <Card v-for="transformation in character?.transformations" :key="transformation.id"
                                :transformation="transformation" />


                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-gray-800 p-4 text-right">
                <button @click="$emit('close')"
                    class="botones">
                    Cerrar
                </button>
            </div>
        </div>
    </div>
</template>

