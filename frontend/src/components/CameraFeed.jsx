import { useEffect } from "react";

const CameraFeed = ({ videoRef }) => {
  useEffect(() => {
    let stream;

    async function setupCamera() {
      stream = await navigator.mediaDevices.getUserMedia({
        video: true,
        audio: false,
      });

      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        videoRef.current.muted = true;     // IMPORTANT
        videoRef.current.playsInline = true;

        videoRef.current.onloadeddata = () => {
          videoRef.current.play().catch(() => {});
        };

      }
    }
    

    setupCamera();

    return () => {
      if (stream) {
        stream.getTracks().forEach((track) => track.stop());
      }
    };
  }, [videoRef]);

  return (
    <video
      ref={videoRef}
      style={{ width: "480px", borderRadius: "8px" }}
    />
  );
};

export default CameraFeed;
