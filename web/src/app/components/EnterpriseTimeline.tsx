import Link from "next/link"
import React from "react"
import { Logo } from "./Logo"

export function EnterpriseTimeLine() {
    return (
        <nav>
            <Link href="/">
                <Logo />
            </Link>
        </nav>
    )
}