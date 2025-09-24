import './css/app.css'
import { Cards } from './components/cards'
import { useState } from 'react'
import Container from 'react-bootstrap/Container'
import { LightModeProvider } from './context/LightModeContext'
import { LightModeButton } from './components/LightModeButton'

export default function App () {
  const [update, setUpdate] = useState(null)
  return (
    <LightModeProvider>
      <main>
        <header>
          <h1 className='text-center titulos'>🇺🇸 Cotizaciones 🇺🇸</h1>
          <div className='text-center update'>
            <LightModeButton />
            {update && (
              <p>--Ultima Actualizacion: {new Date(update).toLocaleString('es-ES')}--</p>
            )}
          </div>
        </header>

        <Container>
          <div className='quitar'>
            <Cards onUpdate={setUpdate} />
          </div>

        </Container>
      </main>
    </LightModeProvider>
  )
}
