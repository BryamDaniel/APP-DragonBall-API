<script setup>
import { ref, onMounted } from 'vue';
import CharacterDetail from './Modal.vue';

const characters = ref([]);
const pagination = ref([]);
const modalOpen = ref(false);
const select_character = ref(null);


async function fetchData(page) {
    try {
        const response = await fetch(`http://localhost:8000/InfoData?page=${page}`);
        const data = await response.json();
        // console.log(data);
        characters.value = data.items;
        pagination.value = data.meta;
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

async function viewDetails(id) {
    // alert(`id: ${id}`);
    try {
        const datails = await fetch(`http://localhost:8000/infoDataCharacter?id=${id}`);
        const detailData = await datails.json();
        select_character.value = detailData;
        modalOpen.value = true;
        // console.log(detailData);
    } catch (error) {
        console.error("Error fetching character details:", error);
    }
}


function closeModal() {
    modalOpen.value = false;
    select_character.value = null;
    setTimeout(() => {
        select_character.value = null;
    }, 300);
}


const irAPagina = (nuevaPagina) => {
    fetchData(nuevaPagina);
}

onMounted(async () => {
    fetchData(1);
});
</script>


<template>
    <div class="p-4 bg-gray-800   rounded-lg shadow-md">
        <h2 class="title-modal">Tabla de Personajes</h2>

        <div class="overflow-x-auto  rounded-lg">
            <table class="w-full text-left border-collapse">
                <thead>
                    <tr class="bg-orange-600 text-center">
                        <th class="cabecera">ID</th>
                        <th class="cabecera">NOMBRE</th>
                        <th class="cabecera">KI</th>
                        <th class="cabecera">MAX KI</th>
                        <th class="cabecera">RACE</th>
                        <th class="cabecera">GENERO</th>
                        <th class="cabecera">AFILIACION</th>
                        <th class="cabecera">ACCIONES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="character in characters" class="bg-white text-gray-500 hover:bg-gray-200"
                        :key="character.id">
                        <td class="py-3 px-5 border-b border-gray-600">
                            <div
                                class="bg-yellow-400 rounded-full justify-center items-center flex border-2 text-orange-500 w-9 h-9">
                                {{ character.id }}
                            </div>
                        </td>
                        <td class="py-3 px-5 border-b border-gray-600 text-blue-800 font-bold">{{ character.name }}</td>
                        <td class="py-3 px-5 border-b border-gray-600 text-blue-800 font-bold">
                            <div class="bg-yellow-400 rounded-full justify-center  flex border-2 ">
                                {{ character.ki }}
                            </div>
                        </td>
                        <td class="cabecera">{{ character.maxKi }}</td>
                        <td class="cabecera">{{ character.race }}</td>
                        <td class="cabecera">{{ character.gender }}</td>
                        <td class="cabecera">
                            <div class="bg-purple-200 rounded-full justify-center  flex text-purple-800  text-s">
                                {{ character.affiliation }}</div>
                        </td>
                        <td class="cabecera ">
                            <button @click="viewDetails(character.id)" class="botones">
                                Ver Detalles
                            </button>
                        </td>

                    </tr>
                </tbody>
            </table>

            <div class="flex flex-col sm:flex-row justify-between items-center mt-6 gap-4  p-4 rounded-lg">
                <div class="footer-text"> Mostrando página
                    
                        {{ pagination.currentPage }} de {{ pagination.totalPages }}
                </div>
                <div class="inline-flex space-x-2">
                    <button @click="irAPagina(pagination.currentPage - 1)" :disabled="pagination.currentPage === 1"
                        class="px-4 py-2 bg-gray-700 hover:bg-orange-600 disabled:opacity-50 disabled:hover:bg-orange-700 rounded-l transition-colors border-r border-gray-600">
                        Anterior </button>
                    <button @click="irAPagina(pagination.currentPage + 1)"
                        :disabled="pagination.currentPage === pagination.totalPages"
                        class="px-4 py-2 bg-orange-700 hover:bg-orange-600 disabled:opacity-50 disabled:hover:bg-orange-700 rounded-r transition-colors">
                        Siguiente </button>
                </div>
                <div class="footer-text"> Total de personajes: {{ pagination.totalItems }} </div>
            </div>
            <div class="firma"> By ~ Bryam Daniel </div>

        </div>
        <CharacterDetail v-if="modalOpen" :character="select_character" :isOpen="modalOpen" @close="closeModal" />
    </div>
</template>
