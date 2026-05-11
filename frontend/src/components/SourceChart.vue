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
    title: { text: '新闻来源分布', left: 'center' },
    tooltip: {},
    xAxis: {
      type: 'category',
      data: props.data.map(item => item.source)
    },
    yAxis: { type: 'value' },
    series: [
      {
        type: 'bar',
        data: props.data.map(item => item.count)
      }
    ]
  })
}

onMounted(renderChart)
watch(() => props.data, renderChart, { deep: true })
</script>
