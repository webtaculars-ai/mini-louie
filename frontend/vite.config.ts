import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/summarize": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
    },
  },
});
