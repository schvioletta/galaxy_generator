def encode_username(username):
    username = username.lower()
    vector = []
    for symbol in username:
        number = ord(symbol) - 96
        vector.append(number)
    return vector

def show_image(image):
    pass

def main():
    # input name
    username = input("Enter Your Name: \n")
    # print name
    print("Hello " + username)
    # encode username to vector
    encoded_username = encode_username(username)
    print("Encoded username: ")
    print(encoded_username)
    # generate image
    image = None
    # show image + name
    show_image(image)

if __name__ == '__main__':
    main()