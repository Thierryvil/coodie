interface GreenButtonProps {
    texto: string,
    onClick: () => void,
}

export function GreenButton({ texto, onClick }: GreenButtonProps) {
    return (
        <button onClick={onClick} className="w-32 h-10 text-sm font-bold text-white bg-green-700 border-none">
            {texto}
        </button>
    );
}