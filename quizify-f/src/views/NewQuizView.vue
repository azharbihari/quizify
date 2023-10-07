<template>
    <main class="container my-5">
        <h2 class="">Generate a New Quiz</h2>
        <p class="lead">Choose a subject, topic, and difficulty level to generate a customized quiz.
        </p>

        <form @submit.prevent="generateQuiz" class="col-md-6">
            <div class="mb-3">
                <label for="subject" class="form-label">Select Subject</label>
                <select v-model="subject" id="subject" class="form-select">
                    <option v-for="subject in subjects" :key="subject.id" :value="subject">{{ subject.name
                    }}</option>
                </select>
            </div>

            <div class="mb-3" v-if="subject && subject.topics && subject.topics.length > 0">
                <label for="topic" class="form-label">Select Topic</label>
                <select v-model="topic" id="topic" class="form-select">
                    <option v-for="topic in subject.topics" :key="topic.id" :value="topic">{{ topic.name }}
                    </option>
                </select>
            </div>
            <div class="mb-3">
                <label for="difficulty" class="form-label">Select Difficulty</label>
                <select v-model="difficulty" id="difficulty" class="form-select">
                    <option v-for="difficulty in difficulties" :key="difficulty.value" :value="difficulty">
                        {{ difficulty.label }}
                    </option>
                </select>
            </div>

            <button type="submit" class="btn btn-energetic" :disabled="loading">
                <div v-if="loading" class="d-flex align-items-center">
                    <span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                    <span>Loading...</span>
                </div>
                <span v-else>Generate Quiz</span>
            </button>
        </form>
    </main>
</template>


<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import type { Subject, Difficulty, Topic, Quiz } from '@/types';
import api from '@/api';
import { useRouter } from 'vue-router';

const quiz = ref<Quiz>({} as Quiz);
const subject = ref<Subject>({} as Subject);
const topic = ref<Topic>({} as Topic);
const difficulty = ref<Difficulty>({} as Difficulty);
const subjects = ref<Subject[]>([]);
const difficulties = ref<Difficulty[]>([
    { value: 'easy', label: 'Easy' },
    { value: 'medium', label: 'Medium' },
    { value: 'hard', label: 'Hard' },
]);
const router = useRouter();


const loading = ref<boolean>(false);

onMounted(async () => {
    try {
        const response = await api.get('/subjects/');
        subjects.value = response.data;
    } catch (error) {
        console.error('Error fetching subjects:', error);
    }
});

const generateQuiz = async () => {
    loading.value = true;
    try {
        const response = await api.post('quizzes/create/', {
            subject: subject.value.id,
            topic: topic.value.id,
            difficulty: difficulty.value.value,
        });
        quiz.value = response.data;
        router.push({ name: 'QuizDetailPage', params: { quizSlug: quiz.value.slug } });
    } catch (error) {
        console.error('Error generating quiz:', error);
    } finally {
        loading.value = false;
    }
};
</script>
<style scoped>
.btn-energetic {
    background-color: #505CE8;
    border-color: #505CE8;
    color: white;
}


.btn-energetic:hover {
    background-color: #3943A8;
}


/* .btn-vibrant
.btn-energetic
.btn-cerulean
.btn-lively
.btn-azure
.btn-dynamic
.btn-cobalt
.btn-invigorating
.btn-sapphire
.btn-radiant */
</style>