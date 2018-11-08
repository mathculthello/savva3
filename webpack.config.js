const path = require('path');

module.exports = {
  entry: {
    common: './webpack-src/common.js',
    index: './webpack-src/index.js',
    calenda: './webpack-src/calenda.js',
    base: './webpack-src/base.js',
  },
  devtool: 'source-map',
  output: {
    path: path.resolve(__dirname,'savva3/static/webpack'),
    filename: '[name].js',
    publicPath: 'static/webpack/',
  },
  module: {
  rules: [
    { test: /\.scss$/, use: [
      'style-loader',
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
