import ShaderBackground from "@/components/ui/shader-background";

const DemoShader = () => {
  return (
    <div className="relative w-screen h-screen flex flex-col items-center justify-center">
      <ShaderBackground />
      <h1 className="text-4xl md:text-6xl font-black text-white z-10 font-syne drop-shadow-2xl">
        WebGL Living Architecture
      </h1>
      <p className="text-white/70 mt-4 max-w-lg text-center z-10 font-raleway">
        Experimentando con algoritmos de shaders oscuros y animaciones calculadas al vuelo por tu GPU.
      </p>
    </div>
  );
};

export { DemoShader };
