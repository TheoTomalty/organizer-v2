const path = require('path');
let ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
    mode: "development",
    entry: {
        'login': "./organizer/static/login.js",
    },
    output: {
        path: path.resolve(__dirname, "build"),
        filename: "[name].js",
        publicPath: "/static/",
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                  loader: "babel-loader"
                }
            }
        ]
    }
};