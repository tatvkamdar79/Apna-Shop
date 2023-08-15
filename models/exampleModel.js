const mongoose = require("mongoose");

// Define the schema for the Example model
const exampleSchema = new mongoose.Schema({
  name: String,
  age: Number,
});

// Create the Example model using the schema
const Example = mongoose.model("Example", exampleSchema);

// Export the Example model
module.exports = Example;
