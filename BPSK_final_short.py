import BPSK_final


def text_to_bits(text):
    """Convert text into a flat list of 8-bit values."""
    bits = []

    for character in text:
        binary = format(ord(character), "08b")
        bits.extend(int(bit) for bit in binary)

    return bits


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

    print(f"Received text: {received_text}")


if __name__ == "__main__":
    main()