function Calendario() {
  return (
    <section>
      <h1 className="page-title">Calendario</h1>
      <p className="page-subtitle">
        Planifica qué vas a ponerte en tus próximos eventos.
      </p>

      <div className="card">
        <h2 className="card-title">Ejemplo de eventos</h2>
        <ul className="calendar-list">
          <li>
            <strong>20/11</strong> · Comida familiar · Look “Casual comfy”
          </li>
          <li>
            <strong>23/11</strong> · Oficina · Look “Oficina neutra”
          </li>
          <li>
            <strong>25/11</strong> · Cena · Look “Cena especial”
          </li>
        </ul>
      </div>
    </section>
  );
}

export default Calendario;