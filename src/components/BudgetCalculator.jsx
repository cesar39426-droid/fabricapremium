import React, { useState } from 'react';

const industries = [
  { id: 'ecommerce', name: 'E-commerce & Retail Pro', factor: 1.4, icon: '🛒' },
  { id: 'logistica', name: 'Logística & Puertos (Zárate)', factor: 1.2, icon: '🚢' },
  { id: 'pyme_industrial', name: 'PyME Industrial / Servicios', factor: 1.1, icon: '🏗️' },
  { id: 'servicios_profesionales', name: 'Servicios Profesionales de Élite', factor: 1.3, icon: '🏢' },
  { id: 'startup', name: 'Startups & Tech Founders', factor: 1.5, icon: '🚀' },
];

export default function BudgetCalculator() {
  const [industry, setIndustry] = useState(industries[4]);
  const [size, setSize] = useState(500); // M2 o transacciones
  const [isCalculating, setIsCalculating] = useState(false);
  const [result, setResult] = useState(null);

  const handleCalculate = () => {
    setIsCalculating(true);
    setResult(null);
    setTimeout(() => {
      const basePrice = 150000;
      const finalPrice = Math.round(basePrice * industry.factor + (size * 50));
      setResult(finalPrice);
      setIsCalculating(false);
    }, 1200);
  };

  return (
    <div className="calc-container" style={{ padding: '3rem', background: 'rgba(255,255,255,0.02)', borderRadius: '32px', border: '1px solid rgba(255,255,255,0.08)' }}>
      <h3 style={{ marginBottom: '2rem', fontFamily: 'Syne', fontSize: '1.8rem' }}>Calculador de Inversión <span className="grad-text">Digital</span></h3>
      
      <div className="calc-grid" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>
        <div className="calc-inputs">
          <label style={{ display: 'block', marginBottom: '10px', fontSize: '0.8rem', opacity: 0.6 }}>Tu Sector Industrial</label>
          <select 
            value={industry.id}
            onChange={(e) => setIndustry(industries.find(i => i.id === e.target.value))}
            style={{ width: '100%', padding: '15px', background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)', color: '#fff', borderRadius: '12px', marginBottom: '1.5rem', outline: 'none' }}
          >
            {industries.map(i => <option key={i.id} value={i.id}>{i.icon} {i.name}</option>)}
          </select>

          <label style={{ display: 'block', marginBottom: '10px', fontSize: '0.8rem', opacity: 0.6 }}>Nivel de Operación (Ej. Clientes/Mes)</label>
          <input 
            type="range" min="100" max="10000" step="100"
            value={size}
            onChange={(e) => setSize(parseInt(e.target.value))}
            style={{ width: '100%', accentColor: 'var(--safety-orange)', marginBottom: '1.5rem' }}
          />
          <div style={{ textAlign: 'right', fontSize: '0.9rem', color: 'var(--safety-orange)', fontWeight: 800 }}>{size} op/mes</div>
        </div>

        <div className="calc-results" style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', borderLeft: '1px solid rgba(255,255,255,0.05)', paddingLeft: '2rem' }}>
          {isCalculating ? (
            <div className="loading-spinner">Calculando estimación...</div>
          ) : result ? (
            <div style={{ textAlign: 'center' }}>
              <span style={{ fontSize: '0.8rem', opacity: 0.5 }}>Inversión Estimada</span>
              <div style={{ fontSize: '3rem', fontWeight: 800, fontFamily: 'Syne', margin: '10px 0' }} className="grad-text">
                ${result.toLocaleString('es-AR')}
              </div>
              <p style={{ fontSize: '0.85rem', color: 'rgba(255,255,255,0.4)', marginBottom: '1.5rem' }}>
                *Sujeto a auditoría técnica preliminar (SOP V2).
              </p>
              <button className="btn btn-primary" onClick={() => window.location.href = '#contacto'}>Reservar Auditoría →</button>
            </div>
          ) : (
            <button className="btn btn-ghost" onClick={handleCalculate} style={{ width: '100%' }}>Simular Estrategia</button>
          )}
        </div>
      </div>
    </div>
  );
}
