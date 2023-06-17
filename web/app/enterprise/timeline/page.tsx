import React from "react";
import "../../global.css";
import { Logo } from "../../components/Logo";
import { Avatar } from "../../components/Avatar";
import Link from "next/link";
import { GreenButton } from "../../components/GreenButton";
import EnterpriseJobDetails from "../../components/EnterpriseJobDetails";
import { getServerSession } from "next-auth";

export default async function EnterpriseTimeline() {
  const data = await getServerSession();

  if (!data) {
    return <h1 className="text-center text-3xl">Access Denied</h1>;
  }

  return (
    <>
      <nav className="flex items-center justify-between py-4 px-8">
        <div className="mr-auto">
          <Logo />
        </div>
        <Avatar />
      </nav>
      <div className="bg-gray-100 h-screen">
        <main className="flex flex-col py-8 px-16 bg-gray-100 ">
          <Link href="/enterprise/add-new-job">
            <GreenButton text="Cadastrar Nova Vaga" size="large" />
          </Link>
          <span className="py-8 text-3xl">SUA VAGAS PUBLICADAS</span>
          <div>
            <EnterpriseJobDetails />
          </div>
        </main>
      </div>
    </>
  );
}
