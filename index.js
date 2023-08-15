const express = require("express");
const db = require("./db"); // Import the mongoose connection from db.js

// MODELS
const Example = require("./models/exampleModel");
const Product = require("./models/ProductModel");

const app = express();
const port = 8080;

// Define a route handler for the root path
app.get("/", async (req, res) => {
  const newProduct = new Product({
    ProductName: "Cabinet Handle",
    mrp: 2565,
  });

  // Save the document to the database
  await newProduct.save();

  res.send("Document inserted successfully.");
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
