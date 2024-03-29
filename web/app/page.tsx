"use client";

import Image from "next/image";
import { Lexend_Zetta } from "next/font/google";
import { Footer } from "./components/Footer";
import { Navbar } from "./components/Navbar";
import { JobBox } from "./components/JobBox";
import "./global.css";
import { COODIE_API_URL } from "./constants";

const zetta = Lexend_Zetta({ subsets: ["latin"] });


export default async function Home() {
  await fetch(COODIE_API_URL ?? "") // Wakeup Backend

  return (
    <>
      <Navbar />
      <main>
        <div className="mt-8 flex flex-col items-center">
          <div className="mb-20">
            <p className={`${zetta.className} text-3xl text-center`}>
              Encontre a oportunidade <br />
              perfeita para VOCÊ.
            </p>
            <Image
              className="flex justify-center"
              src="/hiring.svg"
              alt="Descrição da imagem"
              width={665}
              height={547}
            />
          </div>
          <div className="w-full bg-gray-200 py-4 text-center">
            <span className={`${zetta.className} text-3xl`}>
              NOSSAS ÚLTIMAS VAGAS
            </span>
            <div className="flex space-x-20 items-center justify-center py-8">
              <JobBox />
              <JobBox />
              <JobBox />
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </>
  );
}
