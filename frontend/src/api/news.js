import request from './request'

export const getNews = () => request.get('/api/news')
export const getAnalysis = () => request.get('/api/analysis')
export const getStatistics = () => request.get('/api/statistics')
export const getGraph = () => request.get('/api/graph')
export const runPipeline = (clearBeforeRun = false) =>
  request.post(`/api/pipeline/run?clear_before_run=${clearBeforeRun}`)
