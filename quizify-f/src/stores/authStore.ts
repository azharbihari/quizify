import { defineStore } from 'pinia';
import type { Token, User } from '@/types';
import { ref, onMounted } from 'vue';
import api from '@/api';
import { useRouter } from 'vue-router';


export const useAuthStore = defineStore('auth', () => {
    const router = useRouter();
    const user = ref<User>({} as User);
    const isAuthenticated = ref<boolean>(localStorage.getItem('isAuthenticated') === 'true');
    const isRegistered = ref<boolean>(false);
    const login = async () => {
        try {

            const response = await api.post('/accounts/login/', user.value);

            const token = response.data as Token;
            localStorage.setItem('access_token', token.access_token);
            localStorage.setItem('refresh_token', token.refresh_token);
            localStorage.setItem('isAuthenticated', 'true');
            isAuthenticated.value = true;
            await fetchUser();
            router.push('/dashboard');
        } catch (error) {
            console.error('Login error', error);
        }
    };


    const register = async () => {
        try {
            const response = await api.post('/accounts/register/', user.value);
            isRegistered.value = true;
            user.value = response.data;
            router.push('/login');
        } catch (error) {
            console.error('Register error', error);
        }
    };


    const fetchUser = async () => {
        try {
            const response = await api.get('/accounts/user/');
            console.log(response.data)
            user.value = response.data as User;
        } catch (error) {
            console.error('Fetch user error', error);
        }
    };
    const logout = async () => {
        try {

            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            localStorage.removeItem('isAuthenticated');
            isAuthenticated.value = false;
            router.push('/login');
        } catch (error) {
            console.error('Logout error', error);
        }
    };

    return { login, user, register, isRegistered, isAuthenticated, logout, fetchUser };
});