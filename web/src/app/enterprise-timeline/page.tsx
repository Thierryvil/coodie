'use client'

import React from "react";
import { Logo } from "../components/Logo";
import '../global.css';
import { Avatar } from "../components/Avatar";
import { GreenButton } from "../components/GreenButton";
import Link from "next/link";

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
                    <Link href="/new-job">
                        <GreenButton text="Cadastrar Nova Vaga" onClick={() => null} size="large" />
                    </Link>
                    <span className="py-8 text-3xl">SUA VAGAS PUBLICADAS</span>
                </main>
            </div>
        </>
    )
}