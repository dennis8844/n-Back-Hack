# n-Back Hack

Looking for a way to excel at the n-Back test? Know a little about programming? No need to be a crazy engineer, just the basic intro-level material such as proccessing arrays/dict. This algo will help you envision what to do in your head (especially processing as a dict).

I did some n-Back testing while being a guinea pig for a study. At first they practically hurt my brain. Luckily, this was the same time I was learning to program and I ran through a thought experiment on how a mind-algo that could provide results. And it did extremely well. So I decided to stub out what I've done in code, so a quasi-algo comes to mind and if you can understand it, you can hack the n-Back0.

# What is a n-Back test?

The n-back task is a continuous performance task that is commonly used as an assessment in psychology and cognitive neuroscience to measure a part of working memory and working memory capacity.[1] The n-back was introduced by Wayne Kirchner in 1958.[2] Some researchers have argued that n-back training may increase IQ, but evidence is mixed.
[from wikipedia](https://en.wikipedia.org/wiki/N-back)

## First things to know

1. Every input needs to be quickly and consistently analyzed where an input fo the same item will return the same result
    - Easy for standard data types, strings, numbers, booleans etc, not so easy for files, especially images
    - in the mind images need to be uniquely named.
        - "red octagon", "blue-square" worked for images of shapes
        - It took creativity with the images of fractals (see mental obscure image naming below)
    - In the computer algo, a simple hash of a file will more than suffice
1. A queue would work best for the store of n-Back data as progressed through the input array. However a LIFO change at every new item and remembering the order is more taxing on the mind, so a simple dict-like approach and a to_check index works much better in my opinion, you'll see that in the code.

## Obscure Image Naming

Obscure images are images that cannot be easily and uniquely defined by what's in them. It takes a little mnemonic connections to name the image. Bacically, come up with the first word or combination of words that come to mind, that's it. An example would be "sinking sun", "wandering coast", "marble gallery", etc. There is no right or wrong, don't think at all, blurt it out and stay consistent. The more you think the more likely you won't think the same the next time you see the image. You can rename the next time you see it if you wish.

## Final thoughts

If would be fun to train a computer vision algo using OpenCV or tensorflow to do the tests. ha.

*Note* I never encountered n-Backs over 5, so kept a mental image of my dict, and assinged a finger for each key/index, as new images were given i kept track of the index with my fingers. Somehow it helped
