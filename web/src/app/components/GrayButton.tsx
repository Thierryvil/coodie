interface GrayButtonProps {
    texto: string
}

export function GrayButton({ texto }: GrayButtonProps) {
    return (
        <button className="w-32 h-10 text-sm font-bold bg-gray-300 border-none">
            {texto}
        </button>
    );
}