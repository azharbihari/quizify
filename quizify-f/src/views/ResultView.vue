<template>
    <main class="container mt-5">
        <div class="card shadow" v-if="result">
            <div class="card-body">
                <h4 class="card-title">Quiz Result</h4>
                <p>Quiz Name: {{ result.quiz.name }}</p>
                <p>Score: {{ result.score }}</p>

                <hr />

                <!-- Additional Analysis -->
                <div class="analysis">
                    <h5>Performance Analysis</h5>
                    <p>
                        Congratulations on completing the quiz! Your score indicates your
                        understanding of the content. Let's dive deeper into your performance.
                    </p>

                    <p v-if="result.score >= 80">
                        Great job! Your score reflects a strong grasp of the material.
                        You've demonstrated a high level of knowledge and comprehension.
                    </p>
                    <p v-else-if="result.score >= 60">
                        Good work! Your score suggests a satisfactory understanding of
                        the material. There's room for improvement, but you're on the right track.
                    </p>
                    <p v-else>
                        Keep practicing. Your score indicates that there might be some
                        concepts you need to review. Don't worry; with dedication, you can
                        improve your understanding.
                    </p>
                </div>

                <!-- Additional Text -->
                <div class="additional-text">
                    <h5>Further Reading</h5>
                    <p>
                        If you're interested in enhancing your knowledge, consider exploring
                        additional resources related to the quiz topic. This could include
                        books, articles, online courses, and more.
                    </p>

                    <h5>Quiz Insights</h5>
                    <p>
                        Reflect on your quiz experience. What were the challenging questions?
                        Were there any surprises? Use this insight to guide your future study
                        and learning strategies.
                    </p>
                </div>
            </div>
        </div>
    </main>
</template>
  
<script setup lang="ts">
import { ref, onMounted } from 'vue';
import api from '@/api';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();
const result = ref(null);

onMounted(async () => {
    try {
        const response = await api.get(`/quizzes/${route.params.quizSlug}/result/`);
        result.value = response.data;
    } catch (error) {
        console.error('Error fetching result data:', error);
    }
});
</script>
  