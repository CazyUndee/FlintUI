import { defineConfig } from 'astro/config';
import { fileURLToPath } from 'node:url';

export default defineConfig({
  build: {
    format: 'file'
  },
  vite: {
    resolve: {
      alias: {
        '@spec': fileURLToPath(new URL('../packages/spec', import.meta.url))
      }
    }
  }
});
