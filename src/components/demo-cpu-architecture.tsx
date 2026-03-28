"use client";

import React from "react";
import { CpuArchitecture } from "@/components/ui/cpu-architecture"

export const Page = () => {
  return (
    <div className="p-4 rounded-xl bg-accent/20">
      <CpuArchitecture />
    </div>
  );
};

export default Page;
