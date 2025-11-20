import { Link } from "react-router-dom";

function Login() {
  return (
    <div className="auth-wrapper">
      <div className="auth-card">
        <h1 className="auth-title">Inicia sesión</h1>
        <p className="auth-subtitle">Accede a tu armario digital MyWebdrob</p>

        <form className="auth-form">
          <label>
            Usuario
            <input type="text" placeholder="Nombre de usuario" />
          </label>
          <label>
            Contraseña
            <input type="password" placeholder="••••••••" />
          </label>
          <button type="submit" className="btn-primary">
            Entrar
          </button>
        </form>

        <p className="auth-footer">
          ¿No tienes cuenta?{" "}
          <Link to="/register" className="auth-link">
            Regístrate
          </Link>
        </p>
      </div>
    </div>
  );
}

export default Login;