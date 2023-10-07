<template>
    <div class="card-body">
        <h4 class="card-title">{{ question.text }}</h4>
        <ul class="list-group mt-5">
            <li v-for="choice in question.choices" :key="choice.id" class="list-group-item">
                <input class="form-check-input me-1" type="radio" :name="`listGroupRadio-${question.id}`" :value="choice.id"
                    :id="choice.id" @change="saveAnswer({ question: question.id, choice: choice.id })"
                    :checked="choice.id === answer?.choice" />
                <label class="form-check-label ms-2" :for="choice.id">{{ choice.text }}</label>
            </li>
        </ul>
    </div>
</template>
  
<script setup lang="ts">
const props = defineProps({
    question: Object,
    answer: Object,
    saveAnswer: Function
});
</script>