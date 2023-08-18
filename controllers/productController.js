const Product = require("../models/ProductModel");

exports.getAllProducts = async (req, res) => {
  const products = await Product.find();
  res.json(products);
};

exports.getProductBySearch = async (req, res) => {
  res.send("");
};
