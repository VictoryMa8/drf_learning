import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>People Database</h1>
      <div>
        <input type='text' placeholder='Person name...'></input>
        <input type='number' placeholder='Age...'></input>
        <button>Add Person</button>
      </div>
    </>
  )
}

export default App
