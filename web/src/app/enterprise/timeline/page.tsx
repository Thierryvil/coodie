"use client";

import React from "react";
import { Logo } from "../../components/Logo";
import { Avatar } from "../../components/Avatar";
import { GreenButton } from "../../components/GreenButton";
import Link from "next/link";
import EnterpriseJobDetails from "../../components/EnterpriseJobDetails";
import "../../global.css";

export default function EnterpriseTimeline() {
  return (
    <>
      <nav className="flex items-center justify-between py-4 px-8">
        <div className="mr-auto">
          <Logo />
        </div>
        <Avatar />
      </nav>
      <div className="bg-gray-100 h-screen">
        <main className="flex flex-col py-8 px-16">
          <Link href="/enterprise/add-new-job">
            <GreenButton text="Cadastrar Nova Vaga" size="large" />
          </Link>
          <span className="py-8 text-3xl">SUA VAGAS PUBLICADAS</span>
          <EnterpriseJobDetails title="Desenvolvedor FullStack na PUC Minas" />
        </main>
      </div>
    </>
  );
}
