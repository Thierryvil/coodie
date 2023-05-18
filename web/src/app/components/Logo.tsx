import { Lexend_Zetta } from 'next/font/google'
const zetta = Lexend_Zetta({ subsets: ['latin'] })

export function Logo() {
    return (
        <span className={`${zetta.className} text-4xl mx-auto`}>coodie</span>
    )
}