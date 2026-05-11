import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import NewsList from '../views/NewsList.vue'
import KnowledgeGraph from '../views/KnowledgeGraph.vue'
import SystemMonitor from '../views/SystemMonitor.vue'

const routes = [
  { path: '/', component: Dashboard },
  { path: '/news', component: NewsList },
  { path: '/graph', component: KnowledgeGraph },
  { path: '/monitor', component: SystemMonitor }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
