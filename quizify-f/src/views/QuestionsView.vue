<template>
    <div class="container mt-5" v-if="quiz">
        <h1 class="display-6">Quiz Questions</h1>
        <p class="head">Quiz Name: {{ quiz.name }}</p>

        <div v-for="(question, index) in quiz.questions" :key="question.id" class="card mb-3">
            <div class="card-header">
                Question {{ index + 1 }}
            </div>
            <div class="card-body">
                <p class="card-text">{{ question.text }}</p>

                <div class="form-check form-check-inline" v-for="choice in question.choices" :key="choice.id">
                    <input :checked="choice.id === question.userChoice" :id="choice.id" class="form-check-input"
                        type="radio" :value="choice.id" :name="`listGroupRadio-${question.id}`">
                    <label :class="{ 'form-check-label': true, 'text-success fw-bold': choice.is_correct }"
                        :for="choice.id">
                        {{ choice.text }}
                    </label>
                </div>
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
        const response = await api.get(`/quizzes/${route.params.quizSlug}/`);
        quiz.value = response.data;
        const userAnswers = quiz.value.answers;

        userAnswers.forEach(userAnswer => {
            const question = quiz.value.questions.find(q => q.id === userAnswer.question);
            if (question) {
                question.userChoice = userAnswer.choice;
            }
        });
    } catch (error) {
        console.error('Error fetching quiz data:', error);
    }
};

onMounted(() => {
    fetchQuiz();
});

</script>
