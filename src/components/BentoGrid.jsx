import React, { useState } from 'react';

const services = [
  {
    icon: "🛒",
    title: "E-commerce",
    description: "Tiendas Online que Venden. UX probada.",
    fullDetail: "Optimizamos el checkout para reducir abandonos en un 40%. Integración con MercadoPago y logística automática.",
    badge: "Más solicitado",
    featured: true
  },
  {
    icon: "🌐",
    title: "Posicionamiento",
    description: "Aparecés donde tu cliente te busca (SEO/SEM).",
    fullDetail: "Auditamos más de 200 factores técnicos para que tu PyME domine la búsqueda en Google Maps y Zárate."
  },
  {
    icon: "⚡",
    title: "Automatización",
    description: "Marketing 24/7 sin escalar costos.",
    fullDetail: "Configuramos Chatbots y Secuencias de Email que nutren a tus prospectos mientras dormís."
  },
  {
    icon: "📲",
    title: "Social Media",
    description: "Contenido que genera comunidad real.",
    fullDetail: "Estrategias segmentadas por sector: Industrial, Logística o Consumo Masivo."
  },
  {
    icon: "📊",
    title: "Analítica",
    description: "Datos reales que deciden el próximo paso.",
    fullDetail: "Dashboards personalizados en Looker Studio para ver el ROI en tiempo real."
  },
  {
    icon: "🚀",
    title: "Consultoría",
    description: "Crecimiento en 90 días con plan maestro.",
    fullDetail: "Acompañamiento estratégico semanal para ajustar el rumbo basado en métricas."
  }
];

export default function BentoGrid() {
  const [selected, setSelected] = useState(null);

  return (
    <div className="bento" role="list">
      {services.map((s, i) => (
        <article 
          key={i}
          className={`bc ${s.featured ? 'bc-feat' : ''} ${selected === i ? 'bc-active' : ''}`}
          onClick={() => setSelected(selected === i ? null : i)}
          role="listitem"
          style={{ transition: 'all 0.4s' }}
        >
          <div className="bc-icon">{s.icon}</div>
          <h3 className="bc-t">{s.title}</h3>
          <p className="bc-d">{selected === i ? s.fullDetail : s.description}</p>
          
          {s.badge && <div className="bc-badge">{s.badge}</div>}
          
          <div className="bc-action">
            {selected === i ? 'Resumir -' : 'Saber más +'}
          </div>

          {/* Glow effect on hover/active */}
          {selected === i && (
            <div className="bc-glow"></div>
          )}
        </article>
      ))}
    </div>
  );
}
