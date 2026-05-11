<template>
  <div ref="chartRef" class="chart-box"></div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue'
import * as echarts from 'echarts'

const props = defineProps({
  data: { type: Array, default: () => [] }
})

const chartRef = ref(null)
let chart = null

const renderChart = () => {
  if (!chartRef.value) return
  if (!chart) chart = echarts.init(chartRef.value)

  chart.setOption({
    title: { text: '风险事件排行', left: 'center' },
    tooltip: {},
    xAxis: { type: 'value' },
    yAxis: {
      type: 'category',
      data: props.data.map(item => item.related_stock_name || item.event_title).reverse()
    },
    series: [
      {
        type: 'bar',
        data: props.data.map(item => item.risk_score).reverse()
      }
    ]
  })
}

onMounted(renderChart)
watch(() => props.data, renderChart, { deep: true })
</script>
