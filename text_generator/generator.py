#!/usr/bin/env python3

import fire
import json
import os
import numpy as np
import tensorflow.compat.v1 as tf

from text_generator import model
from text_generator import sample
from text_generator import encoder

# define class
class AI:
    def generate_text(self, input_text):
        #String, which model to use
        model_name='124M_TRAINED'
        #Integer seed for random number generators, fix seed to reproduce results
        seed=None 
        #Number of samples to return total
        nsamples=1 
        #Number of batches (only affects speed/memory).  Must divide nsamples.
        batch_size=1
        # Number of tokens in generated text, if None (default 1023, the maximum)
        length=1023
        #Float value controlling randomness in boltzmann 
        # distribution. Lower temperature results in less random completions. As the
        # temperature approaches zero, the model will become deterministic and
        # repetitive. Higher temperature results in more random completions.
        temperature=0.8 
        # Integer value controlling diversity. 1 means only 1 word is
        # considered for each step (token), resulting in deterministic completions,
        # while 40 means 40 words are considered at each step. 0 (default) is a
        # special setting meaning no restrictions. 40 generally is a good value.
        top_k=40
        # Nucleus sampling: limits the generated guesses to a cumulative probability. 
		# (gets good results on a dataset with top_p=0.9) 
        top_p=1
        #:models_dir : path to parent folder containing model subfolders (i.e. contains the <model_name> folder)
        self.response = "" 

        if batch_size is None:
            batch_size = 1
        assert nsamples % batch_size == 0

        # this is going to give us our current location where our generator.py is
        cur_path = os.path.dirname(__file__) + "/models/" + model_name
        enc = encoder.get_encoder(model_name, os.path.dirname(__file__) + "/models")
        hparams = model.default_hparams()
        with open(os.path.join(cur_path + '/hparams.json')) as f:
            hparams.override_from_dict(json.load(f))

        if length is None:
            length = hparams.n_ctx // 2
        elif length > hparams.n_ctx:
            raise ValueError("Can't get samples longer than window size: %s" % hparams.n_ctx)

        with tf.Session(graph=tf.Graph()) as sess:
            context = tf.placeholder(tf.int32, [batch_size, None])
            np.random.seed(seed)
            tf.set_random_seed(seed)
            output = sample.sample_sequence(
                hparams=hparams, length=length,
                context=context,
                batch_size=batch_size,
                temperature=temperature, top_k=top_k, top_p=top_p
            )

            saver = tf.train.Saver()
            ckpt = tf.train.latest_checkpoint(cur_path)
            saver.restore(sess, ckpt)

            context_tokens = enc.encode(input_text)
            generated = 0
            for _ in range(nsamples // batch_size):
                out = sess.run(output, feed_dict={
                    context: [context_tokens for _ in range(batch_size)]
                })[:, len(context_tokens):]
                for i in range(batch_size):
                    generated += 1
                    # our response/generated text
                    text = enc.decode(out[i])
		    # prefix response with inout text
                    self.response = input_text + text
        # return generated text
        return self.response
# initiate 
ai = AI()
