import './css/app.css'
import { Cards } from './components/cards'
import Container from 'react-bootstrap/Container'

export default function App () {
  return (
    <Container className='m-auto quitar'>
      <Cards />
      <Cards />
      <Cards />
    </Container>

  )
}
