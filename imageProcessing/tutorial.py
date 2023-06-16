import numpy as np, cv2

theta = 20 * np.pi / 180  # 회전할 라디안 각도 계산
rot_mat = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]], np.float32)  # 넘파이 행렬 생성

pts1 = np.array([(30, 30), (400, 70),
                 (135, 50), (500, 60), (100, 55)], np.float32)
pts2 = cv2.gemm(pts1, rot_mat, 1, None, 1, flags=cv2.GEMM_2_T)

for i, (pt1, pt2) in enumerate(zip(pts1, pts2)):
    print("pts1[%d] = %s, pst2[%d]= %s" % (i, pt1, i, pt2))

## 영상 생성 및 4개의 좌표 그리기
image = cv2.imread("source/paris.jpg")
cv2.polylines(image, [np.int32(pts1)], True, (0, 255, 100), 2)
cv2.polylines(image, [np.int32(pts2)], True, (255, 255, 0), 3)
cv2.imshow("polylines", image)

if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
