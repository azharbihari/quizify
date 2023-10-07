<template>
    <main class="container my-5" v-if="quizzes">
        <h1 class="display-6">Quiz List<RouterLink class="btn btn-primary float-end" aria-current="page" to="/new-quiz">+
                New Quiz
            </RouterLink>
        </h1>
        <p class="lead text-muted">
            Welcome to the Quiz List page. Here, you can find quizzes that you've
            created.
        </p>

        <div class="table-responsive">
            <table class="table table-hover table-bordered">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Subject</th>
                        <th>Topic</th>
                        <th>Difficulty</th>
                        <th>Number of Questions</th>
                        <th>Duration</th>
                        <th>Created At</th>
                        <th>Score</th>
                        <th>Status & Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="quiz in  quizzes " :key="quiz.id">
                        <td>{{ quiz.name }}</td>
                        <td>{{ quiz.subject.name }}</td>
                        <td>{{ quiz.topic.name }}</td>
                        <td>{{ getDifficulty(quiz.difficulty) }}</td>
                        <td>{{ quiz.questions.length }}
                            <RouterLink class="link-primary" :to="`/quiz/${quiz.slug}/questions`">View Questions
                            </RouterLink>

                            <RouterLink v-if="quiz.user.has_active_subscription" class="link-primary"
                                :to="`/quiz/${quiz.slug}/solutions`">View Solutions
                            </RouterLink>
                        </td>
                        <td>{{ quiz.duration / 60 }} minutes</td>
                        <td>{{ moment(quiz.created_at).fromNow() }}</td>
                        <td>
                            <span v-if="quiz.status === 'finished'">{{ quiz.result.score }}</span>
                            <span v-else>-</span>
                        </td>

                        <td>
                            <RouterLink v-if="quiz.status === 'active'" class="btn btn-sm btn-energetic"
                                :to="`/quizzes/${quiz.slug}/detail`">Start Quiz</RouterLink>

                            <RouterLink v-if="quiz.status === 'started'" class="btn btn-sm btn-energetic"
                                :to="`/quizzes/${quiz.slug}/detail`">Go to Quiz</RouterLink>
                            <span :class="getBadgeClass(quiz.status)" v-else>
                                {{ getStatus(quiz.status) }}
                            </span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </main>
</template>
  
<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import api from '@/api';
import moment from 'moment';

const quizzes = ref(null);
const route = useRoute();
const router = useRouter();
onMounted(async () => {
    await fetchQuizzes();
});


const fetchQuizzes = async () => {
    try {
        const response = await api.get(`/quizzes/`);
        quizzes.value = response.data;
    } catch (error) {
        console.error('Error fetching quizzes data:', error);
    }
};



function getStatus(status: string): string {
    switch (status) {
        case 'active':
            return 'Active';
        case 'started':
            return 'Started';
        case 'finished':
            return 'Finished';
        case 'expired':
            return 'Expired';
        default:
            return status;
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


function getBadgeClass(status: string): string {
    switch (status) {
        case 'active':
            return 'badge rounded-pill text-bg-info';
        case 'started':
            return 'badge rounded-pill text-bg-primary';
        case 'finished':
            return 'badge rounded-pill text-bg-success';
        case 'expired':
            return 'badge rounded-pill text-bg-danger';
        default:
            return '';
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