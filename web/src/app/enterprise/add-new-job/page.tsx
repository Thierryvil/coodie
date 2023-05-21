"use client";

import { Logo } from "../../components/Logo";
import { Avatar } from "../../components/Avatar";
import { GreenButton } from "../../components/GreenButton";
import Link from "next/link";
import "../../global.css";

import React, { FormEvent } from "react";

export default function NewJob() {
  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
  };

  const sendNewJobRequest = async () => {
    const url = `http://localhost:8000/enterprises/jobs/`;
  };

  return (
    <>
      <nav className="flex items-center justify-between py-4 px-8">
        <div className="mr-auto">
          <Link href="/enterprise/timeline">
            <Logo />
          </Link>
        </div>
        <Avatar />
      </nav>
      <div className="bg-gray-100">
        <main>
          <form className="flex flex-col py-8 px-16" onSubmit={handleSubmit}>
            <span className="text-3xl mb-8">Publicar nova vaga</span>
            <label htmlFor="title">Titulo</label>
            <input
              className="py-2 px-2 border border-2 border-gray-500 w-[1280px]"
              type="text"
              id="title"
            />
            <span className="mt-8">Tipo da vaga</span>
            <div className="flex space-x-8">
              <label className="flex items-center">
                <input type="checkbox" className="mr-2" />
                Remoto
              </label>
              <label className="flex items-center">
                <input type="checkbox" className="mr-2" />
                Hibrido
              </label>
              <label className="flex items-center">
                <input type="checkbox" className="mr-2" />
                Presencial
              </label>
            </div>
            <span className="mt-8">Nível de senioridade</span>
            <div className="flex space-x-8">
              <label className="flex items-center">
                <input type="checkbox" className="mr-2" />
                Junior
              </label>
              <label className="flex items-center">
                <input type="checkbox" className="mr-2" />
                Pleno
              </label>
              <label className="flex items-center">
                <input type="checkbox" className="mr-2" />
                Senior
              </label>
            </div>
            <span className="mt-8">Regime de trabalho</span>
            <div className="flex space-x-8">
              <label className="flex items-center">
                <input type="checkbox" className="mr-2" />
                CLT
              </label>
              <label className="flex items-center">
                <input type="checkbox" className="mr-2" />
                PJ
              </label>
            </div>
            <span className="mt-8 mb-2">Descrição da vaga</span>
            <textarea
              className="px-2 py-2 border border-2 border-gray-500 w-[1280px] h-[546px] mb-4"
              name=""
              id=""
            ></textarea>
            <GreenButton text="Publicar" size="medium" />
          </form>
        </main>
      </div>
    </>
  );
}
