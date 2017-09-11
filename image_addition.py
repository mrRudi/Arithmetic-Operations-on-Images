import cv2

#завантаження зображень
art = cv2.imread("art.jpg", cv2.IMREAD_COLOR)
hole = cv2.imread("hole.jpg", cv2.IMREAD_COLOR)

#зменшення розмірів зображення
art = cv2.resize(art,(640, 360))
hole = cv2.resize(hole,(320, 180))

cv2.imshow("art", art)
cv2.imshow("hole", hole)

#для розміщення в лівому верхньому кутку зображення треба бикористати побітові операції
#так як дира не є прямокутною областю, то виділим місце де вона буде
rows,cols,chanels = hole.shape
pole = art[0:rows,0:cols]

#створюєм зображення дири в відтінках сірого
gray = cv2.cvtColor(hole,cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray)

#створюєм маску
ret,mask = cv2.threshold(gray,40,255,cv2.THRESH_BINARY_INV)

cv2.imshow("mask", mask)

#створюєм зворотню маску
mask_inv = cv2.bitwise_not(mask)

#затемним область з дирою на арті
inner = cv2.bitwise_and(pole,pole,mask=mask_inv)

#візьмем лише область з дирою
front = cv2.bitwise_and(hole,hole,mask=mask)

#повтавим зображення дири на арт
add = cv2.add(inner,front)

cv2.imshow("add",add)

#зміним основне зображення
art[0:rows,0:cols] = add

cv2.imshow("with hole", art)

cv2.waitKey(0)
cv2.destroyAllWindows()