import '../css/cards.css'
import { NombresCasas } from '../constants/constants'
import { useState, useEffect } from 'react'
import { API_URL } from '../services/api'

export function Cards ({ onUpdate }) {
  const [casas, setData] = useState([])

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        setData(data.slice(0, 4))
        const fecha = data[0].fecha
        onUpdate(fecha)
        console.log(data)
      })
      .catch(err => console.error(err))
  }, [onUpdate])

  return (
    <>
      {casas.map((item) => (

        <div key={item.id} className='cotizaciones-card'>
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
