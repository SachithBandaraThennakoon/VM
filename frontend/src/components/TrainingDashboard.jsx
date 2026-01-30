import { useRef, useState } from "react";
import CameraFeed from "./CameraFeed";
import PoseAnalyzer from "./PoseAnalyzer";
import { sendPerception } from "../services/api";

const TrainingDashboard = () => {
  const videoRef = useRef(null);

  // ✅ Signals from MediaPipe
  const [signals, setSignals] = useState({});

  // ✅ AI feedback from backend
  const [feedback, setFeedback] = useState("");

  const sendToBackend = async () => {
    try {
      const payload = {
        student_id: 1,
        user_input: "I feel tense while practicing",
        signals: signals,
      };

      const result = await sendPerception(payload);
      setFeedback(result.response);
    } catch (err) {
      console.error("Backend error:", err);
    }
  };

  return (
    <div>
      <h2>Virtual Martial Arts Training</h2>

      <CameraFeed videoRef={videoRef} />
      <PoseAnalyzer videoRef={videoRef} onSignals={setSignals} />

      <div style={{ marginTop: "12px" }}>
        <h4>Posture: {signals.posture || "-"}</h4>
        <h4>Stability: {signals.stability ?? "-"}</h4>
      </div>

      <button style={{ marginTop: "12px" }} onClick={sendToBackend}>
        Ask Master
      </button>

      <div style={{ marginTop: "16px" }}>
        <h3>Master Feedback</h3>
        <p>{feedback}</p>
      </div>
    </div>
  );
};

export default TrainingDashboard;
