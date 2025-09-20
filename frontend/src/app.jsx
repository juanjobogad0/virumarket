import './css/app.css'
import { Cards } from './components/cards'
import { useState } from 'react'
import Container from 'react-bootstrap/Container'

export default function App () {
  const [update, setUpdate] = useState(null)
  return (
    <>
      <h1 className='text-center'>🇺🇸 COTIZACIONES 🇺🇸</h1>
      <Container className='m-auto quitar'>
        <div className='text-center update'>
          {update && (
            <p>Ultima Actualizacion: {new Date(update).toLocaleString('es-ES')}</p>
          )}
        </div>

        <Cards onUpdate={setUpdate} />
      </Container>
    </>

  )
}
