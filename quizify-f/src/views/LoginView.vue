<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="" v-if="isRegistered">
                    <p class="text-success fs-2">Hey, {{ user.first_name }} your registration is successful! You can now log
                        in.</p>

                </div>
                <form @submit.prevent="login" class="mt-5">
                    <h2 class="mb-4">Login</h2>
                    <div class="mb-3">
                        <label for="email" class="form-label">Email Address</label>
                        <input v-model="user.email" type="email" class="form-control" id="email" />
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">Password</label>
                        <input v-model="user.password" type="password" class="form-control" id="password" required />
                    </div>
                    <button type="submit" class="btn btn-primary">Login</button>
                </form>
            </div>
        </div>

    </div>
</template>
  
<script setup lang="ts">
import { useAuthStore } from '@/stores/authStore';
const { user, login, isRegistered } = useAuthStore();
</script>
  