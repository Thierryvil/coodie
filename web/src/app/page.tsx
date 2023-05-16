import { Footer } from './components/Footer'
import { Navbar } from './components/Navbar'
import { Lexend_Zetta } from 'next/font/google'
import Image from 'next/image';
import './global.css'

const zetta = Lexend_Zetta({ subsets: ['latin'] })

export default function Home() {
  return (
    <>
      <Navbar />
      <main>
        <div className='mt-8 flex flex-col items-center'>
          <p className={`${zetta.className} text-3xl text-center`}>Encontre a oportunidade <br />perfeita para VOCÊ.</p>
          <Image className="flex justify-center" src="/hiring.svg" alt="Descrição da imagem" width={665} height={547} />
        </div>
      </main>
      <Footer />
    </>
  )
}
