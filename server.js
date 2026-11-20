// Serves Hugo's generated public/ folder on the port Gandi assigns.
const path = require("node:path");
const express = require("express");

const app = express();
const publicDir = path.join(__dirname, "public");

app.use(express.static(publicDir, { extensions: ["html"], maxAge: "1h" }));

// Hugo's 404 page (Terminal ships one)
app.use((req, res) => {
  res.status(404).sendFile(path.join(publicDir, "404.html"));
});

app.listen(process.env.PORT || 8080);
