import { StrictMode } from "react"
import { createRoot } from "react-dom/client"

import "./style/index.css"
import { ThemeProvider } from "@/contexts/theme-provider"
import MainRoutes from "./routes"

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <ThemeProvider>
      <MainRoutes/>
    </ThemeProvider>
  </StrictMode>
)
