import { LiquidButton, MetalButton } from "@/components/ui/liquid-glass-button";

export default function DemoLiquidButton() {
  return (
    <div className="relative w-screen h-screen bg-neutral-900 flex flex-col items-center justify-center gap-10">
      <div className="flex flex-col items-center gap-2">
        <h3 className="text-white/50 text-sm font-syne uppercase tracking-widest">Liquid Glass Variant</h3>
        <div className="relative h-[200px] w-full flex items-center justify-center">
          <LiquidButton className="px-10 py-4 text-white hover:text-cyan-400">
            Conectar CRM
          </LiquidButton> 
        </div>
      </div>

      <div className="flex flex-col items-center gap-4">
        <h3 className="text-white/50 text-sm font-syne uppercase tracking-widest">Metal Buttons</h3>
        <div className="flex flex-row gap-6 flex-wrap justify-center">
          <MetalButton variant="default">Instalar Pipeline</MetalButton>
          <MetalButton variant="primary">Agendar Demo</MetalButton>
          <MetalButton variant="gold">Plan Pro</MetalButton>
        </div>
      </div>
    </div>
  )
}
