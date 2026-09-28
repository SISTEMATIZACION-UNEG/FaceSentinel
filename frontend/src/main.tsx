import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import axios from 'axios'
import './index.css'
import App from './App.tsx'

// Interceptor global para capturar expiración de token y redirigir limpiamente
axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      const detail = error.response.data?.detail
      if (typeof detail === 'string' && (detail.includes('Token expirado') || detail.includes('Token inválido'))) {
        console.warn('Sesión o token expirado. Redirigiendo a login...')
        localStorage.removeItem('token')
        if (window.location.pathname !== '/' && window.location.pathname !== '/signup') {
          window.location.href = '/'
        }
      }
    }
    return Promise.reject(error)
  }
)

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)

