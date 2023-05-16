import React from 'react';

interface GreenButtonProps {
    texto: string
}

export function GreenButton({ texto }: GreenButtonProps) {
    return (
        <button className="w-32 h-10 text-sm font-bold text-white bg-green-700 border-none">{texto}</button>
    );
}