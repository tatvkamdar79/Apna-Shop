const { Schema, model } = require("mongoose");
const mongoose = require("mongoose");

// Define the schema for the Example model
const ProductSchema = new Schema({
  ProductName: String,
  mrp: Number,
});

// Create the Example model using the schema
const Product = model("Product", ProductSchema);

// Export the Example model
module.exports = Product;
