import React from 'react';

import { GrayButton } from "./GrayButton";
import { GreenButton } from "./GreenButton";
import { Logo } from './Logo';

export function Navbar() {
    return (
        <nav className="flex items-center justify-between py-4 px-8">
            <div className='flex space-x-4 justify-center'>
                <Logo />
                <ul className='flex space-x-8 justify-center'>
                    <li><a href="#">SALÁRIOS</a></li>
                    <li><a href="#">VAGAS</a></li>
                    <li><a href="#">EMPRESAS</a></li>
                </ul>
            </div>
            <div className='flex space-x-4 justify-center'>
                <GrayButton texto="ENTRAR" />
                <GreenButton texto="REGISTRE-SE" />
            </div>
        </nav>
    );
};