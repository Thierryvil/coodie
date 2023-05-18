interface GreenButtonProps {
    text: string;
    onClick: () => void;
    size?: 'small' | 'medium' | 'large';
}

export function GreenButton({ text, onClick, size }: GreenButtonProps) {
    let sizeClass = '';

    if (size === 'small') {
        sizeClass = 'w-20 h-8';
    } else if (size === 'medium') {
        sizeClass = 'w-32 h-10';
    } else if (size === 'large') {
        sizeClass = 'w-[488px] h-[51px]';
    }

    return (
        <button
            onClick={onClick}
            className={`text-sm font-bold text-white bg-green-700 border-none ${sizeClass}`}
        >
            {text}
        </button>
    );
}