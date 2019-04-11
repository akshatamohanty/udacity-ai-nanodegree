const tf = requre '@tensorflow/tfjs';
import { loadGraphModel } from '@tensorflow/tfjs-converter';

const MODEL_URL = './model.json';

const model = await loadGraphModel(MODEL_URL);
// const cat = document.getElementById('cat');
// model.execute(tf.fromPixels(cat));