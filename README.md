# Turning Heads with Generative Adversarial Networks

![TP-GAN Synthesis](https://github.com/mease/turning_heads/blob/master/tpgan_examples.png?raw=true)

Large-pose facial images present a challenge for facial recognition models, especially for fully-lateral (profile) poses. The ability to reconstruct a frontal view (frontalization) from a lateral view while preserving the subject's identifying features is useful for improving recognition accuracy on large-pose facial images, and has applications in other fields such as forensics. The frontalization problem is made difficult by several factors, including pose variation, self-occlusion, lighting conditions, and variation in facial expression. Given the large amount of facial image data available today, deep neural networks, and specifically generative adversarial networks (GAN), are well suited to tackle this problem. In this project, we explore deep learning methods for face frontalization using GANs to generate a convincing frontal-view synthesis from a lateral-view input image.

### GAN Architectures
- [Pix2Pix](http://arxiv.org/abs/1611.07004)
- [TP-GAN](http://arxiv.org/abs/1704.04086)

### Data
Data adapted from [NIST Mugshot Identification Database](https://www.nist.gov/srd/nist-special-database-18)
- [Download the formatted data set](https://drive.google.com/file/d/1CibviCTCiQvDah_afgPgpWIDiEv8u_zC/view?usp=sharing)

Code adapted from:
- [Pix2Pix Tensor flow docs](https://github.com/tensorflow/docs/blob/master/site/en/tutorials/generative/pix2pix.ipynb)
- [LightCNN](https://github.com/AlfredXiangWu/LightCNN)
- [TP-GAN official implementation](https://github.com/HRLTY/TP-GAN)
- [TP-GAN Keras implementation](https://github.com/yh-iro/Keras_TP-GAN)