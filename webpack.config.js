const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const path = require('path');

module.exports = {
  plugins: [
	  new MiniCssExtractPlugin({
		  filename: "[name].css",
//		  chunkFilename: "[id].css"
	  })
  ],
  entry: {
    common: './webpack-src/common.js',
    index: './webpack-src/index.js',
    calenda: './webpack-src/calenda.js',
    base: './webpack-src/base.js',
  },
  devtool: 'source-map',
  output: {
    path: path.resolve(__dirname,'static-dist/webpack'),
    filename: '[name].js',
    publicPath: '/static/webpack/',
  },
  module: {
  rules: [
    { test: /\.scss$/, use: [
      MiniCssExtractPlugin.loader,
      //'style-loader',
      'css-loader',
      'sass-loader',
    ],
    },
    {
          test: /\.(js|jsx)$/,
          exclude: /node_modules/,
          use: ['babel-loader']
    },
    {
      test: /\.(graphql|gql)$/,
      exclude: /node_modules/,
      loader: 'graphql-tag/loader',
    },
  ]
  }
};
