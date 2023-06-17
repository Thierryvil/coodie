import ReactModal from "react-modal";

type ErrorPopup = {
  message: string;
  onClose: () => void;
};

export default function ErrorPopup({ message, onClose }: ErrorPopup) {
  return (
    <ReactModal
      isOpen={true}
      onRequestClose={onClose}
      contentLabel="Erro"
      className="flex items-center justify-center"
      overlayClassName="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center"
    >
      <div className="bg-white rounded p-4 text-center">
        <h2 className="text-red-500 text-lg font-bold mb-2">Erro</h2>
        <p>{message}</p>
        <button
          className="mt-4 px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600"
          onClick={onClose}
        >
          Fechar
        </button>
      </div>
    </ReactModal>
  );
}
