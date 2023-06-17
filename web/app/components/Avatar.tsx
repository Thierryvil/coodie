import Image from "next/image";

export function Avatar() {
    return (
        <div>
            <Image
                src="/puc_minas.png"
                alt="avatar"
                width={64}
                height={64}
                className="rounded-full"
            />
        </div>
    )
}