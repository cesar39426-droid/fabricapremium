import { GlowCard } from "@/components/ui/spotlight-card";

export default function DemoSpotlightCard() {
  return (
    <div className="w-full flex-wrap sm:w-screen sm:h-screen flex flex-row items-center justify-center p-8 gap-10 custom-cursor bg-black text-white">
      <GlowCard glowColor="blue">
        <h3 className="text-xl font-bold font-syne text-center mt-10">Servicios Pro</h3>
      </GlowCard>
      <GlowCard glowColor="purple">
        <h3 className="text-xl font-bold font-syne text-center mt-10">Cloud Tech</h3>
      </GlowCard>
      <GlowCard glowColor="orange">
        <h3 className="text-xl font-bold font-syne text-center mt-10">Agentes AI</h3>
      </GlowCard>
    </div>
  );
}
