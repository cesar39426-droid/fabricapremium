import React, { Suspense } from "react";
import GenerativeMountainScene from "@/components/ui/mountain-scene";

export default function DemoMountainScene() {
  return (
    <main className="relative w-full h-screen bg-[#020818] overflow-hidden text-slate-100 flex items-center justify-center">
      <Suspense fallback={<div className="w-full h-full bg-[#020818]" />}>
        <GenerativeMountainScene />
      </Suspense>
      
      <div className="z-10 text-center pointer-events-none">
        <h1 className="text-5xl md:text-8xl font-black font-syne drop-shadow-[0_0_20px_rgba(6,182,212,0.8)]">
            WEBGL <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-purple-500">MOUNTAINS</span>
        </h1>
        <p className="mt-4 text-cyan-200 tracking-widest font-semibold uppercase text-sm">Living Experience // 2026</p>
      </div>
    </main>
  );
}
