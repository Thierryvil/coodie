import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faInstagram, faFacebookF, faTwitter } from '@fortawesome/free-brands-svg-icons';

export function Footer() {
    return (
        <footer className="bg-gray-300 py-4">
            <div className="flex-col items-center justify-center">
                <div className='flex space-x-4 items-center justify-center mb-4'>
                    <a href="#">
                        <FontAwesomeIcon className='w-8 h-8' icon={faFacebookF} />
                    </a>
                    <a href="#">
                        <FontAwesomeIcon className='w-8 h-8' icon={faInstagram} />
                    </a>
                    <a href="#">
                        <FontAwesomeIcon className='w-8 h-8' icon={faTwitter} />
                    </a>
                </div>
                <p className="text-sm text-center">coodie © 2023 - Todos os direitos reservados</p>
            </div>
        </footer>
    );
}