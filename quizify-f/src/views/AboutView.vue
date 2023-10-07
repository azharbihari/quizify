<template>
    <div class="about-company-page container my-5">
        <h1 class="display-4">About Our Company</h1>
        <p class="lead">Welcome to the About Us page of QuizApp.</p>
        <p>We are a dedicated team of professionals passionate about education and exam preparation.</p>

        <h2 class="mt-5">Our Mission</h2>
        <p>We aim to empower learners on their journey to success by providing a comprehensive platform that bridges the gap
            between exam preparation and real-world performance.</p>

        <h2 class="mt-5">Why Choose Us</h2>
        <div class="row mt-3">
            <div class="col-md-6">
                <h4 class="mb-3">Authentic Exam Simulations</h4>
                <p>Our platform offers meticulously crafted timed questions, emulating the conditions of actual exams,
                    ensuring you're prepared to excel under pressure.</p>
            </div>
            <div class="col-md-6">
                <h4 class="mb-3">Instant Feedback & Personalized Insights</h4>
                <p>Receive immediate feedback on your performance, enabling you to identify strengths and areas that need
                    improvement. Our detailed analytics help you tailor your study approach for optimal results.</p>
            </div>
            <div class="col-md-6">
                <h4 class="mb-3">Wide Exam Coverage</h4>
                <p>Prepare for a diverse range of government exams with our curated mock tests. We've got you covered, no
                    matter which examination path you're pursuing.</p>
            </div>
            <div class="col-md-6">
                <h4 class="mb-3">Subject-wise Preparation</h4>
                <p>Our focused subject-wise approach allows you to master the key topics featured in government exams,
                    maximizing your chances of success.</p>
            </div>
            <div class="col-md-6">
                <h4 class="mb-3">Engaging Community</h4>
                <p>Engage with a vibrant community of learners, share insights, solve doubts, and learn from peers who are
                    on the same journey as you.</p>
            </div>
        </div>

        <h2 class="mt-5">Our Team</h2>
        <div class="row mt-3">
            <div class="col-md-4 mb-4" v-for="teamMember in teamMembers" :key="teamMember.id">
                <div class="card h-100">
                    <img :src="teamMember.avatar" class="card-img-top" alt="Team Member">
                    <div class="card-body">
                        <h5 class="card-title">{{ teamMember.name }}</h5>
                        <p class="card-text">{{ teamMember.role }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script setup lang="ts">
import { ref } from 'vue';


const teamMembers = ref([{
    id: 1,
    name: 'John Doe',
    role: 'Founder & CEO',
    avatar: 'https://i.pravatar.cc/300',
}])
</script>
  
<style>
/* Add your custom styles here */
</style>
  