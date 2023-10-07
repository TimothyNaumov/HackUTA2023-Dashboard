import "@mantine/core/styles.css";
import { MantineProvider } from "@mantine/core";
import { theme } from "./theme";

import Dashboard from "./Pages/Dashboard";

export default function App() {
  return <MantineProvider theme={theme}>

      <Dashboard />

    </MantineProvider>;
}
