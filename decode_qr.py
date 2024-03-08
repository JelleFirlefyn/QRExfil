import sys
from PIL import Image
from pyzbar.pyzbar import decode


def extract_frames(file_path):
    # Open the GIF file
    with Image.open(file_path) as gif:
        index = 0
        while True:
            try:
                gif.seek(index)
                yield gif.copy()  # Make a copy of the current frame
            except EOFError:
                break
            index += 1


def decode_qr_from_frames(frames):
    decoded_texts = []
    for frame in frames:
        # Use pyzbar to decode the QR code from the frame
        qr_codes = decode(frame)
        for qr_code in qr_codes:
            decoded_texts.append(qr_code.data.decode('utf-8'))
    return decoded_texts


def main(gif_path):
    frames = extract_frames(gif_path)
    decoded_texts = decode_qr_from_frames(frames)

    # Print or handle the decoded text as needed
    for text in decoded_texts:
        print(text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decode_qr.py <path_to_gif>")
        sys.exit(1)

    gif_path = sys.argv[1]
    main(gif_path)
