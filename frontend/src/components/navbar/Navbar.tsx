import {Link} from 'react-router-dom';
import {useAuth} from '@/contexts/AuthContext';

const NavigationBar = () => {
  const {isAuthenticated, logout} = useAuth();

  return (
    <nav className="bg-gray-800 p-4 text-white flex justify-between">
      <div className="flex space-x-4">
        <Link to="/" className="hover:underline">Home</Link>
        <Link to="/upload" className="hover:underline">Upload CSV</Link>
        <Link to="/history" className="hover:underline">Histórico</Link>
      </div>
      <div>
        {isAuthenticated ? (
          <button onClick={logout} className="hover:underline">Logout</button>
        ) : (
          <Link to="/login" className="hover:underline">Login</Link>
        )}
      </div>
    </nav>
  );
};

export default NavigationBar;
