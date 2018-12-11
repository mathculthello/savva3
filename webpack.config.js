const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");

module.exports = {
  optimization: {
    splitChunks: {
      cacheGroups: {
        styles: {
          name: 'styles',
          test: /\.(sa|sc|c)ss$/,
          chunks: 'all',
          enforce: true
        }
      }
    }
  },
  plugins: [
    new MiniCssExtractPlugin({ filename: '[name].css', }),
    new OptimizeCSSAssetsPlugin()
  ],
  entry: {
    common: './webpack-src/common.js',
    index: './webpack-src/index.js',
    calenda: './webpack-src/calenda.js',
    base: './webpack-src/base.js',
  },
  devtool: 'source-map',
  output: {
    path: path.resolve(__dirname, 'static-dist/webpack'),
    filename: '[name].js',
    publicPath: '/static/webpack/',
  },
  module: {
    rules: [
      {
        test: /\.scss$/, use: [
          MiniCssExtractPlugin.loader,
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
