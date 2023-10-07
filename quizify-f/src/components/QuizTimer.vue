<template>
    <div>
        <p class="mb-0">Time Remaining</p>
        <p class="display-6 fw-semibold">{{ formatRemainingTime(remainingTime) }}</p>
    </div>
</template>
  
<script setup lang="ts">
defineProps({
    remainingTime: Number,
})
const formatRemainingTime = (timeInSeconds: number) => {
    const roundedTime = Math.round(timeInSeconds);
    const minutes = Math.floor(roundedTime / 60);
    const seconds = roundedTime % 60;

    return `${minutes}m ${seconds}s`;
};
</script>
  