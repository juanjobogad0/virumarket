import '../css/cards.css'
import { useState, useEffect } from 'react'
import { API_URL } from '../services/api'

export function Cards () {
  const [casas, setData] = useState([])

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setData(data))
      .catch(err => console.error(err))
  }, [])

  return (
    <>
      {casas.map((item) => (

        <article key={item.id} className='p-1 card mb-4'>
          <aside className='casa'>{item.casa_cambio}</aside>
          <table className='text-center'>
            <thead>
              <tr className='m-0 thead'>
                <th>Compra</th>
                <th>Venta</th>
              </tr>
            </thead>
            <tbody className='tbody'>
              <tr>
                <td>{item.compra}</td>
                <td>{item.venta}</td>
              </tr>
            </tbody>
          </table>
        </article>

      ))}

    </>

  )
}
