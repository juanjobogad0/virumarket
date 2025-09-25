import '../css/cards.css'
import { NombresCasas } from '../constants/constants'
import { useState, useEffect } from 'react'
import { API_URL } from '../services/api'

export function Cards ({ onUpdate }) {
  const [casas, setData] = useState([])
  const [best, setBest] = useState(null)

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        setData(data.slice(0, 4))
        const fecha = data[0].fecha
        onUpdate(fecha)
      })
      .catch(err => console.error(err))
  }, [onUpdate])

  function buyButton () {
    const datos = [...casas]
    const bestBuy = datos.sort((a, b) => Number(b.compra) - Number(a.compra))
    setData(bestBuy)
    setBest(bestBuy[0].id)
    setTimeout(() => setBest(null), 1000)
  }

  function sellButton () {
    const datos = [...casas]
    const bestSell = datos.sort((a, b) => Number(a.venta) - Number(b.venta))
    setData(bestSell)
    setBest(bestSell[0].id)
    setTimeout(() => setBest(null), 1000)
  }

  return (
    <>
      <div className='d-flex justify-content-center gap-4'>
        <button
          className=''
          onClick={buyButton}
        >Mejor Compra
        </button>
        <button
          className=''
          onClick={sellButton}
        >Mejor Venta
        </button>
      </div>

      {casas.map((item) => (

        <div key={item.id} className={`cotizaciones-card ${best === item.id ? 'highlight' : ''}`}>
          <aside className='casa'>{NombresCasas[item.casa_cambio] ?? item.casa_cambio}</aside>
          <table className='text-center w-100'>
            <thead>
              <tr className='thead'>
                <th>Compra</th>
                <th>Venta</th>
              </tr>
            </thead>
            <tbody className='tbody'>
              <tr>
                <td>{Number(item.compra).toLocaleString('de-DE')}</td>
                <td>{Number(item.venta).toLocaleString('de-DE')}</td>
              </tr>
            </tbody>
          </table>
        </div>

      ))}

    </>

  )
}
