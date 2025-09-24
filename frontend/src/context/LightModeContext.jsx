import { useState, useEffect, createContext } from 'react'

export const LightModeContext = createContext()

export function LightModeProvider ({ children }) {
  const [lightMode, setLightMode] = useState(false)

  useEffect(() => {
    if (lightMode) {
      document.body.classList.add('light')
    } else {
      document.body.classList.remove('light')
    }
  }, [lightMode])

  function handleClick () {
    setLightMode(prev => {
      const newValue = !prev
      localStorage.setItem('light', JSON.stringify(newValue))
      return newValue
    })
  }

  useEffect(() => {
    const saved = localStorage.getItem('light')
    if (saved !== null) setLightMode(JSON.parse(saved))
  }, [])

  return (
    <LightModeContext.Provider value={{ lightMode, handleClick }}>
      {children}
    </LightModeContext.Provider>
  )
}
