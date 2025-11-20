function Dashboard() {
  return (
    <section>
      <h1 className="page-title">Resumen</h1>
      <p className="page-subtitle">
        Una vista rápida de tu armario, looks y próximos eventos.
      </p>

      <div className="grid-3">
        <div className="card">
          <h2 className="card-title">Prendas guardadas</h2>
          <p className="card-number">128</p>
          <p className="card-note">Organizadas por categoría y temporada.</p>
        </div>
        <div className="card">
          <h2 className="card-title">Looks creados</h2>
          <p className="card-number">24</p>
          <p className="card-note">Para trabajo, ocio y eventos.</p>
        </div>
        <div className="card">
          <h2 className="card-title">Eventos esta semana</h2>
          <p className="card-number">3</p>
          <p className="card-note">Planifica qué ponerte con antelación.</p>
        </div>
      </div>
    </section>
  );
}

export default Dashboard;