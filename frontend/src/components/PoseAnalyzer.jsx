import { useEffect } from "react";
import { Pose } from "@mediapipe/pose";
import { Camera } from "@mediapipe/camera_utils";

const PoseAnalyzer = ({ videoRef, onSignals }) => {
  useEffect(() => {
    if (!videoRef.current) return;

    const pose = new Pose({
      locateFile: (file) =>
        `https://cdn.jsdelivr.net/npm/@mediapipe/pose/${file}`,
    });

    pose.setOptions({
      modelComplexity: 1,
      smoothLandmarks: true,
      enableSegmentation: false,
      minDetectionConfidence: 0.5,
      minTrackingConfidence: 0.5,
    });

    pose.onResults((results) => {
      if (!results.poseLandmarks) return;

      // VERY SIMPLE ABSTRACT METRICS
      const leftHip = results.poseLandmarks[23];
      const rightHip = results.poseLandmarks[24];
      const centerY = (leftHip.y + rightHip.y) / 2;

      const stabilityScore = 1 - Math.abs(centerY - 0.5);

      const posture =
        centerY < 0.45 ? "leaning_forward" :
        centerY > 0.55 ? "leaning_back" :
        "neutral";

      onSignals({
        posture,
        stability: Number(stabilityScore.toFixed(2)),
      });
    });

    const camera = new Camera(videoRef.current, {
      onFrame: async () => {
        await pose.send({ image: videoRef.current });
      },
      width: 480,
      height: 360,
    });

    camera.start();
  }, [videoRef, onSignals]);

  return null;
};

export default PoseAnalyzer;


