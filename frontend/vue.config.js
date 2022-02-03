/* eslint-disable @typescript-eslint/no-var-requires */
const path = require('path')

module.exports = {
  outputDir: path.resolve(__dirname, '..\\backend\\src\\static'),
  publicPath: process.env.NODE_ENV === 'production'
    ? '/static/'
    : '/'
}
