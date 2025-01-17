import matplotlib
import cv2 as cv
import sys

def encode_username(username):
    username = username.lower()
    vector = []
    for symbol in username:
        number = ord(symbol) - 96
        vector.append(number)
    return vector

def show_image(img):
    if img is None:
        sys.exit("Could not read the image.")

    cv.imshow("Display window", img)
    k = cv.waitKey(0)

def main():
    # input name
    username = input("Enter Your Name: \n")
    # print name
    print("Hello " + username)
    # encode username to vector
    encoded_username = encode_username(username)
    print("Encoded username: ")
    print(encoded_username)
    # show image + name
    img = cv.imread("starry_night.jpg")
    show_image(img)

if __name__ == '__main__':
    main()