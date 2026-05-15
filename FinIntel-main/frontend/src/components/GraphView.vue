<template>
  <div ref="chartRef" class="chart-box"></div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue'
import * as echarts from 'echarts'

const props = defineProps({
  nodes: { type: Array, default: () => [] },
  edges: { type: Array, default: () => [] }
})

const chartRef = ref(null)
let chart = null

const renderChart = () => {
  if (!chartRef.value) return
  if (!chart) chart = echarts.init(chartRef.value)

  chart.setOption({
    title: { text: '股票情报知识图谱', left: 'center' },
    tooltip: {},
    series: [
      {
        type: 'graph',
        layout: 'force',
        roam: true,
        label: { show: true },
        force: { repulsion: 180, edgeLength: 120 },
        data: props.nodes.map(node => ({
          id: node.node_id,
          name: node.name,
          category: node.node_type,
          symbolSize: node.node_type === 'event' ? 56 : 42
        })),
        links: props.edges.map(edge => ({
          source: edge.source_id,
          target: edge.target_id,
          name: edge.relation_type,
          value: edge.weight
        })),
        categories: [
          { name: 'event' },
          { name: 'stock' },
          { name: 'industry' },
          { name: 'source' }
        ],
        edgeLabel: {
          show: true,
          formatter: params => params.data.name
        }
      }
    ]
  })
}

onMounted(renderChart)
watch(() => [props.nodes, props.edges], renderChart, { deep: true })
</script>
