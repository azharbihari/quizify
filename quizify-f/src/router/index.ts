import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import { useAuthStore } from '@/stores/authStore';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  linkActiveClass: 'active',
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomeView
    },


    {
      path: '/about',
      name: 'AboutPage',
      component: () => import('@/views/AboutView.vue'),
    },

    {
      path: '/contact',
      name: 'ContactPage',
      component: () => import('@/views/ContactView.vue'),
    },

    {
      path: '/subscriptions',
      name: 'SubscriptionPage',
      component: () => import('@/views/SubscriptionsView.vue'),
    },

    {
      path: '/quizzes/:quizSlug/detail',
      name: 'QuizDetailPage',
      component: () => import('@/views/QuizDetailView.vue'),
      props: true,
    },

    {
      path: '/new-quiz',
      name: 'NewQuizPage',
      component: () => import('@/views/NewQuizView.vue'),
    },

    {
      path: '/quiz/:quizSlug/',
      name: 'QuizPage',
      component: () => import('@/views/QuizView.vue'),
      props: true,
    },

    {
      path: '/quiz/:quizSlug/questions',
      name: 'QuestionsPage',
      component: () => import('@/views/QuestionsView.vue'),
      props: true,
      meta: { requiresAuth: true }
    },



    {
      path: '/quiz/:quizSlug/solutions',
      name: 'SolutionssPage',
      component: () => import('@/views/SolutionsView.vue'),
      props: true,
      meta: { requiresAuth: true }
    },


    {
      path: '/profile',
      name: 'ProfilePage',
      component: () => import('@/views/ProfileView.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: () => import('@/views/LoginView.vue'),
    },

    {
      path: '/register',
      name: 'RegisterPage',
      component: () => import('@/views/RegisterView.vue'),
    },


    {
      path: '/dashboard',
      name: 'DashboardPage',
      component: () => import('@/views/DashboardView.vue'),
      meta: { requiresAuth: true }
    },

    {
      path: '/result/:quizSlug',
      name: 'ResultPage',
      component: () => import('@/views/ResultView.vue'),
      props: true,
    },

    {

      path: '/privacy-policy',
      name: 'PrivacyPolicyPage',
      component: () => import('@/views/PrivacyPolicyView.vue'),
      props: true,
    },

    {
      path: '/terms-and-conditions',
      name: 'T&CPage',
      component: () => import('@/views/T&CView.vue'),
      props: true,
    }
  ]
})




router.beforeEach((to, from, next) => {
  const { isAuthenticated } = useAuthStore();
  if (to.meta.requiresAuth && !isAuthenticated) next({ name: 'LoginPage' })
  else if ((to.name === 'LoginPage' || to.name === 'RegisterPage') && isAuthenticated) next({ name: 'HomePage' })
  else next()
})
export default router
