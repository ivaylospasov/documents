var path = require("path");
var webpack = require("webpack");
var HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "build"),
    filename: "main.bundle.js"
  },
  plugins: [
    new HtmlWebpackPlugin({
      title: "Correction form",
      template: "index.html",
      files: {
        js: ["build/main.bundle.js"]
      }
    })
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["env"]
          }
        }
      }
    ]
  },
  stats: {
    colors: true
  },
  devtool: "source-map"
};
