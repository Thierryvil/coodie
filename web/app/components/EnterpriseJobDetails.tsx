"use client";

import React, { useEffect, useState } from "react";
import { faTrash } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Link from "next/link";
import { useSession } from "next-auth/react";
import { COODIE_API_URL } from "../constants";

type Job = {
  id: number;
  title: string;
};

export default function EnterpriseJobDetails() {
  const [jobs, setJobs] = useState<Job[]>([]);
  const { data: session } = useSession();

  useEffect(() => {
    if (!session) return;

    const fetchJobs = async () => {
      const res = await fetch(`${COODIE_API_URL}/jobs`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${session!.user!.access_token}`,
        },
      });

      const response = await res.json();
      setJobs(response);
    };

    fetchJobs();
  }, [session]);

  const deleteJob = async (id: number) => {
    try {
      const res = await fetch(`${COODIE_API_URL}/jobs/${id}`, {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${session!.user!.access_token}`,
        },
      });

      if (res.ok) {
        const updatedJobs = jobs.filter((job) => job.id !== id);
        setJobs(updatedJobs);
      } else {
        throw new Error("Erro ao deletar o trabalho");
      }
    } catch (error) {
      console.error(error);
      throw new Error("Erro ao deletar o trabalho");
    }
  };

  return (
    <>
      {jobs.length > 0 &&
        jobs.map((job: Job) => (
          <JobCard key={job.id} job={job} deleteJob={deleteJob} />
        ))}
    </>
  );
}

export function JobCard({
  job,
  deleteJob,
}: {
  job: Job;
  deleteJob: (id: number) => void;
}) {
  const handleClick = () => {
    const shouldDelete = window.confirm(
      "Tem certeza que deseja deletar o item?"
    );
    if (shouldDelete) {
      deleteJob(job.id);
    }
  };

  return (
    <div className="border border-2 border-gray-300 bg-white mb-10">
      <div className="flex items-center px-4 py-4 justify justify-between">
        <span className="text-2xl">{job.title}</span>
        <div className="space-x-4">
          <button onClick={handleClick}>
            <Link href="/enterprise/timeline/#">
              <FontAwesomeIcon
                className="w-6 h-6 text-red-500"
                icon={faTrash}
              />
            </Link>
          </button>
        </div>
      </div>
    </div>
  );
}
