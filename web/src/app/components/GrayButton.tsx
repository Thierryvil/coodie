interface GrayButtonProps {
    text: string
    onClick: () => void,
}

export function GrayButton({ text, onClick }: GrayButtonProps) {
    return (
        <button onClick={onClick} className="w-32 h-10 text-sm font-bold bg-gray-300 border-none">
            {text}
        </button>
    );
}