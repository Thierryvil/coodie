"use client";

import React, { useEffect, useState } from "react";
import { faPenToSquare, faTrash } from "@fortawesome/free-solid-svg-icons";
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

    const fetchPost = async () => {
      const res = await fetch(`${COODIE_API_URL}/jobs`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${session!.user!.access_token}`,
        },
      });

      const response = await res.json();
      setJobs(response);
    };

    fetchPost();
  }, [session]);

  return (
    <>
      {jobs.length > 0 &&
        jobs.map((job: Job) => <JobCard key={job.id} title={job.title} />)}
    </>
  );
}

export function JobCard({ title }: { title: string }) {
  const handleClick = () => {
    const shouldDelete = window.confirm(
      "Tem certeza que deseja deletar o item?"
    );
    if (shouldDelete) {
      console.log("delete");
    }
  };

  return (
    <div className="border border-2 border-gray-300 bg-white mb-10">
      <div className="flex items-center px-4 py-4 justify justify-between">
        <span className="text-2xl">{title}</span>
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
