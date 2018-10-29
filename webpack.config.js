const path = require('path');

module.exports = {
  entry: {
    common: './webpack-src/common.js',
    index: './webpack-src/index.js',
    calenda: './webpack-src/calenda.js',
  },

  output: {
    path: path.resolve(__dirname,'pages/static/webpack'),
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
  ]
  }
};
