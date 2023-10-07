<template>
    <footer>
        <div class="container-fluid py-2 bg-body-tertiary">
            <p class="text-center text-body-secondary">
                &copy; 2023 Quizify, Inc | <RouterLink class="link-primary" aria-current="page" to="/privacy-policy">
                    Privacy Policy</RouterLink> | <RouterLink class="link-primary" aria-current="page"
                    to="/terms-and-conditions">Terms and Conditions </RouterLink>
            </p>
        </div>
    </footer>
</template>

<script setup lang="ts">
</script>

<style scoped>
.footer-link {
    color: #336699;
    text-decoration: none;
    margin: 0 10px;
}
</style>