import {Route, Routes} from 'react-router-dom';
import UploadCSV from '@/components/upload/UploadCSV.tsx';
import UploadHistory from '@/components/history/UploadHistory.tsx';
import Login from "@/components/login/Login.tsx";
import Home from "@/components/home/Home.tsx";
import NavigationBar from "@/components/navbar/Navbar.tsx";
import {AuthProvider} from "@/contexts/AuthContext.tsx";
import PrivateRoute from "@/components/PrivateRoute.tsx";

const App = () => {
  return (
    <AuthProvider>
      <NavigationBar/>
      <Routes>
        <Route path="/" element={<Login/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route element={<PrivateRoute/>}>
          <Route path="/upload" element={<UploadCSV/>}/>
          <Route path="/history" element={<UploadHistory/>}/>
          <Route path="/home" element={<Home/>}/>
        </Route>
      </Routes>
    </AuthProvider>
  );
};
export default App;
