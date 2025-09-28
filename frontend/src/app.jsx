import './css/app.css'

// import { Cards } from './components/cards'
import { useState, Suspense, lazy } from 'react'
import Container from 'react-bootstrap/Container'
import { LightModeProvider } from './context/LightModeContext'
import { LightModeButton } from './components/LightModeButton'
import { SpinnerLoading } from './components/spinner'

const Cards = lazy(() => import('./components/cards'))

export default function App () {
  const [update, setUpdate] = useState(null)
  return (
    <LightModeProvider>
      <main>
        <header>
          <div className='d-flex justify-content-between align-items-start px-3'>
            <div className='flex-grow-1 text-center'>
              <h1 className='m-0 titulos'>🇺🇸 USD/PYG 🇺🇸</h1>
            </div>
            <div className='mt-2'>
              <LightModeButton />
            </div>
          </div>

          <div className='text-center update'>
            {update && (
              <p>--Ultima Actualizacion: {new Date(update).toLocaleString('es-ES')}--</p>
            )}
          </div>
        </header>

        <Suspense fallback={
          <div className='d-flex justify-content-center align-items-center spinner-bg'>
            <SpinnerLoading />
          </div>
      }
        >
          <Container>
            <div className='api-response'>
              <Cards onUpdate={setUpdate} />
            </div>

          </Container>
        </Suspense>

      </main>
    </LightModeProvider>
  )
}
