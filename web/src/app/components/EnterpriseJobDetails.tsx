import React from "react";
import { faPenToSquare, faTrash } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Link from "next/link";

interface EnterpriseJobDetailsProps {
  title: string;
}

export default function EnterpriseJobDetails({
  title,
}: EnterpriseJobDetailsProps) {
  return (
    <div className="border border-2 border-gray-300 bg-white">
      <div className="flex items-center px-4 py-4 justify justify-between">
        <span className="text-2xl">{title}</span>
        <div className="space-x-4">
          <Link href="/enterprise/timeline/#">
            <FontAwesomeIcon className="w-6 h-6" icon={faPenToSquare} />
          </Link>
          <Link href="/enterprise/timeline/#">
            <FontAwesomeIcon className="w-6 h-6 text-red-500" icon={faTrash} />
          </Link>
        </div>
      </div>
    </div>
  );
}
