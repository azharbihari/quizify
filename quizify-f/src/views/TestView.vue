<template>
    <main v-if="quizGenerated">
        <div class="card-body text-center" v-if="quizGenerated">
            <i class="bi bi-check-circle-fill text-success fs-1"></i>
            <h3 class="card-title">Quiz Generated!</h3>
            <p class="card-text">Your quiz has been successfully generated.</p>
            <RouterLink class="btn btn-sm btn-primary" :to="`/quiz/${quiz.slug}/detail`">Go
                to Quiz</RouterLink>

        </div>

    </main>
    <main class="container my-5" v-else>
        <div class="row">
            <div class="col-lg-6 mx-auto">
                <div class="card shadow">
                    <div class="card-body text-center" v-if="quizGenerated">
                        <i class="bi bi-check-circle-fill text-success fs-1"></i>
                        <h3 class="card-title">Quiz Generated!</h3>
                        <p class="card-text">Your quiz has been successfully generated.</p>
                        <RouterLink class="btn btn-sm btn-primary" :to="`/quiz/${quiz.slug}/detail`">Go
                            to Quiz</RouterLink>

                    </div>
                    <div class="card-body" v-else>
                        <h2 class="card-title">Generate a New Quiz</h2>
                        <p class="text-muted">Choose a subject, topic, and difficulty level to generate a customized quiz.
                        </p>
                        <form @submit.prevent="generateQuiz">
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

                            <button type="submit" class="btn btn-primary" :disabled="loading">
                                <div v-if="loading" class="d-flex align-items-center">
                                    <span class="spinner-border spinner-border-sm me-2" role="status"
                                        aria-hidden="true"></span>
                                    <span>Loading...</span>
                                </div>
                                <span v-else>Generate Quiz</span>
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>


<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import type { Subject, Difficulty, Topic, Quiz } from '@/types';
import api from '@/api';


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



const loading = ref<boolean>(false);
const quizGenerated = ref<boolean>(false);

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
        quizGenerated.value = true;
    } catch (error) {
        console.error('Error generating quiz:', error);
    } finally {
        loading.value = false;
    }
};
</script>
  