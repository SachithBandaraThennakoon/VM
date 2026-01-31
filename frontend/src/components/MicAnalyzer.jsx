import { useRef } from "react";

const MicAnalyzer = ({ onSignals }) => {
  const audioContextRef = useRef(null);
  const analyserRef = useRef(null);
  const dataArrayRef = useRef(null);
  const sourceRef = useRef(null);
  const startedRef = useRef(false);

  const startMic = async () => {
    if (startedRef.current) return;
    startedRef.current = true;

    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

      const audioContext = new AudioContext();
      await audioContext.resume(); // 🔑 IMPORTANT

      const analyser = audioContext.createAnalyser();
      analyser.fftSize = 2048;

      const source = audioContext.createMediaStreamSource(stream);
      source.connect(analyser);

      const dataArray = new Uint8Array(analyser.fftSize);

      audioContextRef.current = audioContext;
      analyserRef.current = analyser;
      dataArrayRef.current = dataArray;
      sourceRef.current = source;

      analyze();
    } catch (err) {
      console.error("Mic error:", err);
    }
  };

  const analyze = () => {
    if (!analyserRef.current) return;

    analyserRef.current.getByteTimeDomainData(dataArrayRef.current);

    // RMS volume
    let sum = 0;
    for (let i = 0; i < dataArrayRef.current.length; i++) {
      const v = (dataArrayRef.current[i] - 128) / 128;
      sum += v * v;
    }
    const rms = Math.sqrt(sum / dataArrayRef.current.length);

    // Zero crossing rate
    let zeroCrossings = 0;
    for (let i = 1; i < dataArrayRef.current.length; i++) {
      if (
        (dataArrayRef.current[i - 1] < 128 &&
          dataArrayRef.current[i] >= 128) ||
        (dataArrayRef.current[i - 1] > 128 &&
          dataArrayRef.current[i] <= 128)
      ) {
        zeroCrossings++;
      }
    }

    const volume =
    rms > 0.04 ? "high" :
    rms > 0.015 ? "medium" :
    "low";

    const pace =
    zeroCrossings > 120 ? "fast" :
    zeroCrossings > 60 ? "normal" :
    "slow";


    const voice_tension =
      volume === "high" && pace === "fast" ? "high" : "normal";

    onSignals({ volume, pace, voice_tension });

    requestAnimationFrame(analyze);
  };

  return (
    <button onClick={startMic} style={{ marginTop: "8px" }}>
      Enable Microphone
    </button>
  );
};

export default MicAnalyzer;
