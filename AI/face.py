import face_recognition
import os
import cv2

KNOWN_DIR = 'known'
UNKNOWN_DIR = 'unknown'
TOLERANCE = 0.7
FRAME_THICKNESS = 3
FONT_THICKNESS = 2



def main():
    known_faces = []
    known_names = []
    for name in os.listdir(f'{KNOWN_DIR}'):
        print(f'Loading known faces for {name}...')
        for filename in os.listdir(f'{KNOWN_DIR}/{name}'):
            print(f'Processing file {filename}...')
            #print(f'Found file for {name} called ==>>{filename}')
            path = f'{KNOWN_DIR}/{name}/{filename}'
            image = face_recognition.load_image_file(path)
            # print(image)
            encodings = face_recognition.face_encodings(image)
            #print(filename,'==>', len(encodings))
            if len(encodings) >= 1:
                encoding = encodings[0]
            else:
                print(f'Did not find any faces in image {filename}')
                continue
            known_faces.append(encoding)
            known_names.append(name)
            #print(encodings.append(known_faces))
    print(f'Processing unknown faces...')
    for filename in os.listdir(UNKNOWN_DIR):
        print(f'Processing filename: {filename}', end ='')
        image = face_recognition.load_image_file(f'{UNKNOWN_DIR}/{filename}')
        location = face_recognition.face_locations(image)
        encodings = face_recognition.face_encodings(image, location)
        # print(f', found {len(encodings)} face(s)')
        # print()
        for face_encoding, face_locations in zip(encodings, location):
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
            if any(results):
                pos = results.index(True)
                print(f'Found {known_names[pos]} in image{filename}.')


if __name__ == '__main__':
    main()
