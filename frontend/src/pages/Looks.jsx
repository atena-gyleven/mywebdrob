function Looks() {
  return (
    <section>
      <h1 className="page-title">Looks</h1>
      <p className="page-subtitle">
        Combina tus prendas favoritas y guarda tus looks para diferentes
        ocasiones.
      </p>

      <div className="toolbar">
        <button className="btn-secondary">Nuevo look</button>
      </div>

      <div className="grid-3">
        <div className="card">
          <h2 className="card-title">Look oficina</h2>
          <p>Blazer beige, pantalón negro, blusa blanca, mocasines.</p>
        </div>
        <div className="card">
          <h2 className="card-title">Look finde</h2>
          <p>Vaqueros, camiseta oversize y deportivas.</p>
        </div>
        <div className="card">
          <h2 className="card-title">Cena especial</h2>
          <p>Vestido negro, tacones y abrigo largo.</p>
        </div>
      </div>
    </section>
  );
}

export default Looks;