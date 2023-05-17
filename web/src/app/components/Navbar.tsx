'use client'

import React from 'react';
import { IdentifyUserModal } from './IdentifyUserModal';
import { GrayButton } from "./GrayButton";
import { GreenButton } from "./GreenButton";
import { Logo } from './Logo';
import { useState } from 'react';
import Link from 'next/link';

export function Navbar() {
    const [isOpen, setIsOpen] = useState(false);

    const openModal = () => {
        setIsOpen(true);
    };

    const closeModal = () => {
        setIsOpen(false);
    };

    return (
        <nav className="flex items-center justify-between py-4 px-8">
            <div className='flex space-x-4 justify-center'>
                <Logo />
                <ul className='flex space-x-8 items-center'>
                    <li><a href="#">SALÁRIOS</a></li>
                    <li><a href="#">VAGAS</a></li>
                    <li><a href="#">EMPRESAS</a></li>
                </ul>
            </div>
            <div className='flex space-x-4 justify-center'>
                <Link href="/login">
                    <GrayButton texto="ENTRAR" onClick={() => null} />
                </Link>
                <IdentifyUserModal isOpen={isOpen} closeModal={closeModal} />
                <GreenButton texto="REGISTRE-SE" onClick={openModal} />
            </div>
        </nav>
    );
};