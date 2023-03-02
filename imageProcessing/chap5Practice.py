import cv2 as cv
import numpy as np

matrix = np.random.randint(0, 100, 20).reshape(4, 5)
print(f"default : \n{matrix}")
print(f"sort every row :\n {cv.sort(matrix, cv.SORT_EVERY_ROW)}")
print(f"sort every column :\n {cv.sort(matrix, cv.SORT_EVERY_COLUMN)}")

# # 임의 난수 생성
#
# # 행렬 원소 정렬
# ck_time(0)
# sort1 = cv2.sort(m, cv2.SORT_EVERY_ROW)  # 행단위 오름차순
# sort2 = cv2.sort(m, cv2.SORT_EVERY_COLUMN)  # 열단위(세로) 오름차순
# sort3 = cv2.sort(m, cv2.SORT_EVERY_ROW + cv2.SORT_DESCENDING)  # 행단위(가로) 내림차순

# windows_title = "ville"
# image = cv.imread("source/paris.jpg")
# # london = cv.imread("source/bridge.jpg")
# #
#
# print(f'mean of image\'s channel : {cv.mean(image)}')
# print(f'sum of image\'s channel : {cv.sumElems(image)}')
# # cv.imshow("ville", image)
# # cv.imshow("bridge", london)
# cv.imshow("subtract", cv.subtract(image, london))
# cv.imshow("absdiff", cv.absdiff(image, london))
# cv.imshow("bitwise_xor : ", cv.bitwise_not(image, london))

# matrix = np.array([1, 2, 3, 4, 5, 6], np.float32).reshape(2, 3)
# print(f'sample : \n {matrix}')
# print(
#     f'dot product of matrix and transposed matrix (using cv.gemm()): \n {cv.gemm(matrix, matrix, 1.0, None, 1.0, flags=cv.GEMM_1_T)}')
#
# matrix_square = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], np.float32).reshape(3, 3)
# ret, inv = cv.invert(matrix_square, cv.DECOMP_LU)
#
# if ret:
#     dst1 = inv.dot()
# print(f"invert : \n {cv.invert(matrix_square, flag = cv.DECOMP_LU)}")
# # cv.waitKey(0)
# blue, green, red = cv.split(image)
# # # print(f'b, g, r color channels : \n {image[0][:5]} \n')
# part_of_blue = blue[1][:9].reshape(3, 3)
# print(part_of_blue)
# print(cv.sort(part_of_blue, cv.SORT_EVERY_ROW))
# print(f'b color channels : \n {blue[0][:5]} \n')
# print(f'g color channels : \n {green[0][:5]} \n')
# # print(f'r color channels : \n {red[0][:5]} \n')
#
# blue_array = np.array(blue[0][:5], np.float32)
# # print(f"array of the part of blue channel :\n {blue_array}")
# # print(f"ln :\n {cv.log(blue_array)}")
# print(f"blue + green : \n {cv.add(blue[0][:5], green[0][:5])}")

# log_img = cv.log(image)
# print(log_img)

# flip method

# while True:
#     cv.imshow(f"{windows_title}", cv.flip(image, 1))
#     cv.imshow(f"{windows_title} : repeated", cv.repeat(image, 2, 2))
# cv.imshow(f"{windows_title} : default image", image)
# cv.imshow(f"{windows_title} : blue channel", blue)
# cv.imshow(f"{windows_title} : green channel", green)
# cv.imshow(f"{windows_title} : red channel", red)
#     cv.imshow(f"{windows_title} : blue green red channels", green + red)
if cv.waitKey(0) == ord("q"):
    cv.destroyAllWindows
