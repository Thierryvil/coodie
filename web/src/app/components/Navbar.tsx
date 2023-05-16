import React from 'react';

import { GrayButton } from "./GrayButton";
import { GreenButton } from "./GreenButton";

export function Navbar() {
    return (
        <nav className="flex items-center justify-between py-4 px-8">
            <div className='flex space-x-4 justify-center'>
                <span className="text-4xl font-bold">coodie</span>
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