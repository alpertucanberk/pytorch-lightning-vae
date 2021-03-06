from .vae import VAE, Stack 
from .resnet18_vae import Resnet18_VAE
from .conv_vae import Convolutional_VAE
from .perceptual_networks import AlexNet
from .perceptual_conv_vae import Perceptual_VAE

__all__ = [
    'VAE', 'Stack'
    'Resnet18_VAE', 'Convolutional_VAE', 'Perceptual_VAE'
]

vae_models = {
    "vae": VAE,
    'resnet18-vae': Resnet18_VAE,
    'conv-vae': Convolutional_VAE,
    'perceptual-vae': Perceptual_VAE
}