import { createTheme } from "@material-ui/core";

// A custom theme for this app
const theme = createTheme({
  palette: {
    type: 'dark',
    primary: {
      main: '#29b6f6ff',
      light: '#73e8ffff',
      dark: '#0086c3ff',
    },
    secondary: {
      main: '#ff9800ff',
      light: '#ffc947ff',
      dark: '#c66900ff',
    },
    background: {
      default: '#e6e6e6'
    }
  },
});

export default theme;