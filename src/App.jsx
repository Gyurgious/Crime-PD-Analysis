import { useState } from 'react'
import './App.css'
import MapComponent from './MapComponent'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <h1 className="title">Houston City Zip Code Map</h1>
        <MapComponent />

      </div>
    </>
  )
}

export default App
