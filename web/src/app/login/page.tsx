'use client'

import React, { useState } from 'react';
import { Logo } from '../components/Logo';
import '../global.css';
import { GreenButton } from '../components/GreenButton';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEye, faEyeSlash } from '@fortawesome/free-solid-svg-icons';
import Link from 'next/link';

export default function Login() {
    const [showPassword, setShowPassword] = useState(false);

    const handleTogglePassword = () => {
        setShowPassword(!showPassword);
    };

    return (
        <>
            <nav className="py-4 px-8">
                <Link href="/">
                    <Logo />
                </Link>
            </nav>
            <div className="flex flex-col items-center bg-gray-100 h-screen justify-between">
                <main className="flex flex-col items-center flex-grow">
                    <span className="text-4xl text-center mt-8 mb-4">
                        Entre em nossa plataforma
                    </span>
                    <div className="flex flex-col py-10 px-10 border border-gray-300 bg-white w-[600px] h-[435px]">
                        <label htmlFor="email">E-mail:</label>
                        <input
                            className="border border-gray-500 border-2 px-2 py-2"
                            type="email"
                            name="email"
                            id="email"
                        />
                        <label htmlFor="password">Senha:</label>
                        <input
                            className="border border-gray-500 border-2 py-2 px-3 pr-10"
                            type={showPassword ? 'text' : 'password'}
                            name="password"
                            id="password"
                        />
                        <div className="relative">
                            <span
                                className="absolute top-1/2 transform -translate-y-8 right-3 cursor-pointer"
                                onClick={handleTogglePassword}
                            >
                                <FontAwesomeIcon
                                    icon={showPassword ? faEyeSlash : faEye}
                                    size="lg"
                                />
                            </span>
                        </div>
                        <label className='text-right text-sm'>Esqueceu sua senha?</label>
                        <div className='flex flex-col items-center py-20'>
                            <GreenButton text="Entrar" onClick={() => null} size='large' />
                            <span className='text-sm'>Não possui conta? Registre-se agora</span>
                        </div>
                    </div>
                </main>
            </div>
        </>
    );
}
