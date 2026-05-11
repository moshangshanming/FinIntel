<template>
  <div>
    <div class="page-title">新闻情报列表</div>

    <table class="table">
      <thead>
        <tr>
          <th>标题</th>
          <th>来源</th>
          <th>股票</th>
          <th>行业</th>
          <th>发布时间</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in newsList" :key="item.id">
          <td>{{ item.title }}</td>
          <td>{{ item.source }}</td>
          <td>{{ item.stock_name }} {{ item.stock_code }}</td>
          <td>{{ item.industry }}</td>
          <td>{{ item.publish_time }}</td>
        </tr>
      </tbody>
    </table>

    <div class="page-title" style="margin-top: 28px;">智能分析结果</div>
    <table class="table">
      <thead>
        <tr>
          <th>事件</th>
          <th>股票</th>
          <th>情绪</th>
          <th>影响分</th>
          <th>风险分</th>
          <th>摘要</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in analysisList" :key="item.analysis_id">
          <td>{{ item.event_title }}</td>
          <td>{{ item.related_stock_name }}</td>
          <td :class="item.sentiment">{{ item.sentiment }}</td>
          <td>{{ item.impact_score }}</td>
          <td>{{ item.risk_score }}</td>
          <td>{{ item.summary }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { getNews, getAnalysis } from '../api/news'

const newsList = ref([])
const analysisList = ref([])

onMounted(async () => {
  const newsRes = await getNews()
  newsList.value = newsRes.data

  const analysisRes = await getAnalysis()
  analysisList.value = analysisRes.data
})
</script>
