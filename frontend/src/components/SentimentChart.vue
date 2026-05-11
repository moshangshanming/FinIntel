<template>
  <div ref="chartRef" class="chart-box"></div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue'
import * as echarts from 'echarts'

const props = defineProps({
  data: {
    type: Array,
    default: () => []
  }
})

const chartRef = ref(null)
let chart = null

const renderChart = () => {
  if (!chartRef.value) return
  if (!chart) chart = echarts.init(chartRef.value)
  chart.setOption({
    title: { text: '情绪分布', left: 'center' },
    tooltip: { trigger: 'item' },
    series: [
      {
        type: 'pie',
        radius: '60%',
        data: props.data.map(item => ({
          name: item.sentiment,
          value: item.count
        }))
      }
    ]
  })
}

onMounted(renderChart)
watch(() => props.data, renderChart, { deep: true })
</script>
