import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
//import { VitePluginImages } from 'vite-plugin-images'; // Import the image handling plugin


// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    //VitePluginImages() // Add the image handling plugin to the plugins array

  ],
})
