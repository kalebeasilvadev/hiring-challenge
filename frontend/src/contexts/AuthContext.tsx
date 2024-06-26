import React, {createContext, useContext, useState} from 'react';
import axios from "axios";


interface AuthContextType {
  isAuthenticated: boolean;
  login: (username: string, password: string) => void;
  logout: () => void;
  token?: string;
  backendUrl?: string;
}

interface AuthProviderProps {
  children: React.ReactNode;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<AuthProviderProps> = ({children}) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [token, setToken] = useState('');
  const backendUrl = import.meta.env.VITE_BACKEND_URL;


  const login = (username: string, password: string) => {
    axios.post(`${backendUrl}/auth/token`, {username, password})
      .then((response) => {
        setToken(`${response.data.token_type} ${response.data.access_token}`);
        setIsAuthenticated(true);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  const logout = () => {
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{isAuthenticated, login, logout, token, backendUrl}}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
