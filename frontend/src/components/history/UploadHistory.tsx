import {useEffect, useState} from 'react';
import axios from 'axios';
import {useAuth} from '@/contexts/AuthContext';
import Modal from "@/components/modal/Modal.tsx";

const UploadHistory = () => {
  const [history, setHistory] = useState<any[]>([]);
  const [selectedHistory, setSelectedHistory] = useState<any | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const {token} = useAuth();


  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const response = await axios.get('http://localhost:8050/history/uploads',
          {headers: {Authorization: token}});
        setHistory(response.data);
      } catch (error) {
        console.error('Erro ao buscar histórico de uploads:', error);
      }
    };

    fetchHistory();
  }, []);

  const closeModal = () => {
    setIsModalOpen(false);
    setSelectedHistory(null);
  };

  const handleItemClick = async (id: number) => {
    try {
      const response = await axios.get(`http://localhost:8050/history/processing?id=${id}`,
        {headers: {Authorization: token}});
      setSelectedHistory(response.data);
      setIsModalOpen(true);
    } catch (error) {
      console.error('Erro ao buscar detalhes do histórico:', error);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Histórico de Uploads</h1>
      {history.map((item) => (
        <div key={item.id} className="border p-4 mb-4 rounded"
             onClick={() => handleItemClick(item.history_id)}>
          <p><strong>Arquivo:</strong> {item.filename}</p>
          <p><strong>Tamanho:</strong> {item.rows} linhas</p>
          <p><strong>Arquivo:</strong> {item.upload_time}</p>
        </div>
      ))}
      {selectedHistory && (
        <Modal isOpen={isModalOpen} onClose={closeModal} title="Detalhes do Upload">
          <p><strong>ID:</strong> {selectedHistory.id}</p>
          <p><strong>Status:</strong> {selectedHistory.status}</p>
          <p><strong>Sucess :</strong> {selectedHistory.success_count}</p>
          <p><strong>Failure :</strong> {selectedHistory.failure_count}</p>
          <p><strong>Size :</strong> {selectedHistory.size}</p>
        </Modal>
      )}
    </div>
  );
};

export default UploadHistory;
