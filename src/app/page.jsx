"use client"; 
import Image from "next/image";
import { assets } from "../../assets/assets";
import { motion } from "motion/react"; 

// Animación de crecimiento desde abajo
const AppearFromBottom = ({ text, className }) => {
  return (
    <motion.div
      initial={{ opacity: 0, scaleY: 0.5, y: 20 }}
      animate={{ opacity: 1, scaleY: 1, y: 0 }}
      transition={{ duration: 0.5, ease: "easeOut", type: "spring", stiffness: 100 }}
      className={className}
    >
      {text}
    </motion.div>
  );
};

// Animación de glitch para el nombre
const GlitchText = ({ text, className }) => {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: [1, 0.5, 1, 0.8, 1], x: [0, -2, 2, -1, 1, 0] }}
      transition={{ duration: 2, repeat: Infinity, repeatType: "reverse" }}
      className={`relative ${className}`}
    >
      {text}
      {/* red layer */}
      <motion.div
        className="absolute top-0 left-0 w-full h-full text-red-500 opacity-50"
        animate={{ x: [0, -1, 1, -0.5, 0] }}
        transition={{ duration: 0.1, repeat: Infinity, repeatType: "reverse" }}
      >
        {text}
      </motion.div>
      {/* blue layer */}
      <motion.div
        className="absolute top-0 left-0 w-full h-full text-blue-500 opacity-50"
        animate={{ x: [0, 1, -1, 0.5, 0] }}
        transition={{ duration: 0.1, repeat: Infinity, repeatType: "reverse" }}
      >
        {text}
      </motion.div>
    </motion.div>
  );
};

// Animación de disolvencia
const FadeInText = ({ text, className }) => {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 2, ease: "easeInOut" }}
      className={className}
    >
      {text}
    </motion.div>
  );
};

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-8 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col items-center text-center">
        {/* Imagen de perfil */}
        <Image
          src={assets.profile_picture}
          alt="Profile Ronny Ascencio"
          width={180}
          height={180}
          priority
          className="rounded-lg border-2 border-gray-200 mb-6"
        />

        {/* Saying hello */}
        <AppearFromBottom text="Hola, Hello, Bonjour!" className="text-2xl font-bold text-pink-500" />


        {/* fade in effect text */}
        <FadeInText text="I am" className="text-2xl font-bold mt-6 text-white-900" />
        <FadeInText text="Ronny Ascencio" className="text-4xl font-bold mt-4 text-white-900" />

        {/* glitch effect for my text */}
        <GlitchText text="Python Developer | Digital Artist" className="text-xl text-gray-500 mt-2" />
      </main>

      {/* Footer */}
      <footer className="mt-10 flex gap-6 flex-wrap items-center justify-center text-gray-600 text-sm">
        <a href="https://github.com/ronnyascencio" className="hover:text-black transition">GitHub</a>
        <a href="https://linkedin.com/in/ronnyascencio" className="hover:text-black transition">LinkedIn</a>
        <a href="mailto:ronnycompartist@gmail.com" className="hover:text-black transition">Email</a>
        <a>ronnycompartis@gmail.com</a>
      </footer>
    </div>
  );
}
