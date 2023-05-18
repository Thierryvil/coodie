'use client'

import React from "react";
import { Logo } from "../components/Logo";
import '../global.css';
import { Avatar } from "../components/Avatar";
import { GreenButton } from "../components/GreenButton";

export default function EnterpriseTimeline() {
    return (
        <>
            <nav className="flex items-center justify-between py-4 px-8">
                <div className="mr-auto" >
                    <Logo />
                </div>
                <Avatar />
            </nav>
            <div className="bg-gray-100 h-screen">
                <main className="flex flex-col py-8 px-16">
                    <GreenButton text="Cadastrar Nova Vaga" onClick={() => null} size="large" />
                    <span className="py-8 text-3xl">SUA VAGAS PUBLICADAS</span>
                </main>
            </div>
        </>
    )
}