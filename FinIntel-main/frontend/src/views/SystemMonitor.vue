<template>
  <div>
    <div class="page-title">系统运行监控</div>

    <div class="card">
      <button @click="run(false)">运行一次情报分析流水线</button>
      <button @click="run(true)" style="margin-left: 12px;">清空并重新运行</button>
      <pre>{{ result }}</pre>
    </div>

    <div class="card" style="margin-top: 20px;">
      <h3>说明</h3>
      <p>提交版本使用 mock_news.json 作为模拟新闻源，保证离线环境也能稳定演示。</p>
      <p>后续可以在 crawlers 目录中扩展真实新浪财经、东方财富、同花顺、财联社爬虫。</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { runPipeline } from '../api/news'

const result = ref('尚未运行')

const run = async (clearBeforeRun) => {
  const res = await runPipeline(clearBeforeRun)
  result.value = JSON.stringify(res.data, null, 2)
}
</script>

<style scoped>
button {
  padding: 10px 16px;
  border: 0;
  border-radius: 10px;
  background: #2563eb;
  color: #fff;
  cursor: pointer;
}
pre {
  margin-top: 18px;
  background: #111827;
  color: #d1d5db;
  padding: 18px;
  border-radius: 12px;
  overflow: auto;
}
</style>
