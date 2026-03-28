"use client";

import React from "react";
import { Radar, IconContainer } from "@/components/ui/radar-effect";
import { 
  FileText, 
  CircleDollarSign, 
  Layout, 
  Wrench, 
  Server, 
  Github, 
  Database 
} from "lucide-react";

export default function DemoRadarEffect() {
  return (
    <div className="flex min-h-screen w-full items-center justify-center bg-[#020818] overflow-hidden">
      <div className="relative flex h-96 w-full max-w-3xl flex-col items-center justify-center space-y-4 px-4 m-auto">
        
        {/* Row 1 */}
        <div className="mx-auto w-full max-w-3xl">
          <div className="flex w-full items-center justify-center space-x-10 md:justify-between md:space-x-0 relative z-50">
            <IconContainer
              text="Desarrollo Web"
              delay={0.2}
              icon={<FileText className="h-6 w-6 text-cyan-400" />}
            />
            <IconContainer
              delay={0.4}
              text="Conversión B2B"
              icon={<CircleDollarSign className="h-6 w-6 text-cyan-400" />}
            />
            <IconContainer
              text="Diseño UI/UX"
              delay={0.3}
              icon={<Layout className="h-6 w-6 text-cyan-400" />}
            />
          </div>
        </div>
        
        {/* Row 2 */}
        <div className="mx-auto w-full max-w-md relative z-50">
          <div className="flex w-full items-center justify-center space-x-10 md:justify-between md:space-x-0">
            <IconContainer
              text="Mantenimiento"
              delay={0.5}
              icon={<Wrench className="h-6 w-6 text-cyan-400" />}
            />
            <IconContainer
              text="DevOps & AWS"
              delay={0.8}
              icon={<Server className="h-6 w-6 text-cyan-400" />}
            />
          </div>
        </div>

        {/* Row 3 */}
        <div className="mx-auto w-full max-w-3xl relative z-50">
          <div className="flex w-full items-center justify-center space-x-10 md:justify-between md:space-x-0">
            <IconContainer
              delay={0.6}
              text="Git Pipelines"
              icon={<Github className="h-6 w-6 text-cyan-400" />}
            />
            <IconContainer
              delay={0.7}
              text="CMS / Base de Datos"
              icon={<Database className="h-6 w-6 text-cyan-400" />}
            />
          </div>
        </div>

        {/* Radar Background */}
        <Radar className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2" />
        
        <div className="absolute bottom-0 z-[41] h-px w-full bg-gradient-to-r from-transparent via-cyan-900 to-transparent" />
      </div>
    </div>
  );
}
