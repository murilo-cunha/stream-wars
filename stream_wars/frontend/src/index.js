import "./index.css";
import React from "react";
import ReactDOM from "react-dom";
import { StreamlitProvider } from "streamlit-component-lib-react-hooks";
import StreamWars from "./StreamWars";

ReactDOM.render(
  <React.StrictMode>
    <StreamlitProvider>
      <StreamWars />
    </StreamlitProvider>
  </React.StrictMode>,
  document.getElementById("root")
);
