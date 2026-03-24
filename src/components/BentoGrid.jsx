import React, { useState } from 'react';

const services = [
  {
    icon: "🛒",
    title: "Tiendas Nube",
    description: "E-commerce con todo integrado. Listo para vender desde el día 1.",
    fullDetail: "Tiendas Nube conectadas a MercadoPago, WhatsApp, Instagram y Google Shopping. UX optimizada para reducir abandonos de carrito hasta un 40%.",
    badge: "Más solicitado",
    featured: true
  },
  {
    icon: "🌐",
    title: "Sitios Ultra-Conversión",
    description: "Páginas que convierten visitas en clientes reales.",
    fullDetail: "Diseño único por cliente. Mobile-first, carga en menos de 2 segundos. Optimizado para que cada visita tenga un próximo paso claro hacia la compra."
  },
  {
    icon: "🔍",
    title: "SEO & Visibilidad",
    description: "Aparecés donde tu cliente te busca en Google.",
    fullDetail: "Posicionamiento orgánico local y nacional. Auditoría de 200+ factores técnicos. Resultados medibles en los primeros 90 días."
  },
  {
    icon: "⚡",
    title: "Marketing con IA",
    description: "Automatización 24/7 — tu vendedor digital que nunca duerme.",
    fullDetail: "Chatbots, secuencias de email y campañas automáticas que nutren prospectos y cierran ventas mientras te enfocás en tu negocio."
  },
  {
    icon: "📊",
    title: "Resultados Medibles",
    description: "Datos reales, no suposiciones.",
    fullDetail: "Dashboard en tiempo real para ver tu ROI. Reportes semanales con métricas que importan: ventas generadas, leads, costo por cliente."
  },
  {
    icon: "🤖",
    title: "Integración con IA",
    description: "Tecnología de punta aplicada a tu negocio.",
    fullDetail: "Integramos asistentes de IA, automatizaciones de CRM y flujos inteligentes que escalan tu operación sin escalar tus costos."
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

          {selected === i && (
            <div className="bc-glow"></div>
          )}
        </article>
      ))}
    </div>
  );
}
