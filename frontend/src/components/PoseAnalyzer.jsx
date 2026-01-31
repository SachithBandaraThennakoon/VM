import { useEffect, useRef } from "react";
import { Pose } from "@mediapipe/pose";

const PoseAnalyzer = ({ videoRef, onSignals }) => {
  const poseRef = useRef(null);
  const runningRef = useRef(false);
  const processingRef = useRef(false);
  const rafRef = useRef(null);

  useEffect(() => {
    if (!videoRef.current) return;
    if (poseRef.current) return; // prevent re-init

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
      processingRef.current = false;

      if (!results.poseLandmarks) return;

      const leftHip = results.poseLandmarks[23];
      const rightHip = results.poseLandmarks[24];
      const centerY = (leftHip.y + rightHip.y) / 2;

      const posture =
        centerY < 0.48
          ? "leaning_forward"
          : centerY > 0.52
          ? "leaning_back"
          : "neutral";

      const stability = Math.max(
        0,
        1 - Math.abs(centerY - 0.5) * 2
      );

      onSignals({
        posture,
        stability: Number(stability.toFixed(2)),
      });
    });

    poseRef.current = pose;
    runningRef.current = true;

    const loop = async () => {
      if (!runningRef.current) return;

      const video = videoRef.current;

      // 🔒 CRITICAL SAFETY GUARDS
      if (
        video &&
        video.readyState === 4 &&
        !processingRef.current
      ) {
        try {
          processingRef.current = true;
          await pose.send({ image: video });
        } catch (e) {
          processingRef.current = false;
          console.warn("Pose skipped frame:", e);
        }
      }

      rafRef.current = requestAnimationFrame(loop);
    };

    loop();

    return () => {
      runningRef.current = false;
      if (rafRef.current) cancelAnimationFrame(rafRef.current);
      poseRef.current = null;
    };
  }, [videoRef, onSignals]);

  return null;
};

export default PoseAnalyzer;
