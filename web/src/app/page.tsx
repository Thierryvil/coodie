import { Footer } from './components/Footer'
import { GrayButton } from './components/GrayButton'
import { GreenButton } from './components/GreenButton'
import { Navbar } from './components/Navbar'
import './global.css'

export default function Home() {
  return (
    <>
      <Navbar />
      <main>
        <h1>Encontre a oportunidade perfeita para VOCÊ.</h1>
      </main>
      <Footer />

    </>
  )
}
