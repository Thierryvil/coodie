"use client";

import React from "react";
import Image from "next/image";
import { GreenButton } from "./GreenButton";

export function JobBox() {
  return (
    <div className="flex flex-col bg-white w-[360px] h-[360px] border border-gray-300 py-4">
      <div className="flex flex-col items-center">
        <span>Desenvolvedor Full Stack na PUC MINAS</span>
      </div>
      <div className="flex flex-col items-center mt-10">
        <Image
          src="/puc_minas.png"
          alt="logo puc minas"
          width="150"
          height="150"
        />
      </div>
      <div className="flex flex-col items-center justify-between mt-auto">
        <GreenButton text="VER VAGA" onClick={() => null} size="medium" />
      </div>
    </div>
  );
}
