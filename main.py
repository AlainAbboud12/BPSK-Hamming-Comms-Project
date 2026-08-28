import BPSK_final as BPSK_final


def text_to_bits(text):
    """Convert text into a flat list of 8-bit values."""
    bits = []

    for character in text:
        binary = format(ord(character), "08b")
        bits.extend(int(bit) for bit in binary)

    return bits


def bit_error_rate(original, recovered):
    """Return the bit error rate for two equal-length binary lists."""
    if len(original) != len(recovered):
        raise ValueError("Original and recovered bit lists must have the same length.")
    if len(original) == 0:
        return 0.0
    errors = sum(a != b for a, b in zip(original, recovered))
    return errors / len(original)


def main():
    # Get the message and noise level from the user.
    message = input("Enter a string: ")
    noise_std = float(input("Enter noise standard deviation: "))

    # Convert the message to bits.
    message_bits = text_to_bits(message)

    print(f"Original text: {message}")
    print(f"Original bits: {message_bits}")

    # Run encoding, modulation, noise, demodulation, and decoding.
    received_text = BPSK_final.noise_filtering1(
        noise_std,
        message_bits
    )
    # Run the noise filtering without Hamming encoding/decoding.
    received_text1 = BPSK_final.noise_filtering(
        noise_std,
        message_bits
      )

    print(f"Received text: {received_text}")
    print(f"Received text without Hamming: {received_text1}")

    # Comparison over many noise levels using bit error rate (BER)
    noiselvl = BPSK_final.numpy.linspace(0, 10, 20)
    ber_without = []
    ber_with = []

    for i, x in enumerate(noiselvl):
        data = BPSK_final.numpy.random.randint(0, 2, 1000).tolist()

        signal_without = BPSK_final.modulate(data)
        noisy_signal_without = BPSK_final.add_noise(signal_without, x)
        recovered_without = BPSK_final.demodulate(noisy_signal_without, len(data))
        ber_without.append(bit_error_rate(data, recovered_without))

        encoded = BPSK_final.encode_data(data)
        signal_with = BPSK_final.modulate(encoded)
        noisy_signal_with = BPSK_final.add_noise(signal_with, x)
        recovered_with = BPSK_final.demodulate(noisy_signal_with, len(encoded))
        decoded_bits = BPSK_final.decode_bits(recovered_with)
        ber_with.append(bit_error_rate(data, decoded_bits))

        print(
            f"Noise level: {x}, "
            f"BER without Hamming: {ber_without[i]}, "
            f"BER with Hamming: {ber_with[i]}"
        )

    # Plotting the results
    BPSK_final.plt.plot(noiselvl, ber_without, label="Without Hamming")
    BPSK_final.plt.plot(noiselvl, ber_with, label="With Hamming")
    BPSK_final.plt.xlabel("Noise level")
    BPSK_final.plt.ylabel("Bit Error Rate")
    BPSK_final.plt.title("BER vs Noise with and without Hamming Code")
    BPSK_final.plt.legend()
    BPSK_final.plt.show()


if __name__ == "__main__":
    main()