<template>
  <div class="card">
    <h3>{{ news.title }}</h3>
    <p>{{ news.content }}</p>
    <span class="tag">{{ news.source }}</span>
    <span class="tag">{{ news.stock_name }}</span>
    <span class="tag">{{ news.industry }}</span>
  </div>
</template>

<script setup>
defineProps({
  news: {
    type: Object,
    required: true
  }
})
</script>
