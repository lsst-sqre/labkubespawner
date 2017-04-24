var buildExtension = require('@jupyterlab/extension-builder').buildExtension;

buildExtension({
        name: 'sqre_labkubespawner',
        entry: './lib/plugin.js',
        outputDir: './sqre_labkubespawner/static'
});
