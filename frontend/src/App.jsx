import { Routes, Route, Navigate } from "react-router-dom";
import Layout from "./components/Layout.jsx";
import Login from "./pages/Login.jsx";
import Register from "./pages/Register.jsx";
import Dashboard from "./pages/Dashboard.jsx";
import Prendas from "./pages/Prendas.jsx";
import Looks from "./pages/Looks.jsx";
import Calendario from "./pages/Calendario.jsx";
import Comunidad from "./pages/Comunidad.jsx";

function App() {
  return (
    <Routes>
      {/* Páginas públicas */}
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />

      {/* Parte "privada" (de momento sin auth real en el front) */}
      <Route
        path="/"
        element={
          <Layout>
            <Dashboard />
          </Layout>
        }
      />
      <Route
        path="/prendas"
        element={
          <Layout>
            <Prendas />
          </Layout>
        }
      />
      <Route
        path="/looks"
        element={
          <Layout>
            <Looks />
          </Layout>
        }
      />
      <Route
        path="/calendario"
        element={
          <Layout>
            <Calendario />
          </Layout>
        }
      />
      <Route
        path="/comunidad"
        element={
          <Layout>
            <Comunidad />
          </Layout>
        }
      />

      {/* Cualquier otra ruta → home */}
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}

export default App;
