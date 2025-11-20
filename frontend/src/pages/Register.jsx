import { Link } from "react-router-dom";

function Register() {
  return (
    <div className="auth-wrapper">
      <div className="auth-card">
        <h1 className="auth-title">Crear cuenta</h1>
        <p className="auth-subtitle">Empieza a organizar tu armario</p>

        <form className="auth-form">
          <label>
            Usuario
            <input type="text" placeholder="Nombre de usuario" />
          </label>
          <label>
            Email
            <input type="email" placeholder="tucorreo@example.com" />
          </label>
          <label>
            Contraseña
            <input type="password" placeholder="••••••••" />
          </label>
          <button type="submit" className="btn-primary">
            Registrarme
          </button>
        </form>

        <p className="auth-footer">
          ¿Ya tienes cuenta?{" "}
          <Link to="/login" className="auth-link">
            Inicia sesión
          </Link>
        </p>
      </div>
    </div>
  );
}

export default Register;