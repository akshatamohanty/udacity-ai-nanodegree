module.exports = {  
    outputDir: '../docs', 
    publicPath: process.env.NODE_ENV === 'production'
    ? '/udacity-ai-nanodegree/'
    : '/',
    runtimeCompiler: process.env.NODE_ENV === 'production' ? false: true,
}