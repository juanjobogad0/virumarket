import { useContext } from 'react'
import darkIcon from '../assets/dark.svg'
import lightIcon from '../assets/light.svg'
import { LightModeContext } from '../context/LightModeContext'

export function LightModeButton () {
  const { lightMode, handleClick } = useContext(LightModeContext)
  return (
    <button onClick={handleClick} className=''>
      {lightMode
        ? <img src={darkIcon} alt='Dark Mode' className='' />
        : <img src={lightIcon} alt='Light Mode' className='' />}
    </button>
  )
}
