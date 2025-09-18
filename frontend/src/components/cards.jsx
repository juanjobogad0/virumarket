import '../css/cards.css'

export function Cards () {
  return (
    <article className='p-1 card mb-4'>
      <aside className='casa'>Cambios Chaco</aside>
      <table className='text-center'>
        <thead>
          <tr className='m-0 thead'>
            <th>Compra</th>
            <th>Venta</th>
          </tr>
        </thead>
        <tbody className='tbody'>
          <tr>
            <td>7800</td>
            <td>8000</td>
          </tr>
        </tbody>
      </table>
    </article>
  )
}
