"use client";

import { Logo } from "../../components/Logo";
import { Avatar } from "../../components/Avatar";
import { GreenButton } from "../../components/GreenButton";
import Link from "next/link";
import "../../global.css";
import React, { FormEvent, useState } from "react";
import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import ErrorPopup from "../../components/ErrorPopup";
import { COODIE_API_URL } from "../../constants";

interface Job {
  title: string;
  description: string;
  location: string[];
  seniority: string[];
  regime: string[];
}

const regimes = ["CLT", "PJ"];
const seniorities = ["Junior", "Pleno", "Senior"];
const locations = ["Remoto", "Hibrido", "Presencial"];

export default function NewJob() {
  const { data: session } = useSession();
  const { push } = useRouter();
  const [error, setError] = useState<string | null>(null);
  const [regime, setRegime] = useState(Array(3).fill(false));
  const [seniority, setSeniority] = useState(Array(3).fill(false));
  const [location, setLocation] = useState(Array(3).fill(false));

  if (!session) {
    return <h1 className="text-center text-3xl">Access Denied</h1>;
  }

  const handleRegimeCheckboxChange = (index: number) => {
    const updatedCheckboxes = [...regime];
    updatedCheckboxes[index] = !updatedCheckboxes[index];
    setRegime(updatedCheckboxes);
  };

  const handleSeniorityCheckboxChange = (index: number) => {
    const updatedCheckboxes = [...seniority];
    updatedCheckboxes[index] = !updatedCheckboxes[index];
    setSeniority(updatedCheckboxes);
  };

  const handleLocationCheckboxChange = (index: number) => {
    const updatedCheckboxes = [...location];
    updatedCheckboxes[index] = !updatedCheckboxes[index];
    setLocation(updatedCheckboxes);
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const job: Job = {
      title: e.currentTarget.titleInput.value,
      description: e.currentTarget.description.value,
      location: location
        .map((selected, index) =>
          selected ? locations[index].toLowerCase() : ""
        )
        .filter((item) => item !== ""),
      seniority: seniority
        .map((selected, index) =>
          selected ? seniorities[index].toLowerCase() : ""
        )
        .filter((item) => item !== ""),
      regime: regime
        .map((selected, index) =>
          selected ? regimes[index].toLowerCase() : ""
        )
        .filter((item) => item !== ""),
    };

    const response = await sendNewJobRequest(job);
    if (!response.ok) {
      setError("Ocorreu um erro!");
      return;
    }
    push("/enterprise/timeline");
  };

  const sendNewJobRequest = async (job: Job) => {
    console.log(job);
    const response = await fetch(`${COODIE_API_URL}/jobs`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${session!.user!.access_token!}`,
      },
      body: JSON.stringify(job),
    });

    return response;
  };

  const handleCloseError = () => {
    setError(null);
  };

  return (
    <>
      {error && <ErrorPopup message={error} onClose={handleCloseError} />}
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
            <label htmlFor="titleInput">Titulo</label>
            <input
              className="py-2 px-2 border border-2 border-gray-500 w-[1280px]"
              type="text"
              id="titleInput"
              name="titleInput"
            />

            <span className="mt-8">Tipo da vaga</span>
            <div className="flex space-x-8">
              {locations.map((location, index) => (
                <div key={index}>
                  <label className="flex items-center">
                    <input
                      type="checkbox"
                      className="mr-2"
                      onChange={() => handleLocationCheckboxChange(index)}
                    />
                    {location}
                  </label>
                </div>
              ))}
            </div>

            <span className="mt-8">Nível de senioridade</span>
            <div className="flex space-x-8">
              {seniorities.map((seniority, index) => (
                <div key={index}>
                  <label className="flex items-center">
                    <input
                      type="checkbox"
                      className="mr-2"
                      onChange={() => handleSeniorityCheckboxChange(index)}
                    />
                    {seniority}
                  </label>
                </div>
              ))}
            </div>

            <span className="mt-8">Regime de trabalho</span>
            <div className="flex space-x-8">
              {regimes.map((regime, index) => (
                <div key={index}>
                  <label className="flex items-center">
                    <input
                      type="checkbox"
                      className="mr-2"
                      onChange={() => handleRegimeCheckboxChange(index)}
                    />
                    {regime}
                  </label>
                </div>
              ))}
            </div>

            <span className="mt-8 mb-2">Descrição da vaga</span>
            <textarea
              className="px-2 py-2 border border-2 border-gray-500 w-[1280px] h-[546px] mb-4"
              name="description"
              id="description"
            ></textarea>
            <GreenButton text="Publicar" size="medium" />
          </form>
        </main>
      </div>
    </>
  );
}
