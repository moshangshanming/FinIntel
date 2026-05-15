<template>
  <div class="app-shell">
    <aside class="sidebar">
      <div class="brand">FinIntel</div>
      <router-link to="/">首页仪表盘</router-link>
      <router-link to="/news">新闻情报</router-link>
      <router-link to="/graph">知识图谱</router-link>
      <router-link to="/monitor">系统监控</router-link>
    </aside>
    <main class="main">
      <router-view />
    </main>
  </div>
</template>
