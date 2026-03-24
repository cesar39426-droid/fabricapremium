import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Float, MeshDistortMaterial, MeshWobbleMaterial, PerspectiveCamera } from '@react-three/drei';

function HexagonMesh({ position }) {
  const meshRef = useRef();

  useFrame((state) => {
    if (meshRef.current) {
      // Rotación orgánica basada en el tiempo (Cerebro: Filosofía Museos 3D)
      meshRef.current.rotation.x = Math.sin(state.clock.getElapsedTime() * 0.4) * 0.3;
      meshRef.current.rotation.y = state.clock.getElapsedTime() * 0.5;
      
      // Movimiento suave de la cámara (Scroll-Reactive Concept)
      const scrollY = window.scrollY;
      state.camera.position.y = Math.sin(scrollY * 0.005) * 1.5;
      state.camera.lookAt(0, 0, 0);
    }
  });

  return (
    <Float speed={3} rotationIntensity={1} floatIntensity={2}>
      <mesh ref={meshRef} position={position} castShadow>
        <torusKnotGeometry args={[1.5, 0.4, 200, 32]} />
        <MeshDistortMaterial
          color="#06B6D4" // Nuven Cyan
          speed={3}
          distort={0.45}
          radius={1}
          metalness={1}
          roughness={0}
          emissive="#8B5CF6" // Purple Glow
          emissiveIntensity={0.6}
        />
      </mesh>
    </Float>
  );
}

export default function Industrial3D() {
  return (
    <div className="scene-container" style={{ width: '100%', height: '100%', cursor: 'grab' }}>
      <Canvas shadows camera={{ position: [0, 0, 10], fov: 45 }}>
        <color attach="background" args={['#050810']} />
        <ambientLight intensity={0.2} />
        <spotLight position={[10, 15, 10]} angle={0.2} penumbra={1} intensity={25} castShadow />
        <pointLight position={[-10, -10, -10]} intensity={1.5} color="#8B5CF6" />
        
        <HexagonMesh position={[0, 0, 0]} />
        
        {/* Grilla de ingeniería V4 (Más sutil y expandida) */}
        <gridHelper args={[50, 50, "#8B5CF6", "#1A1A1A"]} rotation={[Math.PI / 2, 0, 0]} position={[0, 0, -4]} />
        
        {/* Nebulosa de datos en el fondo */}
        <fog attach="fog" args={['#050810', 5, 20]} />
      </Canvas>
    </div>
  );
}
