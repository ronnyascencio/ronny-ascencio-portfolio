/** @type {import('next').NextConfig} */
const nextConfig = {
  output: "export", // Exporta archivos estáticos
  images: {
    unoptimized: true, // Evita problemas con imágenes en GitHub Pages
  },
  basePath: "/ronny-ascencio-portfolio", // Nombre de tu repositorio en GitHub
  assetPrefix: "/ronny-ascencio-portfolio/", // Asegura que los assets se carguen bien
};

export default nextConfig;
