import numpy as numpy
from math import pi
import matplotlib.pyplot as plt
from Hamming_Code import hamming_encode, hamming_decode

SAMPLES_PER_BIT = 100
CARRIER_FREQ = 4


def encode_data(data):
    """Hamming(7,4)-encode a list of bits, 4 bits at a time."""
    encoded = []
    for j in range(0, len(data), 4):
        encoded += hamming_encode(data[j:j + 4])
    return encoded


def modulate(encoded):
    """Turn encoded bits into a BPSK sine-wave signal."""
    signal = numpy.array([])
    for i in range(len(encoded)):
        x = numpy.linspace(i, i + 1, SAMPLES_PER_BIT)
        y = 1 if encoded[i] == 1 else -1
        k = y * numpy.sin(2 * pi * CARRIER_FREQ * x)
        signal = numpy.concatenate((signal, k))
    return signal


def add_noise(signal, noise_std):
    """Add Gaussian noise to a signal."""
    error = numpy.random.normal(0, noise_std, len(signal))
    return signal + error


def demodulate(signal, num_bits):
    """Recover bit guesses from a noisy signal via correlation detection."""
    guess = []
    for i in range(num_bits):
        x = numpy.linspace(i, i + 1, SAMPLES_PER_BIT)
        k = numpy.sin(2 * pi * CARRIER_FREQ * x)
        product = k * signal[i * SAMPLES_PER_BIT:(i + 1) * SAMPLES_PER_BIT]
        total = numpy.sum(product)
        guess.append(0 if total < 0 else 1)
    return guess


def decode_bits(guess):
    """Hamming-decode a list of received bits, 7 bits at a time."""
    p = []
    for i in range(0, len(guess), 7):
        p += hamming_decode(guess[i:i + 7])
    return p


def bits_to_text(bits):
    """Convert a flat bit list (8 bits per char) back into a string."""
    chars = []
    for i in range(0, len(bits), 8):
        n = ''.join(map(str, bits[i:i + 8]))
        chars.append(chr(int(n, 2)))
    return ''.join(chars)


def noise_filtering1(noise_std, data):
    """Full pipeline: encode -> modulate -> add noise -> demodulate -> decode -> text."""
    encoded = encode_data(data)
    signal = modulate(encoded)
    noisy_signal = add_noise(signal, noise_std)
    guess = demodulate(noisy_signal, len(encoded))
    decoded_bits = decode_bits(guess)
    return bits_to_text(decoded_bits)


# if __name__ == "__main__":
#     noiselvl = numpy.linspace(0, 10, 20)
#     list1 = [0] * 20
#     for i, x in enumerate(noiselvl):
#         data = numpy.random.randint(0, 2, 1000).tolist()
#         list1[i] = noise_filtering(x, data)
#         print(list1[i])
#
#     plt.plot(noiselvl, list1)
#     plt.xlabel("Noise level")
#     plt.ylabel("Error rate")
#     plt.show()