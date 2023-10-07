import router from '@/router';
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  headers: {
    'Content-Type': 'application/json',
  },
});



api.interceptors.request.use(function (config) {
  const access_token = localStorage.getItem('access_token');
  if (access_token) {
    config.headers['Authorization'] = `Bearer ${access_token}`;
  }
  return config;
}, function (error) {
  return Promise.reject(error);
});


export default api;