<template>
  <div>
    <div class="page-title">FinIntel 首页仪表盘</div>

    <div class="card-grid">
      <div class="card">
        <div class="metric-label">新闻总数</div>
        <div class="metric-value">{{ overview.news_count || 0 }}</div>
      </div>
      <div class="card">
        <div class="metric-label">融合事件数</div>
        <div class="metric-value">{{ overview.event_count || 0 }}</div>
      </div>
      <div class="card">
        <div class="metric-label">正面情报</div>
        <div class="metric-value">{{ sentimentCount.positive || 0 }}</div>
      </div>
      <div class="card">
        <div class="metric-label">风险情报</div>
        <div class="metric-value">{{ sentimentCount.negative || 0 }}</div>
      </div>
    </div>

    <div class="card-grid" style="grid-template-columns: 1fr 1fr;">
      <div class="card">
        <SentimentChart :data="stats.sentiment_distribution || []" />
      </div>
      <div class="card">
        <SourceChart :data="stats.source_distribution || []" />
      </div>
    </div>

    <div class="card">
      <ImpactRankChart :data="stats.top_impact_events || []" />
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { getStatistics } from '../api/news'
import SentimentChart from '../components/SentimentChart.vue'
import SourceChart from '../components/SourceChart.vue'
import ImpactRankChart from '../components/ImpactRankChart.vue'

const stats = ref({})
const overview = computed(() => stats.value.overview || {})
const sentimentCount = computed(() => {
  const result = {}
  for (const item of stats.value.sentiment_distribution || []) {
    result[item.sentiment] = item.count
  }
  return result
})

onMounted(async () => {
  const res = await getStatistics()
  stats.value = res.data
})
</script>
