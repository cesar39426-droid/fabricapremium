import { TestimonialCard } from "@/components/ui/testimonial-cards";
import { useState } from "react";

const testimonials = [
  {
    id: 12,
    testimonial: "La integración de la IA de NubeN automatizó nuestro funnel de ventas un 300%. Era nuestra tarea pendiente y la resolvieron con tecnología de vanguardia.",
    author: "Federico - VCP Tech"
  },
  {
    id: 33,
    testimonial: "Pocas agencias entienden realmente el desarrollo WebGL de alto rendimiento. Fábrica Premium logró llevar nuestra marca al 'Living Web' con éxito.", 
    author: "Lucas - NextGen Logistics"
  },
  {
    id: 68,
    testimonial: "El equipo arquitectónico excedió los parámetros B2B. Sus agentes IA han sustituido gran parte del soporte Tier 1 para nuestra base de clientes.",
    author: "Mariana R. - AI Startups"
  }
];

type PositionType = "front" | "middle" | "back";

export default function DemoTestimonialCards() {
  const [positions, setPositions] = useState<PositionType[]>(["front", "middle", "back"]);

  const handleShuffle = () => {
    setPositions((prevPositions) => {
        const newPositions = [...prevPositions];
        const last = newPositions.pop();
        if(last) newPositions.unshift(last);
        return newPositions;
    });
  };

  return (
    <div className="grid place-content-center overflow-hidden bg-black px-8 py-24 text-slate-50 min-h-screen h-full w-full">
      <div className="relative -ml-[100px] h-[450px] w-[350px] md:-ml-[175px]">
        {testimonials.map((testimonial, index) => (
          <TestimonialCard
            key={testimonial.id}
            {...testimonial}
            handleShuffle={handleShuffle}
            position={positions[index]}
          />
        ))}
      </div>
    </div>
  );
}
