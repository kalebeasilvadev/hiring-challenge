import React, {useState} from 'react';
import axios from 'axios';
import {useAuth} from '@/contexts/AuthContext';
import Modal from "@/components/modal/Modal.tsx";

const UploadCSV = () => {
  const [file, setFile] = useState<File | null>(null);
  const [message, setMessage] = useState('');
  const {token, backendUrl} = useAuth();
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      setFile(event.target.files[0]);
    }
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    try {
      await axios.post(`${backendUrl}/csv/uploadfile`, formData,
        {headers: {'Content-Type': 'multipart/form-data', Authorization: token}});
      setMessage(`Arquivo enviado com sucesso.`);
      setIsModalOpen(true);
    } catch (error) {
      setMessage('Erro ao enviar o arquivo.');
      setIsModalOpen(true);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Upload de Arquivo CSV</h1>
      <form onSubmit={handleSubmit} className="flex flex-col space-y-4">
        <input
          type="file"
          accept=".csv"
          onChange={handleFileChange}
          className="border p-2"
        />
        <button
          type="submit"
          className="bg-blue-500 text-white p-2 rounded hover:bg-blue-700"
        >
          Upload
        </button>
      </form>
      <Modal isOpen={isModalOpen} onClose={closeModal} title="Upload Status">
        <p>{message}</p>
      </Modal>
    </div>
  );
};

export default UploadCSV;
