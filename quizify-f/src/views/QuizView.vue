<template>
    <main class="container my-5" v-if="quiz">
        <div v-if="quizStarted">
            <div class="row">
                <div class="col-md-9">
                    <h2 class="">{{ quiz.name }}</h2>
                    <p class="lead">Number of Questions: {{ quiz.questions.length }}, Difficulty: {{
                        getDifficulty(quiz.difficulty) }},
                        Duration: {{ quiz.duration / 60 }}
                        minutes</p>
                </div>
                <div class="col-md-3">
                    <QuizTimer :remainingTime="remainingTime" />
                </div>
            </div>

            <hr>
            <div class="row g-4">
                <div class="col-md-9">
                    <div class="card mb-4">
                        <div class="card-header bg-azure">
                            Question {{ currentQuestionIndex + 1 }} of {{ quiz.questions.length }}
                            <span class="badge rounded-pill text-bg-secondary float-end">{{ getDifficulty(quiz.difficulty)
                            }}</span>

                        </div>

                        <Question :question="currentQuestion" :answer="currentQuestion.answer" :saveAnswer="saveAnswer" />

                        <div class="card-footer hstack gap-2">
                            <button @click="previousQuestion" :disabled="currentQuestionIndex === 0"
                                class="btn btn-energetic">Previous
                                Question</button>
                            <button @click="nextQuestion" :disabled="currentQuestionIndex === quiz.questions.length - 1"
                                class="btn btn-energetic">Next Question</button>
                            <button @click="submitQuiz" class="btn btn-danger ms-auto">Submit Quiz</button>
                        </div>
                    </div>
                </div>

                <div class="col-md-3 border py-2">
                    <h6>Questions</h6>
                    <div class="hstack gap-2">
                        <button v-for="(question, index) in quiz.questions" :key="question.id" @click="goToQuestion(index)"
                            class="btn" :class="{ 'btn-energetic': currentQuestionIndex === index }">
                            {{ index + 1 }}
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>
  
<script setup lang="ts">
import { ref, onMounted, computed, onBeforeUnmount } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import api from '@/api';
import QuizTimer from '@/components/QuizTimer.vue';
import Question from '@/components/Question.vue';
import("@/assets/mathjax/es5/tex-svg-full.js");
import type { Quiz } from '@/types';
import moment from 'moment';


const quiz = ref<Quiz>();
const route = useRoute();
const router = useRouter();
const quizStarted = computed(() => quiz.value && quiz.value.status === 'started');

onMounted(async () => {
    await fetchQuiz();
    if (quizStarted.value) {
        startTimer(); // Start the timer if the quiz has started
    }
});


const remainingTime = ref(0);

const startTimer = () => {
    remainingTime.value = quiz.value.remaining_time; // Initialize remaining time with quiz duration in seconds

    const interval = setInterval(() => {
        if (remainingTime.value > 0) {
            remainingTime.value--;
        } else {
            clearInterval(interval); // Clear the timer interval
            submitQuiz(); // Automatically submit the quiz when time is up
        }
    }, 1000); // Update timer every second
};

const fetchQuiz = async () => {
    try {
        const response = await api.get(`/quizzes/${route.params.quizSlug}/start/`);
        quiz.value = response.data;
        const answers = quiz.value.answers;

        answers.forEach(answer => {
            const question = quiz.value.questions.find(question => question.id === answer.question);
            if (question) {
                question.answer = answer;
            }
        });
    } catch (error) {
        console.error('Error fetching quiz data:', error);
    }
};




const submitQuiz = async () => {
    try {
        await api.post(`/quizzes/${route.params.quizSlug}/finish/`);
        console.log('Quiz submitted successfully');
        router.push({ name: 'ResultPage', params: { quizSlug: route.params.quizSlug } });
        fetchQuiz();
    } catch (error) {
        console.error('Error submitting quiz:', error);
    }
};

const saveAnswer = async (answer) => {
    try {
        const response = await api.post(`/quizzes/${route.params.quizSlug}/answer/`, answer);
        console.log('Answer saved successfully');
        fetchQuiz()
    } catch (error) {
        console.error('Error saving answer:', error);
    }
};

const currentQuestionIndex = ref(0); // Initialize with the first question

const currentQuestion = computed(() => {
    if (quiz.value && quiz.value.questions) {
        return quiz.value.questions[currentQuestionIndex.value];
    }
    return null;
});

const nextQuestion = () => {
    if (currentQuestionIndex.value < quiz.value.questions.length - 1) {
        currentQuestionIndex.value++;
    }
};


const previousQuestion = () => {
    if (currentQuestionIndex.value > 0) {
        currentQuestionIndex.value--;
    }
};


const goToQuestion = (index) => {
    if (index >= 0 && index < quiz.value.questions.length) {
        currentQuestionIndex.value = index;
    }
};


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

.bg-azure {
    background-color: #b0c5bf;
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