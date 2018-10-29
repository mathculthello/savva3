const path = require('path');

module.exports = {
  entry: {
    main: './frontend/index.js',
    calenda: './frontend/calenda.js',
  },

  output: {
    path: path.resolve(__dirname,'pages/static'),
    filename: '[name].js'
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
