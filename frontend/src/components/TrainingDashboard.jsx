import { useRef, useState } from "react";
import CameraFeed from "./CameraFeed";
import PoseAnalyzer from "./PoseAnalyzer";
import MicAnalyzer from "./MicAnalyzer";
import { sendPerception } from "../services/api";


const TrainingDashboard = () => {
  const videoRef = useRef(null);

  const [signals, setSignals] = useState({});
  const [feedback, setFeedback] = useState("");

  const updateSignals = (newSignals) => {
    setSignals((prev) => ({ ...prev, ...newSignals }));
  };

  const sendToBackend = async () => {
    try {
      const payload = {
        student_id: 1,
        user_input: "I feel tense while practicing",
        signals,
      };

      const result = await sendPerception(payload);
      setFeedback(result.response);
    } catch (err) {
      console.error("Backend error:", err);
    }
  };

  return (
    <div style={{ padding: "16px" }}>
      <h2>Virtual Martial Arts Training</h2>
      <pre>{JSON.stringify(signals, null, 2)}</pre>


      <CameraFeed videoRef={videoRef} />

      <PoseAnalyzer videoRef={videoRef} onSignals={updateSignals} />
      <MicAnalyzer onSignals={updateSignals} />

      <div style={{ marginTop: "12px" }}>
        <p>Posture: {signals.posture || "-"}</p>
        <p>Stability: {signals.stability ?? "-"}</p>
        <p>Voice tension: {signals.voice_tension || "-"}</p>
      </div>

      <button onClick={sendToBackend} style={{ marginTop: "12px" }}>
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
