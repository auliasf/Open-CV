fpsLimit = 1
startTime = time.time()

while True:
    ret,img = cap.read()
    img = cv2.flip(img,1)
    for x in range (330,340,1):
        for y in range (220,340,1):
            color = img [x,y]
            colorB = img [y,x,0]
            colorG = img [y,x,1]
            colorC = img [y,x,2]

    print('B G R = ', color)
    cv2.imshow("Color tracking",img)

    if clf.predict([color]) == 'biru':
        print ("Biru")

    elif clf.predict([color]) == 'hijau':
        print ("Hijau")

    elif clf.predict([color]) == 'kuning':
        print ("Kuning")

    elif clf.predict([color]) == 'merah':
        print ("Merah")

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
