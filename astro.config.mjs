import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import { fileURLToPath, URL } from 'url';

// https://astro.build/config
export default defineConfig({
  integrations: [react()],
  output: 'static',
  build: {
    format: 'file',
  },
  vite: {
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url)),
      },
    },
  },
});
