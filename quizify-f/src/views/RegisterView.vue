<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <form @submit.prevent="register" class="mt-5">
                    <h2 class="mb-4">Register</h2>
                    <!-- <div v-if="showSuccessMessage" class="alert alert-success mb-3" role="alert">
                        Registration successful! You can now log in.
                    </div> -->
                    <div class="mb-3">
                        <label for="first_name" class="form-label">First Name</label>
                        <input v-model="user.first_name" type="text" class="form-control" id="first_name" />
                    </div>
                    <div class="mb-3">
                        <label for="last_name" class="form-label">Last Name</label>
                        <input v-model="user.last_name" type="text" class="form-control" id="last_name" />
                    </div>
                    <div class="mb-3">
                        <label for="email" class="form-label">Email</label>
                        <input v-model="user.email" type="text" class="form-control" id="email" required />
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">Password</label>
                        <input v-model="user.password" type="password" class="form-control" id="password" required />
                    </div>
                    <button type="submit" class="btn btn-primary">Register</button>
                </form>
            </div>
        </div>
    </div>
</template>
  
<script setup lang="ts">
import { useAuthStore } from '@/stores/authStore';
const { user, register } = useAuthStore();
</script>