import '../css/LightMode.css'
import { useContext } from 'react'
import darkIcon from '../assets/dark.svg'
import lightIcon from '../assets/light.svg'
import { LightModeContext } from '../context/LightModeContext'

export function LightModeButton () {
  const { lightMode, handleClick } = useContext(LightModeContext)
  return (
    <button onClick={handleClick} className='button-icons'>
      {lightMode
        ? <img src={darkIcon} alt='Dark Mode' className='dark-icon' />
        : <img src={lightIcon} alt='Light Mode' className='light-icon' />}
    </button>
  )
}
