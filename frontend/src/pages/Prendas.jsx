function Prendas() {
  return (
    <section>
      <h1 className="page-title">Mi armario</h1>
      <p className="page-subtitle">
        Visualiza y organiza las prendas que has añadido a MyWebdrob.
      </p>

      <div className="toolbar">
        <input className="input" placeholder="Buscar por color, estilo..." />
        <button className="btn-secondary">Añadir prenda</button>
      </div>

      <div className="grid-4">
        <div className="card prenda-card">
          <div className="prenda-thumbnail" />
          <div className="prenda-info">
            <h2>Cazadora vaquera</h2>
            <p>Casual · Primavera · Azul</p>
          </div>
        </div>
        <div className="card prenda-card">
          <div className="prenda-thumbnail" />
          <div className="prenda-info">
            <h2>Vestido negro</h2>
            <p>Elegante · Todo el año · Negro</p>
          </div>
        </div>
        <div className="card prenda-card">
          <div className="prenda-thumbnail" />
          <div className="prenda-info">
            <h2>Zapatillas blancas</h2>
            <p>Casual · Verano · Blanco</p>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Prendas;