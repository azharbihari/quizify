<template>
    <main v-if="quiz" class="container my-5">
        <h2 class="mb-4">Quiz Generated!</h2>
        <p class="lead mb-4">Your quiz has been successfully generated. Get ready to test your knowledge.</p>

        <table class="table table-bordered w-auto">
            <tbody>
                <tr>
                    <th>Name</th>
                    <td>{{ quiz.name }}</td>
                </tr>
                <tr>
                    <th>Subject</th>
                    <td>{{ quiz.subject.name }}</td>
                </tr>
                <tr>
                    <th>Topic</th>
                    <td>{{ quiz.topic.name }}</td>
                </tr>
                <tr>
                    <th>Number of Questions</th>
                    <td>{{ quiz.number_of_questions }}</td>
                </tr>
                <tr>
                    <th>Difficulty</th>
                    <td>{{ getDifficulty(quiz.difficulty) }}</td>
                </tr>
                <tr>
                    <th>Duration</th>
                    <td>{{ quiz.duration / 60 }} minutes</td>
                </tr>
            </tbody>
        </table>
        <p class="fw-bold">
            Click the button below to start the quiz and begin answering the questions. <br>
            If you'd like to start the quiz later, you can do so from your
            <RouterLink class="link-primary" to="/dashboard">Dashboard</RouterLink>.
        </p>
        <button @click="startQuiz" class="btn btn-energetic btn-lg">Start Quiz</button>
    </main>
</template>
  
<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import api from '@/api';
import type { Quiz } from '@/types';



const quiz = ref<Quiz>();
const route = useRoute();
const router = useRouter();

onMounted(async () => {
    await fetchQuiz()
});
async function fetchQuiz() {
    try {
        const response = await api.get<Quiz>(`/quizzes/${route.params.quizSlug}/`);
        quiz.value = response.data;
    } catch (error) {
        console.error('Error fetching quiz:', error);
    }
}

async function startQuiz() {
    try {
        const response = await api.patch<Quiz>(`/quizzes/${route.params.quizSlug}/start/`);
        quiz.value = response.data;
        console.log('Quiz started successfully');
        router.push({ name: 'QuizPage', params: { quizSlug: quiz.value.slug } });
    } catch (error) {
        console.error('Error starting quiz:', error);
    }
}


function getDifficulty(status: string): string {
    switch (status) {
        case 'medium':
            return 'Medium';
        case 'easy':
            return 'Easy';
        case 'hard':
            return 'Hard';
        default:
            return status;
    }
}

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