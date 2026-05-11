<template>
  <span class="tag">
    {{ label }}：{{ score }}
  </span>
</template>

<script setup>
defineProps({
  label: String,
  score: [Number, String]
})
</script>
