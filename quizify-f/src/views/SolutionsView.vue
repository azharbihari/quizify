<template>
    <div class="container mt-5" v-if="quiz">
        <h1 class="display-6">Quiz Solutions</h1>
        <p class="head">Quiz Name: {{ quiz.name }}</p>

        <div v-for="(question, index) in quiz.questions" :key="question.id" class="card mb-3">
            <div class="card-header">
                Question {{ index + 1 }}
            </div>
            <div class="card-body">
                <p class="card-text">{{ question.text }}</p>

                <div v-if="question.solution" class="text-success">
                    {{ question.solution.text }}
                </div>
                <p v-else>
                    No solution available for this question.
                </p>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted, nextTick } from 'vue';
import api from '@/api';
import { useRoute, useRouter } from 'vue-router';
import("@/assets/mathjax/es5/tex-svg-full.js");

const route = useRoute();
const quiz = ref(null);
const fetchQuiz = async () => {
    try {
        const response = await api.get(`/solutions/${route.params.quizSlug}/`);
        quiz.value = response.data;
    } catch (error) {
        console.error('Error fetching quiz solutions:', error);
    }
};

onMounted(() => {
    fetchQuiz();
});

</script>
