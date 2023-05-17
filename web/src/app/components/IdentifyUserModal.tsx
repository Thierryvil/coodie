import ReactModal from 'react-modal';
import React from 'react';
import Image from 'next/image';
import { GrayButton } from './GrayButton';

interface ModalProps {
    isOpen: boolean,
    closeModal: () => void
}

export function IdentifyUserModal({ isOpen, closeModal }: ModalProps) {
    const modalStyle = {
        content: {
            width: '500px',
            height: '350px',
            margin: 'auto'
        }
    };
    return (
        <div>
            <ReactModal
                isOpen={isOpen}
                onRequestClose={closeModal}
                style={modalStyle}
            >
                <div className='flex flex-col items-center justify-center'>
                    <Image src='/welcome.svg' alt="welcome" width='460' height='220' />
                    <div className='flex space-x-4 mt-5'>
                        <GrayButton texto='Sou Candidato' onClick={() => null} />
                        <GrayButton texto='Sou Empresa' onClick={() => null} />
                    </div>
                </div>
            </ReactModal>
        </div>
    );
};