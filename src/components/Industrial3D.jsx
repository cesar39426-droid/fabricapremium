import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Float, MeshDistortMaterial, MeshWobbleMaterial, PerspectiveCamera } from '@react-three/drei';

function HexagonMesh({ position }) {
  const meshRef = useRef();

  useFrame((state) => {
    if (meshRef.current) {
      meshRef.current.rotation.x = Math.sin(state.clock.getElapsedTime() * 0.5) * 0.2;
      meshRef.current.rotation.y = state.clock.getElapsedTime() * 0.3;
    }
  });

  return (
    <Float speed={2} rotationIntensity={0.5} floatIntensity={1}>
      <mesh ref={meshRef} position={position}>
        <icosahedronGeometry args={[2, 1]} />
        <MeshDistortMaterial
          color="#F97316"
          speed={2}
          distort={0.4}
          radius={1}
          metalness={0.9}
          roughness={0.1}
          emissive="#F97316"
          emissiveIntensity={0.2}
        />
      </mesh>
    </Float>
  );
}

export default function Industrial3D() {
  return (
    <div className="scene-container" style={{ width: '100%', height: '1000px', cursor: 'grab' }}>
      <Canvas shadows>
        <PerspectiveCamera makeDefault position={[0, 0, 8]} />
        <ambientLight intensity={0.5} />
        <spotLight position={[10, 10, 10]} angle={0.15} penumbra={1} intensity={15} castShadow />
        <pointLight position={[-10, -10, -10]} intensity={1} color="#0F172A" />
        
        <HexagonMesh position={[0, 0, 0]} />
        
        {/* Grilla técnica volumétrica */}
        <gridHelper args={[20, 20, "#334155", "#0F172A"]} rotation={[Math.PI / 2, 0, 0]} position={[0, 0, -2]} />
      </Canvas>
    </div>
  );
}
