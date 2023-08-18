const express = require("express");
const app = express();
const db = require("./config/db");
const cors = require("cors");
const port = 8080;

// Middleware
app.use(express.json());
app.use(cors());

// Routes
const productRoutes = require("./routes/productRoutes");

app.use("/product", productRoutes);

// Start the server
module.exports = app;
