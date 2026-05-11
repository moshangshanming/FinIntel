<template>
  <div>
    <div class="page-title">知识图谱展示</div>
    <div class="card">
      <GraphView :nodes="nodes" :edges="edges" />
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { getGraph } from '../api/news'
import GraphView from '../components/GraphView.vue'

const nodes = ref([])
const edges = ref([])

onMounted(async () => {
  const res = await getGraph()
  nodes.value = res.data.nodes || []
  edges.value = res.data.edges || []
})
</script>
