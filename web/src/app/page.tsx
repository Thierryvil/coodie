import { Footer } from './components/Footer'
import { Navbar } from './components/Navbar'
import { Lexend_Zetta } from 'next/font/google'
import './global.css'

const zetta = Lexend_Zetta({ subsets: ['latin'] })

export default function Home() {
  return (
    <>
      <Navbar />
      <main>
        <p className={zetta.className}>Encontre a oportunidade <br />perfeita para VOCÊ.</p>
      </main>
      <Footer />
    </>
  )
}
