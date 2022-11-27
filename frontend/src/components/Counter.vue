<script setup>
import { ref } from "vue";

defineProps({
  message: String,
  //   initialCount: Number,
});

const count = ref(0);

function increment() {
  count.value += 2;
}
</script>

<template>
  <div>
    <h2>{{ message }}</h2>
    <button @click="increment">{{ count }}</button>
  </div>
</template>

<style scoped>
button {
  background: pink;
}
</style>