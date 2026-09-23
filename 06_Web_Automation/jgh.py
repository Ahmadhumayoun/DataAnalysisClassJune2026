import cv2
import numpy as np
import os

ARUCO_DICT = cv2.aruco.DICT_6X6_250
MARKER_ID = 0
MARKER_SIZE_MM = 50
CUBE_SIZE_MM = 50
OUTPUT_MARKER = os.path.join(os.path.dirname(__file__), "marker.png")


def generate_marker():
    dictionary = cv2.aruco.getPredefinedDictionary(ARUCO_DICT)
    marker_img = cv2.aruco.generateImageMarker(dictionary, MARKER_ID, 400)
    cv2.imwrite(OUTPUT_MARKER, marker_img)
    print(f"Marker saved to {OUTPUT_MARKER} — print it and hold it to the camera")


def get_camera_matrix(w, h):
    focal = max(w, h)
    return np.array([
        [focal, 0, w / 2],
        [0, focal, h / 2],
        [0, 0, 1]
    ], dtype=np.float64)


def draw_cube(frame, rvec, tvec, camera_matrix, dist_coeffs):
    s = CUBE_SIZE_MM / 2.0
    obj_points = np.array([
        [-s, -s, 0], [s, -s, 0], [s, s, 0], [-s, s, 0],
        [-s, -s, -2*s], [s, -s, -2*s], [s, s, -2*s], [-s, s, -2*s]
    ], dtype=np.float64)

    img_points, _ = cv2.projectPoints(obj_points, rvec, tvec, camera_matrix, dist_coeffs)
    pts = img_points.reshape(-1, 2).astype(int)

    # bottom face
    for i in range(4):
        cv2.line(frame, tuple(pts[i]), tuple(pts[(i+1) % 4]), (0, 255, 0), 3)
    # top face
    for i in range(4):
        cv2.line(frame, tuple(pts[4+i]), tuple(pts[4+(i+1) % 4]), (0, 200, 255), 3)
    # vertical edges
    for i in range(4):
        cv2.line(frame, tuple(pts[i]), tuple(pts[i+4]), (255, 100, 0), 2)


generate_marker()

dictionary = cv2.aruco.getPredefinedDictionary(ARUCO_DICT)
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)

cap = None
for i in range(4):
    cap = cv2.VideoCapture(i, cv2.CAP_AVFOUNDATION)
    if cap.isOpened():
        ret, test = cap.read()
        if ret:
            print(f"Camera opened at index {i}")
            break
    cap.release()
    cap = None

if cap is None or not cap.isOpened():
    print("ERROR: No working camera found.")
    exit(1)

print("Hold the printed marker to the camera. Press 'q' to exit.")

rvec = None
tvec = None
smooth_rvec = None
smooth_tvec = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    camera_matrix = get_camera_matrix(w, h)
    dist_coeffs = np.zeros(5)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, rejected = detector.detectMarkers(gray)

    if ids is not None and len(ids) > 0:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        marker_corners = corners[0][0].astype(np.float64)
        obj_points = np.array([
            [-MARKER_SIZE_MM/2,  MARKER_SIZE_MM/2, 0],
            [ MARKER_SIZE_MM/2,  MARKER_SIZE_MM/2, 0],
            [ MARKER_SIZE_MM/2, -MARKER_SIZE_MM/2, 0],
            [-MARKER_SIZE_MM/2, -MARKER_SIZE_MM/2, 0]
        ], dtype=np.float64)

        success, rvec, tvec = cv2.solvePnP(
            obj_points, marker_corners, camera_matrix, dist_coeffs
        )

        if success:
            alpha = 0.4
            if smooth_rvec is None:
                smooth_rvec = rvec.copy()
                smooth_tvec = tvec.copy()
            else:
                smooth_rvec = smooth_rvec * (1 - alpha) + rvec * alpha
                smooth_tvec = smooth_tvec * (1 - alpha) + tvec * alpha

            draw_cube(frame, smooth_rvec, smooth_tvec, camera_matrix, dist_coeffs)

            axis_len = 30
            cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, smooth_rvec, smooth_tvec, axis_len)

    cv2.imshow("AR Marker Tracker", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
