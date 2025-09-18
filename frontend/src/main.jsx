import 'bootstrap/dist/css/bootstrap.min.css'
import { createRoot } from 'react-dom/client'
import App from './app.jsx'

const root = createRoot(document.getElementById('app'))

root.render(
  <>
    <App />
  </>

)
